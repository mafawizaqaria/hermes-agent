import os
import threading
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler


# ============================================================
# Render Health Check Server
# ============================================================

class HealthCheckHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass


def run_health_server():
    port = int(os.environ.get("PORT", "10000"))

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthCheckHandler
    )

    print(
        f"🌐 Render health server listening on port {port}",
        flush=True
    )

    server.serve_forever()


# ============================================================
# Hermes Model Configuration
# ============================================================

def configure_hermes_model():

    # Hermes home directory
    hermes_home = Path(
        os.environ.get(
            "HERMES_HOME",
            str(Path.home() / ".hermes")
        )
    )

    hermes_home.mkdir(
        parents=True,
        exist_ok=True
    )

    config_path = hermes_home / "config.yaml"

    print(
        f"⚙️ Hermes config: {config_path}",
        flush=True
    )

    # Read existing config if it exists
    config = {}

    if config_path.exists():
        try:
            import yaml

            with open(
                config_path,
                "r",
                encoding="utf-8"
            ) as f:
                config = yaml.safe_load(f) or {}

        except Exception as e:
            print(
                f"⚠️ Could not read existing Hermes config: {e}",
                flush=True
            )
            config = {}

    # Make sure model section exists
    model_config = config.setdefault(
        "model",
        {}
    )

    # ========================================================
    # OpenRouter Free Router
    # ========================================================

    model_config["provider"] = "openrouter"
    model_config["default"] = "openrouter/free"
    model_config["base_url"] = "https://openrouter.ai/api/v1"

    # Save configuration
    try:
        import yaml

        with open(
            config_path,
            "w",
            encoding="utf-8"
        ) as f:
            yaml.safe_dump(
                config,
                f,
                sort_keys=False,
                allow_unicode=True
            )

        print(
            "✅ Hermes model configured:",
            flush=True
        )

        print(
            "   Provider: openrouter",
            flush=True
        )

        print(
            "   Model: openrouter/free",
            flush=True
        )

        print(
            "   Base URL: https://openrouter.ai/api/v1",
            flush=True
        )

    except Exception as e:
        print(
            f"❌ Failed to save Hermes config: {e}",
            flush=True
        )
        raise


# ============================================================
# Start Hermes Gateway
# ============================================================

if __name__ == "__main__":

    # Start Render health server
    threading.Thread(
        target=run_health_server,
        daemon=True
    ).start()

    # Configure Hermes before starting Gateway
    configure_hermes_model()

    print(
        "🚀 Starting Hermes Gateway...",
        flush=True
    )

    # Start Hermes Gateway
    from gateway.run import main

    main()
