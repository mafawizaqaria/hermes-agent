#!/usr/bin/env bash
set -euo pipefail

baseline="${BASELINE_REF:-}"
if [ -n "$baseline" ]; then
  case "$baseline" in HEAD|NEXT) exit 0 ;; esac
  git rev-parse --verify "refs/tags/$baseline^{commit}" >/dev/null 2>&1 && exit 0
  [[ "$baseline" =~ ^v[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+)?$ ]] || {
    echo "error: invalid release baseline: $baseline" >&2; exit 1;
  }
elif git tag --list 'v*' | grep -Eq '^v[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+)?$'; then
  exit 0
fi

parent="$(gh api "repos/$GITHUB_REPOSITORY" --jq '.parent.full_name // empty')"
[ -n "$parent" ] || exit 0
url="${GITHUB_SERVER_URL:-https://github.com}/$parent.git"

# Fetch only real stable tags, never canaries or branches. Nothing is pushed.
if [ -n "$baseline" ]; then
  git fetch --no-tags "$url" "refs/tags/$baseline:refs/tags/$baseline"
else
  refs="$(git ls-remote --tags --refs "$url" 'refs/tags/v*')"
  refspecs=()
  while read -r sha ref; do
    [[ "$ref" =~ ^refs/tags/v[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+)?$ ]] || continue
    refspecs+=("$ref:$ref")
  done <<< "$refs"
  [ "${#refspecs[@]}" -gt 0 ] || { echo "error: parent has no stable release tags" >&2; exit 1; }
  git fetch --no-tags "$url" "${refspecs[@]}"
  # The parent can be ahead of the fork. Test upgrades from its history,
  # rather than downgrades from releases newer than the commit under test.
  for refspec in "${refspecs[@]}"; do
    ref="${refspec%%:*}"
    if ! git merge-base --is-ancestor "$ref^{commit}" HEAD; then
      git update-ref -d "$ref"
    fi
  done
fi

