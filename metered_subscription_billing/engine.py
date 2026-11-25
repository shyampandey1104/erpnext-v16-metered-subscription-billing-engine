"""ERPNext v16 Metered Subscription & Usage-Based Billing Engine."""
from typing import Dict, Any, List

class MeteredBillingEngine:
    def __init__(self, currency: str = "USD"):
        self.currency = currency
        self.usage_ledger: Dict[str, float] = {}

    def record_usage_event(self, customer_id: str, metric_name: str, units: float):
        key = f"{customer_id}:{metric_name}"
        self.usage_ledger[key] = self.usage_ledger.get(key, 0.0) + float(units)

    def calculate_tiered_cost(self, total_units: float, tier_slabs: List[Dict[str, Any]]) -> float:
        remaining = total_units
        total_cost = 0.0
        prev_limit = 0.0

        for slab in tier_slabs:
            slab_limit = slab["max"]
            rate = slab["rate"]
            slab_capacity = slab_limit - prev_limit

            if remaining <= 0:
                break

            consumed_in_slab = min(remaining, slab_capacity)
            total_cost += consumed_in_slab * rate
            remaining -= consumed_in_slab
            prev_limit = slab_limit

        return round(total_cost, 2)

    def generate_customer_invoice_summary(self, customer_id: str, base_subscription_fee: float, api_calls_slab: List[Dict[str, Any]]) -> Dict[str, Any]:
        api_units = self.usage_ledger.get(f"{customer_id}:api_calls", 0.0)
        usage_fee = self.calculate_tiered_cost(api_units, api_calls_slab)
        subtotal = round(base_subscription_fee + usage_fee, 2)

        return {
            "customer_id": customer_id,
            "base_subscription_fee": base_subscription_fee,
            "metered_units_consumed": api_units,
            "metered_usage_fee": usage_fee,
            "total_invoice_amount": subtotal,
            "currency": self.currency,
            "billing_status": "READY_FOR_ERPNEXT_SALES_INVOICE"
        }
