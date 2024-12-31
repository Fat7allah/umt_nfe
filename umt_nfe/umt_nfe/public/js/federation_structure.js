frappe.ui.form.on('Federation Structure', {
    refresh: function(frm) {
        // Set filters for member selection
        frm.set_query('member', function() {
            return {
                filters: {
                    'is_active': 1
                }
            };
        });
    },
    
    structure_type: function(frm) {
        // Reset dependent fields
        frm.set_value('position', '');
        frm.set_value('position_type', '');
        frm.set_value('office_type', '');
        
        // Show/hide fields based on structure type
        if(frm.doc.structure_type === 'Executive Office') {
            frm.set_df_property('position', 'options', 
                'National Secretary\nDeputy\nGeneral Secretary\nTreasurer\nAdvisor\nTask Officer');
        } else if(['Regional Office', 'Provincial Office', 'Local Office'].includes(frm.doc.structure_type)) {
            frm.set_df_property('position', 'options',
                'Secretary\nDeputy\nGeneral Secretary\nTreasurer\nAdvisor');
        }
    },
    
    position: function(frm) {
        // Reset position type
        frm.set_value('position_type', '');
        
        // Show/hide position type based on position
        if(['National Secretary', 'General Secretary', 'Treasurer'].includes(frm.doc.position)) {
            frm.set_df_property('position_type', 'reqd', 1);
        } else {
            frm.set_df_property('position_type', 'reqd', 0);
        }
    }
});
