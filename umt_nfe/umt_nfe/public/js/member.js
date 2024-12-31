frappe.ui.form.on('Member', {
    refresh: function(frm) {
        // Add custom buttons
        if(frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Create Membership Card'), function() {
                frappe.new_doc('Membership Card', {
                    member: frm.doc.name
                });
            });
        }
        
        // Add dashboard information
        frm.set_query('subject', function() {
            let subjects = [];
            if(frm.doc.profession === 'Primary Teaching') {
                subjects = ['Arabic', 'French'];
            } else if(frm.doc.profession === 'Middle School Teaching') {
                subjects = ['Arabic', 'Social Studies', 'French', 'Mathematics', 
                           'Scientific Activities', 'Islamic Education', 'Art Education'];
            } else if(frm.doc.profession === 'High School Teaching') {
                subjects = ['Mathematics', 'Physics Chemistry', 'Earth Science', 
                           'Computer Science', 'Arabic', 'French', 'English',
                           'Social Studies and Geography', 'Islamic Education', 'Philosophy'];
            }
            return {
                filters: {
                    'name': ['in', subjects]
                }
            };
        });
    },
    
    profession: function(frm) {
        // Clear subject when profession changes
        frm.set_value('subject', '');
    },
    
    role: function(frm) {
        // Clear role type when role changes
        if(frm.doc.role !== 'Educational Administration') {
            frm.set_value('role_type', '');
        }
    }
});
