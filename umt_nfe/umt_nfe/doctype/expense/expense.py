import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate

class Expense(Document):
    def validate(self):
        self.validate_amount()
        self.validate_date()
        self.check_budget()
        
    def validate_amount(self):
        """Ensure amount is positive"""
        if self.amount <= 0:
            frappe.throw(_("Amount must be greater than zero"))
            
    def validate_date(self):
        """Validate expense date"""
        if self.date and getdate(self.date) > getdate():
            frappe.throw(_("Expense date cannot be in the future"))
            
    def check_budget(self):
        """Check if expense exceeds available budget"""
        fiscal_year = self.get_fiscal_year()
        
        total_income = frappe.db.sql("""
            SELECT SUM(amount)
            FROM `tabIncome`
            WHERE YEAR(date) = %s
        """, fiscal_year)[0][0] or 0
        
        total_expenses = frappe.db.sql("""
            SELECT SUM(amount)
            FROM `tabExpense`
            WHERE YEAR(date) = %s
            AND name != %s
        """, (fiscal_year, self.name or ""))[0][0] or 0
        
        available_budget = total_income - total_expenses
        
        if self.amount > available_budget:
            frappe.throw(_("Expense amount exceeds available budget for fiscal year {0}").format(fiscal_year))
            
    def get_fiscal_year(self):
        """Get fiscal year from expense date"""
        return getdate(self.date).year
