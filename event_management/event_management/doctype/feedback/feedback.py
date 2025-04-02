# Copyright (c) 2025, prakash and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Feedback(Document):
	pass
# feedback_analysis_report.py

def execute(filters=None):
    columns = [
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Data", "width": 180},
        {"label": "Event", "fieldname": "event", "fieldtype": "Data", "width": 180},
        {"label": "Rating", "fieldname": "rating", "fieldtype": "Int", "width": 100},
    ]

    data = [
        {"customer": "Customer A", "event": "TechCon 2025", "rating": 5},
        {"customer": "Customer B", "event": "ERPNext Workshop", "rating": 4},
    ]

    return columns, data
