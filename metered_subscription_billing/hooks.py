# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "metered_subscription_billing"
app_title = "ERPNext v16 Metered Subscription & Usage-Based Billing"
app_publisher = "Shyamkumar Pandey"
app_description = "ERPNext v16 high-throughput usage-based billing engine supporting API event ingestion, tiered bandwidth/storage meters, graduated pricing models, and automated recurring billing invoices."
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"
required_frappe_version = ">=16.0.0"

# Includes in <head>
app_include_css = "/assets/metered_subscription_billing/css/metered_subscription_billing.bundle.css"
app_include_js = "/assets/metered_subscription_billing/js/metered_subscription_billing.bundle.js"

# Document Events
doc_events = {
    "ERPNext v16 Metered Subscription & Usage-Based Billing Entry": {
        "validate": "metered_subscription_billing.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "metered_subscription_billing.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
scheduler_events = {
    "hourly": [
        "metered_subscription_billing.tasks.hourly_sync"
    ],
    "daily": [
        "metered_subscription_billing.tasks.daily_reconciliation"
    ],
    "weekly": [
        "metered_subscription_billing.tasks.weekly_digest"
    ]
}
