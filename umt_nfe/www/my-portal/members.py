import frappe
from frappe import _

def get_context(context):
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect

    context.show_sidebar = True
    
    # Get list of members with important fields
    context.members = frappe.get_all(
        'Member',
        fields=['name', 'full_name', 'email', 'phone', 'status'],
        order_by='full_name asc'
    )

    # Add breadcrumbs
    context.parents = [
        {"name": _("My Portal"), "route": "/my-portal"}
    ]
