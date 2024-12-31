import frappe
from frappe import _
from frappe.model.document import Document

class MutualStructure(Document):
    def validate(self):
        self.validate_member()
        self.validate_structure_limits()
        self.validate_positions()
        
    def validate_member(self):
        """Ensure member is active"""
        is_active = frappe.db.get_value("Member", self.member, "is_active")
        if not is_active:
            frappe.throw(_("Member must be active to be part of Mutual Structure"))
            
    def validate_structure_limits(self):
        """Validate member limits for different structure types"""
        limits = {
            "Executive Office": 10,
            "Administrative Council": 50,
            "General Assembly": 260,
            "Control Committee": 5,
            "Outgoing Third": 86
        }
        
        if self.structure_type in limits:
            total_members = frappe.db.count("Mutual Structure", 
                {"structure_type": self.structure_type})
            if total_members >= limits[self.structure_type] and not self.name:
                frappe.throw(_("{0} cannot have more than {1} members").format(
                    self.structure_type, limits[self.structure_type]))
                    
    def validate_positions(self):
        """Validate position requirements for executive office"""
        if self.structure_type == "Executive Office":
            if not self.position:
                frappe.throw(_("Position is mandatory for Executive Office members"))
                
            if self.position in ["President", "General Secretary", "Treasurer"]:
                existing = frappe.db.exists("Mutual Structure", {
                    "structure_type": "Executive Office",
                    "position": self.position,
                    "position_type": "Main",
                    "name": ("!=", self.name)
                })
                if existing:
                    frappe.throw(_("There can only be one {0}").format(self.position))
