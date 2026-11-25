// Frappe v16 Client Script for ERPNext v16 Metered Subscription & Usage-Based Billing Entry
frappe.ui.form.on("ERPNext v16 Metered Subscription & Usage-Based Billing Entry", {
    refresh: function(frm) {
        if (frm.doc.status === "Submitted") {
            frm.page.set_indicator(__("v16 Verified"), "green");
        }
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__("View v16 Audit Trail"), function() {
                frappe.set_route("List", "ERPNext v16 Metered Subscription & Usage-Based Billing Audit Log");
            }, __("v16 Actions"));
        }
    }
});
