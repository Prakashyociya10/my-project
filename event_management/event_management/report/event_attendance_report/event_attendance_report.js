frappe.query_reports["Event Attendee Report"] = {
    filters: [
        {
            fieldname: "event",
            label: __("Event"),
            fieldtype: "Link",
            options: "Event"
        },
        {
            fieldname: "status",
            label: __("Status"),
            fieldtype: "Select",
            options: ["", "Registered", "Checked In", "Cancelled"]
        }
    ]
};

