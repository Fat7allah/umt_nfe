import frappe
from frappe.utils import flt

def get_context(context):
    context.title = "Expenses"
    
    # Get list of expenses
    context.expenses = frappe.get_list(
        "Expense",
        fields=["name", "title", "amount", "date", "category"],
        order_by="date desc"
    )
    
    # Calculate total expenses
    context.total_expenses = sum(flt(expense.amount) for expense in context.expenses)
    
    # Add permissions context
    context.can_create = frappe.has_permission("Expense", "create")
    context.can_read = frappe.has_permission("Expense", "read")
