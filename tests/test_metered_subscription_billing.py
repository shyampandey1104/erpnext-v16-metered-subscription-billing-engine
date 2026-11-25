import unittest
from metered_subscription_billing.engine import MeteredBillingEngine

class TestMeteredBillingEngine(unittest.TestCase):
    def setUp(self):
        self.engine = MeteredBillingEngine("USD")

    def test_graduated_metered_billing(self):
        customer = "CUST-SAAS-001"
        self.engine.record_usage_event(customer, "api_calls", 1500)
        self.engine.record_usage_event(customer, "api_calls", 1500)

        tiers = [
            {"max": 1000, "rate": 0.10},
            {"max": 5000, "rate": 0.05},
            {"max": float("inf"), "rate": 0.02}
        ]

        summary = self.engine.generate_customer_invoice_summary(customer, base_subscription_fee=299.0, api_calls_slab=tiers)
        self.assertEqual(summary["metered_units_consumed"], 3000.0)
        self.assertEqual(summary["metered_usage_fee"], 200.0)
        self.assertEqual(summary["total_invoice_amount"], 499.0)
        self.assertEqual(summary["billing_status"], "READY_FOR_ERPNEXT_SALES_INVOICE")

if __name__ == "__main__":
    unittest.main()
