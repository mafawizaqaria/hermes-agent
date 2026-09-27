# Chart of Accounts — Mafawiz Real Estate
## Canonical Version 1.0

**Status:** AUTHORITATIVE  
**Business:** مفاوز العقارية  
**Business model:** Saudi real-estate brokerage, marketing, property-management, and related services office.

> This file is the authoritative source for account IDs, names, categories, and permitted use inside the `real-estate-accounting` skill.
>
> Historical Excel files, test datasets, and prior skill versions may contain different account numbers. Those historical numbers do **not** override this file.

---

# 1. Mandatory COA Controls

1. Every account used in a journal entry must exist in this file.
2. Never invent an account number.
3. Never substitute a similar account merely because the intended account is missing.
4. Never silently remap a historical account.
5. A missing/conflicting mapping must be marked `NEEDS_REVIEW`.
6. `NEEDS_REVIEW` is primarily a workflow/status. It is **not automatically** account `9200`.
7. Account `9200` may be used only when the workflow explicitly requires a temporary posted review account and the user/current accounting policy permits it.
8. Control/group accounts are not intended for normal posting when a dedicated child account exists.
9. The current COA overrides historical test workbooks for account identity.
10. Changing this COA is a controlled configuration change and must not happen as a side effect of transaction analysis.

---

# 2. Current Tax Configuration

- `VAT Registered = NO`
- `VAT Number = NONE`
- `VAT Mode = OFF`
- `VAT Rate = 15%` — reference/informational rate only while VAT Mode is OFF
- `RETT Rate = 5%` — reference rate only
- `RETT Mode = TRANSACTION_SPECIFIC`

Tax accounts may exist in the COA for future or exceptional use, but they must not be posted merely because the accounts exist.

---

# 3. Assets

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 1000 | النقد والبنوك — حساب رقابي | Cash & Banks — Control | Current Asset / Control | Control only; use specific bank accounts |
| 1100 | البنك الرئيسي | Main Bank | Current Asset | Posting account |
| 1110 | البنك الإضافي | Additional Bank | Current Asset | Posting account |
| 1200 | الذمم المدينة | Accounts Receivable | Current Asset | Posting account; use Client/Invoice IDs where relevant |
| 1300 | المصروفات المقدمة — حساب رقابي | Prepaid Expenses — Control | Current Asset / Control | Prefer specific prepaid account |
| 1310 | برامج واشتراكات مدفوعة مقدماً | Prepaid Software & Subscriptions | Current Asset | Posting account |
| 1400 | الأصول الثابتة — حساب رقابي | Fixed Assets — Control | Non-current Asset / Control | Prefer specific fixed-asset account |
| 1410 | أجهزة الحاسب والمعدات المكتبية | Computers & Office Equipment | Non-current Asset | Posting account |

### Asset rules
- Collection of an existing receivable: `Dr Bank / Cr 1200 Accounts Receivable`.
- Collection is not new revenue.
- Annual/future-period software may initially be recorded in `1310` where appropriate.
- A qualifying computer/equipment purchase may be recorded in `1410` rather than expensed immediately.
- Depreciation requires an approved policy/basis; do not invent depreciation.

---

# 4. Liabilities

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 2000 | الذمم الدائنة — حساب رقابي | Accounts Payable — Control | Current Liability / Control | Prefer specific payable account |
| 2100 | مستحقات الوسطاء والموردين — حساب رقابي | Broker & Vendor Payables — Control | Current Liability / Control | Prefer specific child account |
| 2130 | مستحقات الوسطاء الخارجيين | External Brokers Payable | Current Liability | Posting account |
| 2200 | مستحقات العمولات — حساب رقابي | Commission Payables — Control | Current Liability / Control | Prefer specific child account |
| 2220 | مستحقات عمولات المسوقين | Marketer Commissions Payable | Current Liability | Posting account |
| 2300 | الضرائب المستحقة — حساب رقابي | Taxes Payable — Control | Current Liability / Control | Do not post without confirmed tax basis |
| 2330 | ضريبة القيمة المضافة المستحقة | VAT Payable | Current Liability | **Disabled while VAT Mode = OFF** |
| 2340 | ضريبة التصرفات العقارية المستحقة | RETT Payable | Current Liability | Use only when office liability is actually established |
| 2400 | أموال الغير — حساب رقابي | Third-Party Funds — Control | Current Liability / Control | Prefer specific child account |
| 2410 | أموال الملاك والعملاء المستحقة لهم | Owner / Client Funds Payable | Current Liability | Posting account for money held for others |
| 2500 | دفعات مقدمة من العملاء | Advances from Clients | Current Liability | Use when amount is an advance, not earned revenue |

