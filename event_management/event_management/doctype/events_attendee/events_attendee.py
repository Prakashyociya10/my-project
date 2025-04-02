

import frappe
from frappe.model.document import Document


class EventsAttendee(Document):
	pass


def execute(filters=None):
    columns = [
        {"label": "Event", "fieldname": "event", "fieldtype": "Link", "options": "Event", "width": 150},
        {"label": "Attendee Name", "fieldname": "attendee_name", "fieldtype": "Data", "width": 150},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data", "width": 200},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Data", "width": 130},
        {"label": "Status", "fieldname": "status", "fieldtype": "Select", "width": 100},
        {"label": "Check In Time", "fieldname": "check_in_time", "fieldtype": "Datetime", "width": 180},
        {"label": "Event Date", "fieldname": "event_date", "fieldtype": "Date", "width": 120},
    ]

    conditions = ""
    if filters.get("event"):
        conditions += f" AND ea.event = '{filters['event']}'"
    if filters.get("status"):
        conditions += f" AND ea.status = '{filters['status']}'"

    data = frappe.db.sql(f"""
        SELECT
            ea.event,
            ea.attendee_name,
            ea.email,
            ea.phone,
            ea.status,
            ea.check_in_time,
            ea.event_date
        FROM `tabEvents Attendee` ea
        WHERE 1=1 {conditions}
        ORDER BY ea.check_in_time DESC
    """, as_dict=True)

    return columns, data
