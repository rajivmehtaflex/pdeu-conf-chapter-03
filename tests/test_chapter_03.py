import json
import audit_agent


def test_query_ledger_returns_paid_gujarat_invoice():
    rows = json.loads(audit_agent.query_ledger("select Invoice_ID, Vendor_ID, Amount, Status from Invoices where Vendor_ID = 'VEN-1000'"))
    assert rows == [{"Invoice_ID": "INV-2000", "Vendor_ID": "VEN-1000", "Amount": 500000.0, "Status": "Paid"}]


def test_check_delivery_log_finds_fourteen_day_late_record():
    rows = json.loads(audit_agent.check_delivery_log("VEN-1000"))
    assert any(row["days_late"] == 14 for row in rows)


def test_build_discrepancy_summary_calculates_penalty():
    report = audit_agent.build_discrepancy_summary("Gujarat Steel Corp")
    assert report["vendor_id"] == "VEN-1000"
    assert report["invoice_amount"] == 500000.0
    assert report["days_late"] == 14
    assert report["penalty_amount_inr"] == 25000.0
