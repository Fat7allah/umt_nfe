import frappe
from frappe import _
from frappe.model.document import Document

class FederationStructure(Document):
    def validate(self):
        self.validate_member()
        self.validate_position_limits()
        self.validate_structure_type()
        
    def validate_member(self):
        """Ensure member is active"""
        is_active = frappe.db.get_value("Member", self.member, "is_active")
        if not is_active:
            frappe.throw(_("Member must be active to be part of Federation Structure"))
            
    def validate_position_limits(self):
        """Validate position limits based on structure type"""
        if self.structure_type == "Executive Office":
            self.validate_executive_office()
        elif self.structure_type in ["Regional Office", "Provincial Office", "Local Office"]:
            self.validate_office_positions()
            
    def validate_executive_office(self):
        """Validate executive office position limits"""
        # Check total members limit (31)
        total_members = frappe.db.count("Federation Structure", 
            {"structure_type": "Executive Office"})
        if total_members >= 31 and not self.name:
            frappe.throw(_("Executive Office cannot have more than 31 members"))
            
        # Validate unique positions
        if self.position in ["National Secretary", "General Secretary", "Treasurer"]:
            existing = frappe.db.exists("Federation Structure", {
                "structure_type": "Executive Office",
                "position": self.position,
                "position_type": "Main",
                "name": ("!=", self.name)
            })
            if existing:
                frappe.throw(_("There can only be one {0}").format(self.position))
                
    def validate_office_positions(self):
        """Validate regional/provincial/local office positions"""
        if self.office_type:
            existing = frappe.db.exists("Federation Structure", {
                "structure_type": self.structure_type,
                "office_type": self.office_type,
                "position": self.position,
                "position_type": "Main",
                "name": ("!=", self.name)
            })
            if existing and self.position_type == "Main":
                frappe.throw(_("There can only be one {0} for {1} {2}").format(
                    self.position, self.office_type, self.structure_type))
                    
    def validate_structure_type(self):
        """Validate structure type specific requirements"""
        if self.structure_type in ["Regional Office", "Provincial Office", "Local Office"]:
            if not self.office_type:
                frappe.throw(_("Office Type is mandatory for {0}").format(self.structure_type))