### Liability rules
- `2130` and `2220` are different accounts and must never be substituted for each other.
- Money received on behalf of an owner/client normally belongs in `2410`, not revenue.
- Property value passing through the office is not office revenue.
- `2330` exists for controlled future use, but while `VAT Mode = OFF`, posted VAT remains zero unless the business configuration is formally changed.
- `2340` must not be used merely because a property transaction exists. RETT must be transaction-specific and the office's liability must be established.

---

# 5. Equity and Partner Accounts

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 3000 | رأس المال | Capital | Equity | General capital |
| 3100 | مساهمات الشركاء | Partner Contributions | Equity | Actual contributions only |
| 3110 | حساب الشريك الجاري | Partner Current Account | Equity / Current | Amounts owed between partner and office |
| 3200 | سحوبات الشركاء | Partner Drawings | Contra Equity | Personal withdrawals |
| 3210 | تسويات الشركاء | Partner Settlements | Equity / Settlement | Controlled settlements/reclassifications |
| 3300 | توزيعات أرباح الشركاء | Partner Profit Distributions | Contra Equity | Profit distributions only |
| 3900 | الرصيد الختامي — حقوق الملكية | Closing Balance — Equity | Equity Summary | Closing/reporting use |

### Partner rules
- Track the individual partner with `Partner ID`; do not create a new GL code merely because there is more than one partner.
- A partner's personal withdrawal uses `3200`, not an operating expense.
- If a partner personally pays a genuine office expense and the office owes reimbursement, credit `3110` unless documented facts support another partner-account treatment.
- Reimbursement normally clears `3110`; it is not a second expense.
- A capital contribution uses `3100`, not `3110`, unless facts clearly show a current-account movement.
- Profit distribution uses `3300`, not operating expense.

---

# 6. Revenue

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 4000 | الإيرادات — حساب رقابي | Revenue — Control | Revenue / Control | Prefer specific revenue account |
| 4100 | إيرادات الوساطة العقارية | Brokerage Revenue | Operating Revenue | Posting account |
| 4200 | إيرادات التسويق العقاري | Real Estate Marketing Revenue | Operating Revenue | Posting account |
| 4300 | إيرادات إدارة الأملاك | Property Management Revenue | Operating Revenue | Posting account |
| 4400 | إيرادات الخدمات الأخرى — حساب رقابي | Other Service Revenue — Control | Revenue / Control | Prefer specific child account |
| 4410 | إيرادات الاستشارات العقارية | Real Estate Consulting Revenue | Operating Revenue | Posting account |

### Revenue rules
- `4100` is **Brokerage Revenue** in Canonical v1.0.
- `4200` is **Real Estate Marketing Revenue**.
- `4300` is **Property Management Revenue**.
- `4410` is **Real Estate Consulting Revenue**.
- A property sale/purchase value is not revenue merely because Mafawiz facilitated the deal.
- Collection of `1200` is not new revenue.
- If commission is withheld from `2410`, recognize revenue only when documentation supports that the office actually earned the commission.
- Do not count the same revenue at accrual and again at collection.

---

# 7. Direct / Deal-Related Costs

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 5000 | تكاليف الصفقات المباشرة — حساب رقابي | Direct Deal Costs — Control | Expense / Control | Prefer specific child account |
| 5100 | عمولات المسوقين | Marketer Commissions Expense | Expense | Posting account |
| 5200 | عمولات الوسطاء الخارجيين | External Broker Commissions Expense | Expense | Posting account |
| 5300 | تكاليف الصفقة المباشرة الأخرى | Other Direct Deal Costs | Expense | Posting account only when specifically deal-related |

