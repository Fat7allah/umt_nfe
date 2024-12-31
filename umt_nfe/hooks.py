app_name = "umt_nfe"
app_title = "UMT NFE"
app_publisher = "Codeium"
app_description = "National Federation of Education Management System"
app_email = "contact@codeium.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/umt_nfe/css/umt_nfe.css"
# app_include_js = "/assets/umt_nfe/js/umt_nfe.js"

# include js, css files in header of web template
# web_include_css = "/assets/umt_nfe/css/umt_nfe_web.css"
# web_include_js = "/assets/umt_nfe/js/umt_nfe_web.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "umt_nfe/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Member": "public/js/member.js",
    "Membership Card": "public/js/membership_card.js",
    "Federation Structure": "public/js/federation_structure.js",
    "Mutual Structure": "public/js/mutual_structure.js",
    "Income": "public/js/income.js",
    "Expense": "public/js/expense.js"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Desk Notifications
# ---------------
notification_config = "umt_nfe.notifications.get_notification_config"

# Document Events
# ---------------
doc_events = {
    "Member": {
        "validate": "umt_nfe.umt_nfe.doctype.member.member.validate",
        "before_save": "umt_nfe.umt_nfe.doctype.member.member.before_save"
    },
    "Membership Card": {
        "validate": "umt_nfe.umt_nfe.doctype.membership_card.membership_card.validate",
        "before_save": "umt_nfe.umt_nfe.doctype.membership_card.membership_card.before_save"
    },
    "Federation Structure": {
        "validate": "umt_nfe.umt_nfe.doctype.federation_structure.federation_structure.validate"
    },
    "Mutual Structure": {
        "validate": "umt_nfe.umt_nfe.doctype.mutual_structure.mutual_structure.validate"
    },
    "Income": {
        "validate": "umt_nfe.umt_nfe.doctype.income.income.validate",
        "before_save": "umt_nfe.umt_nfe.doctype.income.income.before_save",
        "on_trash": "umt_nfe.umt_nfe.doctype.income.income.on_trash"
    },
    "Expense": {
        "validate": "umt_nfe.umt_nfe.doctype.expense.expense.validate"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "umt_nfe.tasks.daily"
    ],
    "monthly": [
        "umt_nfe.tasks.monthly"
    ]
}

# Testing
# -------
# before_tests = "umt_nfe.install.before_tests"

# Overriding Methods
# ---------------
#
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "umt_nfe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#     "Task": "umt_nfe.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["umt_nfe.utils.before_request"]
# after_request = ["umt_nfe.utils.after_request"]

# Job Events
# ----------
# before_job = ["umt_nfe.utils.before_job"]
# after_job = ["umt_nfe.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#     {
#         "doctype": "{doctype_1}",
#         "filter_by": "{filter_by}",
#         "redact_fields": ["{field_1}", "{field_2}"],
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_2}",
#         "filter_by": "{filter_by}",
#         "partial": 1,
#     },
#     {
#         "doctype": "{doctype_3}",
#         "strict": False,
#     }
# ]
