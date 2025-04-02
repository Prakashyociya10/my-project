frappe.query_reports["Feedback Analysis Report"] = {
    filters: [
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            reqd: 1
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
            reqd: 1
        },
        {
            fieldname: "customer",
            label: __("Customer"),
            fieldtype: "Link",
            options: "Customer"
        },
        {
            fieldname: "customer_group",
            label: __("Customer Group"),
            fieldtype: "Link",
            options: "Customer Group"
        }
    ],

    // Optional: Enable chart rendering
    formatter: function(value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (column.fieldname === "avg_rating" && value) {
            const rating = parseFloat(value);
            let color = "gray";

            if (rating >= 4) color = "green";
            else if (rating >= 2) color = "orange";
            else color = "red";

            return `<span style="color:${color}; font-weight: bold;">${value}</span>`;
        }

        return value;
    },

    // Optional: Add chart
    onload: function(report) {
        report.page.set_title("📊 Feedback Analysis Report");
    },

    get_chart_data: function(columns, data) {
        return {
            data: {
                labels: data.map(d => d.event),
                datasets: [
                    {
                        name: "Average Rating",
                        values: data.map(d => d.avg_rating)
                    }
                ]
            },
            type: 'bar'
        };
    }
};
