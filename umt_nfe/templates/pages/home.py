import frappe

def get_context(context):
    context.title = "UMT NFE Portal"
    
    # Get counts for each doctype
    context.stats = {
        'members': frappe.db.count('Member'),
        'membership_cards': frappe.db.count('Membership Card'),
        'federation_structures': frappe.db.count('Federation Structure'),
        'mutual_structures': frappe.db.count('Mutual Structure'),
        'incomes': frappe.db.count('Income'),
        'expenses': frappe.db.count('Expense')
    }
    
    # Add permissions context
    context.permissions = {
        'Member': frappe.has_permission('Member', 'read'),
        'Membership Card': frappe.has_permission('Membership Card', 'read'),
        'Federation Structure': frappe.has_permission('Federation Structure', 'read'),
        'Mutual Structure': frappe.has_permission('Mutual Structure', 'read'),
        'Income': frappe.has_permission('Income', 'read'),
        'Expense': frappe.has_permission('Expense', 'read')
    }
