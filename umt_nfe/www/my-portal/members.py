import frappe
from frappe import _

no_cache = True

def get_context(context):
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.no_cache = True
    
    # Get list of members with important fields
    context.members = frappe.get_list(
        'Member',
        fields=['name', 'full_name', 'email', 'phone', 'status'],
        order_by='full_name asc'
    )
    
    # Add page metadata
    context.title = _("Members Directory")
    context.parents = [
        {"name": _("Home"), "route": "/"}
    ]
