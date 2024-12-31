import frappe

def get_context(context):
    context.title = "Mutual Structures"
    
    # Get list of mutual structures
    context.mutual_structures = frappe.get_list(
        "Mutual Structure",
        fields=["name", "location", "contact_person", "phone"],
        order_by="creation desc"
    )
    
    # Add permissions context
    context.can_create = frappe.has_permission("Mutual Structure", "create")
    context.can_read = frappe.has_permission("Mutual Structure", "read")