### Direct-cost rules
- `5100`, `5200`, and `5300` are direct/deal-related in Canonical v1.0.
- A general office expense must not be forced into `5300`.
- An advertising cost is `5300` only if it is clearly attributable to a specific deal/property and the accounting policy treats it as direct.
- General brand/office marketing belongs in `6300`.

---

# 8. Operating Expenses

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 6000 | المصروفات التشغيلية — حساب رقابي | Operating Expenses — Control | Expense / Control | Prefer specific account |
| 6100 | إيجار المكتب | Office Rent Expense | Operating Expense | Posting account |
| 6200 | مصروفات الموظفين | Employee Expenses | Operating Expense | Posting account where applicable |
| 6300 | التسويق والإعلان العام | General Marketing & Advertising | Operating Expense | General/non-deal-specific marketing |
| 6400 | الاتصالات — حساب رقابي | Communications — Control | Operating Expense / Control | Prefer specific child account |
| 6420 | الإنترنت | Internet Expense | Operating Expense | Posting account |
| 6500 | البرامج والاشتراكات | Software & Subscriptions Expense | Operating Expense | Period expense after recognition |
| 6600 | النقل والتنقل | Transportation Expense | Operating Expense | Posting account |
| 6700 | الخدمات المهنية | Professional Services Expense | Operating Expense | Posting account |
| 6800 | المصروفات البنكية — حساب رقابي | Banking Expenses — Control | Operating Expense / Control | Prefer specific child account |
| 6810 | الرسوم البنكية | Bank Fees | Operating Expense | Posting account |
| 6900 | مصروفات تشغيلية أخرى | Other Operating Expenses | Operating Expense | Use only when nature is known but no more specific approved account exists |

### Operating-expense rules
- Fixed-asset purchases do not belong here merely because cash was paid.
- Prepaid annual costs do not belong here in full merely because cash was paid.
- Unknown bank movements must not be placed in `6900` simply to make reconciliation work.
- Partner drawings, contributions, settlements, and distributions are not operating expenses.

---

# 9. Transitional / Review Accounts

| Code | Arabic Name | English Name | Type | Posting Rule |
|---|---|---|---|---|
| 9000 | قيد معلق | Suspense Entry | Transitional | Controlled temporary use only |
| 9100 | فرق التسوية | Reconciliation Difference | Transitional | Controlled reconciliation use only |
| 9200 | عمليات تحتاج مراجعة | Items Requiring Review | Transitional | Optional temporary posting account; not the same as status `NEEDS_REVIEW` |

### Transitional-account rules
- `NEEDS_REVIEW` is first a **status/workflow state**.
- Do not automatically post every uncertain transaction to `9200`.
- Use `9200` only when a temporary GL posting is explicitly required by the accounting workflow and supported by policy.
- Do not use `9000`, `9100`, or `9200` to hide an unexplained imbalance.

---

# 10. Entity IDs

Use relevant identifiers where available:

- Transaction ID
- Deal ID
- Property ID
- Owner ID
- Client ID
- Agent ID
- Partner ID
- Invoice ID
- Bank Transaction ID

These IDs are conditional, not universally mandatory.

For a genuinely real-estate/deal-specific transaction, missing essential identifiers or supporting documentation may require `NEEDS_REVIEW`.

---

# 11. Mandatory Integrity Rules

Before confirming any entry:

1. Account exists in Canonical COA v1.0.
2. Debit/credit directions are plausible for account nature.
3. Debits = Credits.
4. Revenue is not duplicated by collection.
5. Property value is not incorrectly treated as office revenue.
6. Third-party funds are separated from revenue.
7. Partner activity is separated from operating expenses.
8. Direct costs and operating expenses are not mixed by intuition.
9. Fixed assets and prepaids are classified correctly.
10. VAT posting agrees with VAT Mode.
11. RETT is transaction-specific.
12. Unknown bank movements are not guessed.
13. Direct reversals use the same accounts in opposite directions.
14. As-Posted and Adjusted/Expected are not silently mixed.
15. Historical account mappings do not override this file.

---

# 12. Legacy / Migration Mapping

This section exists only to prevent old files from being misread.  
It is **not permission to silently rewrite historical entries**.

