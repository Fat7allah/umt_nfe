import frappe

def get_context(context):
    context.title = "Members"
    
    # Get list of members
    context.members = frappe.get_list(
        "Member",
        fields=["name", "full_name", "phone", "email"],
        order_by="creation desc"
    )
    
    # Add permissions context
    context.can_create = frappe.has_permission("Member", "create")
    context.can_read = frappe.has_permission("Member", "read")
