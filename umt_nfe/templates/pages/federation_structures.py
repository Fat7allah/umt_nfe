import frappe

def get_context(context):
    context.title = "Federation Structures"
    
    # Get list of federation structures
    context.federation_structures = frappe.get_list(
        "Federation Structure",
        fields=["name", "location", "contact_person", "phone"],
        order_by="creation desc"
    )
    
    # Add permissions context
    context.can_create = frappe.has_permission("Federation Structure", "create")
    context.can_read = frappe.has_permission("Federation Structure", "read")