| Historical/Test Mapping | Canonical v1.0 | Action |
|---|---|---|
| Old `1000 Bank` | `1100 Main Bank` | Map only during an approved migration |
| Old `1100 Accounts Receivable` | `1200 Accounts Receivable` | Do not reinterpret historical rows silently |
| Old `1200 Prepayments` | `1300/1310 Prepaid Expenses` | Select specific prepaid account during migration |
| Old `1300 Funds Held for Others` | `2400/2410 Third-Party Funds Liability` | Analyze substance before migration |
| Old `4000 Brokerage Revenue` | `4100 Brokerage Revenue` | Controlled migration only |
| Old `4100 Marketing Revenue` | `4200 Marketing Revenue` | Important semantic conflict; never auto-map without version context |
| Old `4200 Property Management Revenue` | `4300 Property Management Revenue` | Controlled migration only |
| Old `4300 Other Revenue` | `4400/4410` or another approved account | Requires nature review |
| Test `6950 Unclassified/Review` | No direct canonical equivalent | Use `NEEDS_REVIEW`; use `9200` only if temporary GL posting is explicitly required |
| Test `2130 External Brokers Payable` | `2130 External Brokers Payable` | Canonical |
| Test `2220 Marketer Commissions Payable` | `2220 Marketer Commissions Payable` | Canonical |
| Test `2410 Owner/Client Funds` | `2410 Owner/Client Funds Payable` | Canonical |
| Test `4100 Brokerage Revenue` | `4100 Brokerage Revenue` | Canonical |
| Test `4300 Property Management Revenue` | `4300 Property Management Revenue` | Canonical |
| Test `4410 Consulting Revenue` | `4410 Real Estate Consulting Revenue` | Canonical |

---

# 13. Tested Canonical Examples

These examples exist to make account behavior unambiguous.

### Brokerage revenue accrued
`Dr 1200 Accounts Receivable`
`Cr 4100 Brokerage Revenue`

### Collection of prior AR
`Dr 1100 Main Bank`
`Cr 1200 Accounts Receivable`

### Deal-specific advertising
`Dr 5300 Other Direct Deal Costs`
`Cr 1100 Main Bank`

### General office marketing
`Dr 6300 General Marketing & Advertising`
`Cr 1100 Main Bank`

### Marketer commission accrued
`Dr 5100 Marketer Commissions Expense`
`Cr 2220 Marketer Commissions Payable`

### Marketer paid
`Dr 2220 Marketer Commissions Payable`
`Cr 1100 Main Bank`

### External broker commission accrued
`Dr 5200 External Broker Commissions Expense`
`Cr 2130 External Brokers Payable`

### External broker paid
`Dr 2130 External Brokers Payable`
`Cr 1100 Main Bank`

### Partner pays office expense personally
`Dr appropriate office expense`
`Cr 3110 Partner Current Account`

### Reimburse partner
`Dr 3110 Partner Current Account`
`Cr 1100 Main Bank`

### Personal partner drawing
`Dr 3200 Partner Drawings`
`Cr 1100 Main Bank`

### Computer/equipment purchase
`Dr 1410 Computers & Office Equipment`
`Cr 1100 Main Bank`

### Annual software prepaid
`Dr 1310 Prepaid Software & Subscriptions`
`Cr 1100 Main Bank`

### Periodic software expense
`Dr 6500 Software & Subscriptions Expense`
`Cr 1310 Prepaid Software & Subscriptions`

### Owner/client funds received
`Dr 1100 Main Bank`
`Cr 2410 Owner / Client Funds Payable`

### Owner/client funds remitted
`Dr 2410 Owner / Client Funds Payable`
`Cr 1100 Main Bank`

### Internal bank transfer
`Dr 1110 Additional Bank`
`Cr 1100 Main Bank`

### Bank fee
`Dr 6810 Bank Fees`
`Cr 1100 Main Bank`

### Property-management revenue accrued
`Dr 1200 Accounts Receivable`
`Cr 4300 Property Management Revenue`

### Real-estate consulting received
`Dr 1100 Main Bank`
`Cr 4410 Real Estate Consulting Revenue`

---

# 14. Version Rule

This file is:

`Mafawiz Canonical Chart of Accounts v1.0`

Any future account addition, deletion, renumbering, merger, or split must:
1. increment the version;
2. document the old account;
3. document the new account;
4. provide a migration rule;
5. never silently reinterpret historical transactions.
