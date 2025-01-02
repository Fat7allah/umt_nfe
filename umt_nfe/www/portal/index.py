import frappe
from frappe import _

no_cache = True

def get_context(context):
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect

    context.stats = {
        'member_count': frappe.db.count('Member'),
        'federation_count': frappe.db.count('Federation Structure'),
        'mutual_count': frappe.db.count('Mutual Structure'),
        'income_count': frappe.db.count('Income'),
        'expense_count': frappe.db.count('Expense'),
        'card_count': frappe.db.count('Membership Card')
    }

    context.title = _("UMT NFE Portal")
    context.parents = [
        {"name": _("Home"), "route": "/"}
    ]
