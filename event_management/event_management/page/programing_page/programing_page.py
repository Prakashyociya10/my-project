import frappe


@frappe.whitelist()
def get_all_items():
    return frappe.get_all("Item", fields=["name","item_group","item_code",""])
