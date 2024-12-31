frappe.ui.form.on('Membership Card', {
    refresh: function(frm) {
        // Add custom buttons
        if(frm.doc.docstatus === 1 && frm.doc.status === 'Unpaid') {
            frm.add_custom_button(__('Record Payment'), function() {
                frm.set_value('status', 'Paid');
                frm.save();
            });
        }
    },
    
    membership_date: function(frm) {
        // Automatically set expiry date to one year after membership date
        if(frm.doc.membership_date) {
            let expiry = frappe.datetime.add_days(frm.doc.membership_date, 365);
            frm.set_value('expiry_date', expiry);
        }
    },
    
    member: function(frm) {
        // Fetch member details
        if(frm.doc.member) {
            frappe.db.get_value('Member', frm.doc.member, ['full_name', 'phone', 'email'])
                .then(r => {
                    let values = r.message;
                    frm.set_df_property('member_info', 'description',
                        `Name: ${values.full_name}<br>
                         Phone: ${values.phone}<br>
                         Email: ${values.email}`);
                });
        }
    }
});
