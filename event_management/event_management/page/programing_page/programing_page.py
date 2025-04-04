import frappe

@frappe.whitelist()
def get_all_items():
    return frappe.get_all(
        "Item",
        fields=["name",  "item_name",  "item_group","item_code","disabled"],
        limit_page_length=100
    )