frappe.ui.form.on('Income', {
    refresh: function(frm) {
        // Add dashboard information
        frm.dashboard.add_transactions({
            'items': [
                {
                    'label': 'Related',
                    'items': ['Membership Card']
                }
            ]
        });
        
        // Show fiscal year summary
        let fiscal_year = frappe.datetime.get_today().split('-')[0];
        frappe.db.get_list('Income', {
            filters: {
                'date': ['like', `${fiscal_year}%`]
            },
            fields: ['sum(amount) as total']
        }).then(r => {
            let total = r[0].total || 0;
            frm.dashboard.add_indicator(
                `Total Income (${fiscal_year}): ${format_currency(total)}`,
                'blue'
            );
        });
    },
    
    income_type: function(frm) {
        // Clear name/description when type changes
        frm.set_value('name_description', '');
        
        // Set filters for branch based on income type
        if(frm.doc.income_type === 'Membership Card') {
            frm.set_query('branch', function() {
                return {
                    filters: {
                        'is_group': 0
                    }
                };
            });
        }
    }
});
