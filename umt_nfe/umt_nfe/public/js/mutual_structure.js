frappe.ui.form.on('Mutual Structure', {
    refresh: function(frm) {
        // Set filters for member selection
        frm.set_query('member', function() {
            return {
                filters: {
                    'is_active': 1
                }
            };
        });
        
        // Add dashboard information
        if(frm.doc.structure_type) {
            frappe.db.count('Mutual Structure', {
                filters: {
                    'structure_type': frm.doc.structure_type
                }
            }).then(count => {
                let limits = {
                    'Executive Office': 10,
                    'Administrative Council': 50,
                    'General Assembly': 260,
                    'Control Committee': 5,
                    'Outgoing Third': 86
                };
                
                frm.dashboard.add_indicator(
                    `Members: ${count}/${limits[frm.doc.structure_type]}`,
                    count >= limits[frm.doc.structure_type] ? 'red' : 'green'
                );
            });
        }
    },
    
    structure_type: function(frm) {
        // Reset dependent fields
        frm.set_value('position', '');
        frm.set_value('position_type', '');
        
        // Show/hide fields based on structure type
        if(frm.doc.structure_type === 'Executive Office') {
            frm.set_df_property('position', 'reqd', 1);
            frm.set_df_property('position', 'options',
                'President\nDeputy\nGeneral Secretary\nTreasurer\nAdvisor');
        } else {
            frm.set_df_property('position', 'reqd', 0);
            frm.set_value('position', '');
        }
    },
    
    position: function(frm) {
        // Reset position type
        frm.set_value('position_type', '');
        
        // Show/hide position type based on position
        if(['President', 'General Secretary', 'Treasurer'].includes(frm.doc.position)) {
            frm.set_df_property('position_type', 'reqd', 1);
        } else {
            frm.set_df_property('position_type', 'reqd', 0);
        }
    }
});
