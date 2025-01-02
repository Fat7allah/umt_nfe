import frappe
from frappe import _

no_cache = True

def get_context(context):
    """Prepare the context for the members portal page"""
    
    # Redirect to login if user is not authenticated
    if frappe.session.user == 'Guest':
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

@frappe.whitelist()
def delete_member(name):
    """Delete a member if user has permissions"""
    try:
        # Check if user has permission to delete
        if not frappe.has_permission('Member', 'delete'):
            frappe.throw(_("You don't have permission to delete members"))
            
        frappe.delete_doc('Member', name)
        frappe.db.commit()
        
        return {
            'status': 'success',
            'message': _('Member deleted successfully')
        }
        
    except Exception as e:
        frappe.log_error(f'Error deleting member: {str(e)}')
        return {
            'status': 'error',
            'message': _('Error deleting member: {0}').format(str(e))
        }
