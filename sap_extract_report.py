import sys
import platform
from datetime import datetime

print("=" * 60)
print("  SAP Report Extraction (simulated)")
print("=" * 60)
print()

if len(sys.argv) < 4:
    print(f"ERROR: expected 3 arguments, got {len(sys.argv) - 1}")
    print("Usage: sap_extract_report.py <company_code> <fiscal_year> <report_type>")
    sys.exit(1)

company_code = sys.argv[1]
fiscal_year = sys.argv[2]
report_type = sys.argv[3]

print(f"Connecting to SAP...")
print(f"  System:        ECC 6.0 (simulated)")
print(f"  Host:          {platform.node()}")
print(f"  Run timestamp: {datetime.now().isoformat(timespec="seconds")}")
print()
print(f"Extraction parameters:")
print(f"  Company code:  {company_code}")
print(f"  Fiscal year:   {fiscal_year}")
print(f"  Report type:   {report_type}")
print()

# Simulated SAP response. In real life this would be an RFC call (pyrfc) or
# an OData read against /sap/opu/odata/... using sapnwrfc / requests.
reports = {
    "balance_sheet":    {"total_assets": 12_450_000, "total_liabilities": 7_200_000, "equity": 5_250_000},
    "income_statement": {"revenue": 8_900_000, "expenses": 6_100_000, "net_income": 2_800_000},
    "cash_flow":        {"operating": 1_500_000, "investing": -800_000, "financing": -200_000},
}

if report_type not in reports:
    print(f"FAIL: unknown report_type {report_type!r}")
    print(f"  Valid types: {sorted(reports.keys())}")
    sys.exit(2)

print(f"Report rows:")
print(f"  {"Account":<22} {"Amount (USD)":>18}")
print(f"  {"-" * 22} {"-" * 18}")
for k, v in reports[report_type].items():
    print(f"  {k:<22} {v:>18,}")
print()
print("Status: SUCCESS")
