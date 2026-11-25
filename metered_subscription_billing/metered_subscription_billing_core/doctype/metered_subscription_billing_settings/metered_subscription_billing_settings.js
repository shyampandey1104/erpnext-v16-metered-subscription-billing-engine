frappe.ui.form.on("ERPNext v16 Metered Subscription & Usage-Based Billing Settings", {
    refresh: function(frm) {
        frm.add_custom_button(__("Test v16 Connection"), function() {
            frm.call({ doc: frm.doc, method: "test_connection" });
        });
    }
});
