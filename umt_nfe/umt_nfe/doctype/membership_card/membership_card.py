import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, date_diff

class MembershipCard(Document):
    def validate(self):
        self.validate_dates()
        self.validate_card_number()
        
    def validate_dates(self):
        if self.membership_date and self.expiry_date:
            if getdate(self.expiry_date) <= getdate(self.membership_date):
                frappe.throw(_("Expiry Date must be after Membership Date"))
                
            # Check if membership period is valid (typically 1 year)
            days_diff = date_diff(self.expiry_date, self.membership_date)
            if days_diff > 366:  # Account for leap years
                frappe.throw(_("Membership period cannot exceed one year"))
                
    def validate_card_number(self):
        if self.card_number:
            # Check if card number already exists
            existing = frappe.db.get_value("Membership Card", 
                {"card_number": self.card_number, "name": ("!=", self.name)}, "name")
            if existing:
                frappe.throw(_("Card Number {0} already exists").format(self.card_number))
                
    def before_save(self):
        self.update_member_status()
        
    def update_member_status(self):
        """Update member's active status based on card payment status"""
        if self.status == "Paid":
            frappe.db.set_value("Member", self.member, "is_active", 1)
        else:
            # Check if member has any other active paid cards
            active_cards = frappe.get_all("Membership Card",
                filters={
                    "member": self.member,
                    "status": "Paid",
                    "name": ("!=", self.name)
                })
            if not active_cards:
                frappe.db.set_value("Member", self.member, "is_active", 0)
