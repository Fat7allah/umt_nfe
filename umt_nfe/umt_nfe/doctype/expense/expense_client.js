frappe.ui.form.on('Expense', {
    refresh: function(frm) {
        // Add dashboard information
        let fiscal_year = frappe.datetime.get_today().split('-')[0];
        
        // Get total income for fiscal year
        frappe.db.get_list('Income', {
            filters: {
                'date': ['like', `${fiscal_year}%`]
            },
            fields: ['sum(amount) as total']
        }).then(r => {
            let total_income = r[0].total || 0;
            
            // Get total expenses for fiscal year
            frappe.db.get_list('Expense', {
                filters: {
                    'date': ['like', `${fiscal_year}%`],
                    'name': ['!=', frm.doc.name || '']
                },
                fields: ['sum(amount) as total']
            }).then(e => {
                let total_expenses = e[0].total || 0;
                let available_budget = total_income - total_expenses;
                
                // Add indicators
                frm.dashboard.add_indicator(
                    `Total Income (${fiscal_year}): ${format_currency(total_income)}`,
                    'blue'
                );
                frm.dashboard.add_indicator(
                    `Total Expenses (${fiscal_year}): ${format_currency(total_expenses)}`,
                    'orange'
                );
                frm.dashboard.add_indicator(
                    `Available Budget: ${format_currency(available_budget)}`,
                    available_budget > 0 ? 'green' : 'red'
                );
            });
        });
    },
    
    amount: function(frm) {
        // Validate amount against available budget
        if(frm.doc.amount && frm.doc.date) {
            let fiscal_year = frm.doc.date.split('-')[0];
            
            frappe.db.get_list('Income', {
                filters: {
                    'date': ['like', `${fiscal_year}%`]
                },
                fields: ['sum(amount) as total']
            }).then(r => {
                let total_income = r[0].total || 0;
                
                frappe.db.get_list('Expense', {
                    filters: {
                        'date': ['like', `${fiscal_year}%`],
                        'name': ['!=', frm.doc.name || '']
                    },
                    fields: ['sum(amount) as total']
                }).then(e => {
                    let total_expenses = e[0].total || 0;
                    let available_budget = total_income - total_expenses;
                    
                    if(frm.doc.amount > available_budget) {
                        frappe.msgprint(__(`Warning: Expense amount exceeds available budget for fiscal year ${fiscal_year}`));
                    }
                });
            });
        }
    }
});
