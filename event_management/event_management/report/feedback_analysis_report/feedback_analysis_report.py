import frappe

def execute(filters=None):
    columns = [
        {"label": "Event", "fieldname": "event", "fieldtype": "Link", "options": "Event", "width": 160},
        {"label": "Attendee", "fieldname": "attendee", "fieldtype": "Link", "options": "Events Attendee", "width": 160},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Data", "width": 140},
        {"label": "Rating", "fieldname": "rating", "fieldtype": "Int", "width": 80},
        {"label": "Submitted On", "fieldname": "submitted_on", "fieldtype": "Datetime", "width": 180},
        {"label": "Comments", "fieldname": "comments", "fieldtype": "Data", "width": 300},
    ]

    conditions = ""
    if filters.get("from_date"):
        conditions += f" AND fb.submitted_on >= '{filters['from_date']}'"
    if filters.get("to_date"):
        conditions += f" AND fb.submitted_on <= '{filters['to_date']}'"

    results = frappe.db.sql(f"""
        SELECT
            fb.event,
            fb.attendee,
            fb.customer,
            fb.rating,
            fb.submitted_on,
            fb.comments
        FROM `tabFeedback` fb
        WHERE 1=1 {conditions}
        ORDER BY fb.submitted_on DESC
    """, as_dict=True)

    return columns, results
