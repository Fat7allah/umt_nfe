import frappe
from frappe import _
from frappe.utils import cstr

no_cache = True

def get_context(context):
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect

    context.show_sidebar = True
    
    # Get member details if editing
    member_name = frappe.form_dict.get('name')
    if member_name:
        context.doc = frappe.get_doc('Member', member_name)
        context.title = _("Edit Member: {0}").format(context.doc.full_name)
    else:
        context.doc = None
        context.title = _("New Member")
    
    # Add breadcrumbs
    context.parents = [
        {"name": _("My Portal"), "route": "/my-portal"},
        {"name": _("Members"), "route": "/my-portal/members"}
    ]

@frappe.whitelist()
def save_member(data):
    """Save member data from the portal form"""
    try:
        if not isinstance(data, dict):
            data = frappe.parse_json(data)
            
        if data.get('name'):
            # Update existing member
            doc = frappe.get_doc('Member', data['name'])
            doc.update(data)
            doc.save()
        else:
            # Create new member
            doc = frappe.get_doc({
                'doctype': 'Member',
                **data
            })
            doc.insert()
            
        return {'success': True, 'message': _('Member saved successfully')}
        
    except Exception as e:
        frappe.log_error('Member Save Error', str(e))
        frappe.throw(_('Error saving member: {0}').format(str(e)))

@frappe.whitelist()
def delete_member(member_name):
    """Delete a member"""
    try:
        frappe.delete_doc('Member', member_name)
        return {'success': True, 'message': _('Member deleted successfully')}
    except Exception as e:
        frappe.log_error('Member Delete Error', str(e))
        frappe.throw(_('Error deleting member: {0}').format(str(e)))
