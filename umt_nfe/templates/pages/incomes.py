import frappe
from frappe.utils import flt

def get_context(context):
    context.title = "Incomes"
    
    # Get list of incomes
    context.incomes = frappe.get_list(
        "Income",
        fields=["name", "title", "amount", "date", "category"],
        order_by="date desc"
    )
    
    # Calculate total income
    context.total_income = sum(flt(income.amount) for income in context.incomes)
    
    # Add permissions context
    context.can_create = frappe.has_permission("Income", "create")
    context.can_read = frappe.has_permission("Income", "read")
