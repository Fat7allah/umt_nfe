import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate

class Income(Document):
    def validate(self):
        self.validate_amount()
        self.validate_date()
        
    def validate_amount(self):
        """Ensure amount is positive"""
        if self.amount <= 0:
            frappe.throw(_("Amount must be greater than zero"))
            
    def validate_date(self):
        """Validate income date"""
        if self.date and getdate(self.date) > getdate():
            frappe.throw(_("Income date cannot be in the future"))
            
    def before_save(self):
        self.update_branch_total()
        
    def update_branch_total(self):
        """Update branch total income if branch is specified"""
        if self.branch:
            total_income = frappe.db.sql("""
                SELECT SUM(amount) 
                FROM `tabIncome`
                WHERE branch = %s
                AND name != %s
            """, (self.branch, self.name or ""))[0][0] or 0
            
            total_income += self.amount
            frappe.db.set_value("Branch", self.branch, "total_income", total_income)
            
    def on_trash(self):
        """Update branch total when income is deleted"""
        if self.branch:
            total_income = frappe.db.sql("""
                SELECT SUM(amount) 
                FROM `tabIncome`
                WHERE branch = %s
                AND name != %s
            """, (self.branch, self.name))[0][0] or 0
            
            frappe.db.set_value("Branch", self.branch, "total_income", total_income)
