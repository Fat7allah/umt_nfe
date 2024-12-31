import frappe

def get_context(context):
    context.title = "Membership Cards"
    
    # Get list of membership cards
    context.membership_cards = frappe.get_list(
        "Membership Card",
        fields=["name", "member", "member_name", "issue_date", "status"],
        order_by="creation desc"
    )
    
    # Add permissions context
    context.can_create = frappe.has_permission("Membership Card", "create")
    context.can_read = frappe.has_permission("Membership Card", "read")
