import frappe
from frappe import _
from frappe.model.document import Document

class Member(Document):
    def validate(self):
        self.validate_email()
        self.validate_phone()
        self.validate_subject()
        
    def validate_email(self):
        if self.email and not frappe.utils.validate_email_address(self.email):
            frappe.throw(_("Please enter a valid email address"))
            
    def validate_phone(self):
        if self.phone and not self.phone.isdigit():
            frappe.throw(_("Phone number should contain only digits"))
            
    def validate_subject(self):
        if self.profession in ["Primary Teaching", "Middle School Teaching", "High School Teaching"] and not self.subject:
            frappe.throw(_("Subject is mandatory for teaching positions"))
            
    def before_save(self):
        self.set_full_title()
        
    def set_full_title(self):
        """Set the full title based on role and position"""
        if not self.full_name:
            return
            
        title_parts = [self.full_name]
        
        if self.role:
            title_parts.append(self.role)
            
        if self.role_type and self.role == "Educational Administration":
            title_parts.append(self.role_type)
            
        self.title = " - ".join(title_parts)

    def has_website_permission(doc, ptype, user, verbose=False):
        if not user:
            return False
        
        if "System Manager" in frappe.get_roles(user):
            return True
            
        return frappe.has_permission("Member", ptype, user=user)
