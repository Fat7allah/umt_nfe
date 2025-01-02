import frappe

def get_context(context):
    if not frappe.session.user or frappe.session.user == 'Guest':
        frappe.local.flags.redirect_location = '/login'
        raise frappe.Redirect
        
    context.show_sidebar = True
    
    # Get counts for different doctypes
    context.member_count = frappe.db.count('Member')
    context.income_count = frappe.db.count('Income')
    context.expense_count = frappe.db.count('Expense')
    context.federation_count = frappe.db.count('Federation Structure')
    context.mutual_count = frappe.db.count('Mutual Structure')
