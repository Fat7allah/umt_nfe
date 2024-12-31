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
web_include_css = "/assets/umt_nfe/css/umt_nfe_web.css"
web_include_js = "/assets/umt_nfe/js/umt_nfe_web.js"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"

# website user home page (by Role)
role_home_page = {
    "System Manager": "home",
    "Administrator": "home"
}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#   "methods": "umt_nfe.utils.jinja_methods",
#   "filters": "umt_nfe.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "umt_nfe.install.before_install"
# after_install = "umt_nfe.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "umt_nfe.uninstall.before_uninstall"
# after_uninstall = "umt_nfe.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "umt_nfe.utils.before_app_install"
# after_app_install = "umt_nfe.utils.after_app_install"

# Integration Cleanup
# ------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "umt_nfe.utils.before_app_uninstall"
# after_app_uninstall = "umt_nfe.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "umt_nfe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#   "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Portal Settings
has_website_permission = {
    "Member": "umt_nfe.umt_nfe.doctype.member.member.has_website_permission",
    "Membership Card": "umt_nfe.umt_nfe.doctype.membership_card.membership_card.has_website_permission",
    "Federation Structure": "umt_nfe.umt_nfe.doctype.federation_structure.federation_structure.has_website_permission",
    "Mutual Structure": "umt_nfe.umt_nfe.doctype.mutual_structure.mutual_structure.has_website_permission",
    "Income": "umt_nfe.umt_nfe.doctype.income.income.has_website_permission",
    "Expense": "umt_nfe.umt_nfe.doctype.expense.expense.has_website_permission"
}

website_route_rules = [
    {"from_route": "/members", "to_route": "Member"},
    {"from_route": "/membership-cards", "to_route": "Membership Card"},
    {"from_route": "/federation-structures", "to_route": "Federation Structure"},
    {"from_route": "/mutual-structures", "to_route": "Mutual Structure"},
    {"from_route": "/incomes", "to_route": "Income"},
    {"from_route": "/expenses", "to_route": "Expense"}
]

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#   "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

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
