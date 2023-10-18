from . import __version__ as app_version

app_name = "taxsparrow"
app_title = "Tax Sparrow"
app_publisher = "Sparrownova"
app_description = "Shopper Prime app to simplify compliance with Indian Rules and Regulations"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@sparrownova.com"
app_license = "GNU General Public License (v3)"
required_apps = ["frappe/shopperprime"]

before_install = "taxsparrow.patches.check_version_compatibility.execute"
after_install = "taxsparrow.install.after_install"
before_uninstall = "taxsparrow.uninstall.before_uninstall"

after_app_install = "taxsparrow.install.after_app_install"
before_app_uninstall = "taxsparrow.uninstall.before_app_uninstall"

before_migrate = "taxsparrow.patches.check_version_compatibility.execute"
after_migrate = "taxsparrow.audit_trail.setup.after_migrate"

before_tests = "taxsparrow.tests.before_tests"

boot_session = "taxsparrow.boot.set_bootinfo"

setup_wizard_requires = "assets/taxsparrow/js/setup_wizard.js"
setup_wizard_complete = "taxsparrow.gst_india.setup.setup_wizard_complete"
setup_wizard_stages = "taxsparrow.setup_wizard.get_setup_wizard_stages"

app_include_js = "taxsparrow.bundle.js"

doctype_js = {
    "Address": "gst_india/client_scripts/address.js",
    "Company": "gst_india/client_scripts/company.js",
    "Customer": "gst_india/client_scripts/customer.js",
    "Delivery Note": [
        "gst_india/client_scripts/e_waybill_actions.js",
        "gst_india/client_scripts/delivery_note.js",
    ],
    "Item": "gst_india/client_scripts/item.js",
    "Expense Claim": [
        "gst_india/client_scripts/journal_entry.js",
        "gst_india/client_scripts/expense_claim.js",
    ],
    "Journal Entry": "gst_india/client_scripts/journal_entry.js",
    "Payment Entry": "gst_india/client_scripts/payment_entry.js",
    "Purchase Invoice": [
        "gst_india/client_scripts/e_waybill_actions.js",
        "gst_india/client_scripts/purchase_invoice.js",
    ],
    "Sales Invoice": [
        "gst_india/client_scripts/e_invoice_actions.js",
        "gst_india/client_scripts/e_waybill_actions.js",
        "gst_india/client_scripts/sales_invoice.js",
    ],
    "Supplier": "gst_india/client_scripts/supplier.js",
    "Accounts Settings": "audit_trail/client_scripts/accounts_settings.js",
    "Customize Form": "audit_trail/client_scripts/customize_form.js",
}

doctype_list_js = {
    "Sales Invoice": [
        "gst_india/client_scripts/e_waybill_actions.js",
        "gst_india/client_scripts/sales_invoice_list.js",
    ]
}

doc_events = {
    "Address": {
        "validate": [
            "taxsparrow.gst_india.overrides.address.validate",
            "taxsparrow.gst_india.overrides.party.set_docs_with_previous_gstin",
        ],
    },
    "Company": {
        "on_trash": "taxsparrow.gst_india.overrides.company.delete_gst_settings_for_company",
        "on_update": [
            "taxsparrow.income_tax_india.overrides.company.make_company_fixtures",
            "taxsparrow.gst_india.overrides.company.make_company_fixtures",
        ],
        "validate": "taxsparrow.gst_india.overrides.party.validate_party",
    },
    "Customer": {
        "validate": "taxsparrow.gst_india.overrides.party.validate_party",
        "after_insert": (
            "taxsparrow.gst_india.overrides.party.create_primary_address"
        ),
    },
    "Delivery Note": {
        "on_trash": (
            "taxsparrow.gst_india.overrides.transaction.ignore_logs_on_trash"
        ),
        "onload": "taxsparrow.gst_india.overrides.delivery_note.onload",
        "validate": (
            "taxsparrow.gst_india.overrides.transaction.validate_transaction"
        ),
    },
    "GL Entry": {
        "validate": "taxsparrow.gst_india.overrides.gl_entry.validate",
    },
    "Item": {"validate": "taxsparrow.gst_india.overrides.item.validate"},
    "Journal Entry": {
        "validate": "taxsparrow.gst_india.overrides.journal_entry.validate",
    },
    "Payment Entry": {
        "validate": "taxsparrow.gst_india.overrides.payment_entry.validate",
        "on_submit": "taxsparrow.gst_india.overrides.payment_entry.on_submit",
        "on_update_after_submit": "taxsparrow.gst_india.overrides.payment_entry.on_update_after_submit",
    },
    "Purchase Invoice": {
        "onload": "taxsparrow.gst_india.overrides.purchase_invoice.onload",
        "validate": "taxsparrow.gst_india.overrides.purchase_invoice.validate",
        "before_validate": (
            "taxsparrow.gst_india.overrides.transaction.before_validate"
        ),
    },
    "Purchase Order": {
        "validate": (
            "taxsparrow.gst_india.overrides.transaction.validate_transaction"
        ),
        "before_validate": (
            "taxsparrow.gst_india.overrides.transaction.before_validate"
        ),
    },
    "Purchase Receipt": {
        "validate": (
            "taxsparrow.gst_india.overrides.transaction.validate_transaction"
        ),
        "before_validate": (
            "taxsparrow.gst_india.overrides.transaction.before_validate"
        ),
    },
    "Sales Invoice": {
        "on_trash": (
            "taxsparrow.gst_india.overrides.transaction.ignore_logs_on_trash"
        ),
        "onload": "taxsparrow.gst_india.overrides.sales_invoice.onload",
        "validate": "taxsparrow.gst_india.overrides.sales_invoice.validate",
        "on_submit": "taxsparrow.gst_india.overrides.sales_invoice.on_submit",
        "on_update_after_submit": "taxsparrow.gst_india.overrides.sales_invoice.on_update_after_submit",
    },
    "Sales Order": {
        "validate": (
            "taxsparrow.gst_india.overrides.transaction.validate_transaction"
        ),
    },
    "Supplier": {
        "validate": [
            "taxsparrow.gst_india.overrides.supplier.validate",
            "taxsparrow.gst_india.overrides.party.validate_party",
        ],
        "after_insert": (
            "taxsparrow.gst_india.overrides.party.create_primary_address"
        ),
    },
    "Tax Category": {
        "validate": "taxsparrow.gst_india.overrides.tax_category.validate"
    },
    "Tax Withholding Category": {
        "on_change": "taxsparrow.income_tax_india.overrides.tax_withholding_category.on_change",
    },
    "POS Invoice": {
        "validate": (
            "taxsparrow.gst_india.overrides.transaction.validate_transaction"
        ),
    },
    "Quotation": {
        "validate": (
            "taxsparrow.gst_india.overrides.transaction.validate_transaction"
        ),
    },
    "Accounts Settings": {
        "validate": "taxsparrow.audit_trail.overrides.accounts_settings.validate"
    },
    "Property Setter": {
        "validate": "taxsparrow.audit_trail.overrides.property_setter.validate",
        "on_trash": "taxsparrow.audit_trail.overrides.property_setter.on_trash",
    },
    "Version": {
        "validate": "taxsparrow.audit_trail.overrides.version.validate",
        "on_trash": "taxsparrow.audit_trail.overrides.version.on_trash",
    },
}


regional_overrides = {
    "India": {
        "erpnext.controllers.taxes_and_totals.get_itemised_tax_breakup_header": "taxsparrow.gst_india.overrides.transaction.get_itemised_tax_breakup_header",
        "erpnext.controllers.taxes_and_totals.get_itemised_tax_breakup_data": "taxsparrow.gst_india.overrides.transaction.get_itemised_tax_breakup_data",
        "erpnext.controllers.taxes_and_totals.get_regional_round_off_accounts": "taxsparrow.gst_india.overrides.transaction.get_regional_round_off_accounts",
        "erpnext.controllers.accounts_controller.update_gl_dict_with_regional_fields": "taxsparrow.gst_india.overrides.gl_entry.update_gl_dict_with_regional_fields",
        "erpnext.controllers.accounts_controller.get_advance_payment_entries_for_regional": (
            "taxsparrow.gst_india.overrides.payment_entry.get_advance_payment_entries_for_regional"
        ),
        "erpnext.accounts.doctype.payment_reconciliation.payment_reconciliation.adjust_allocations_for_taxes": (
            "taxsparrow.gst_india.overrides.payment_entry.adjust_allocations_for_taxes_in_payment_reconciliation"
        ),
        "erpnext.accounts.party.get_regional_address_details": (
            "taxsparrow.gst_india.overrides.transaction.update_party_details"
        ),
        "erpnext.assets.doctype.asset.asset.get_updated_rate_of_depreciation_for_wdv_and_dd": (
            "taxsparrow.income_tax_india.overrides.asset.get_updated_rate_of_depreciation_for_wdv_and_dd"
        ),
    }
}

jinja = {
    "methods": [
        "taxsparrow.gst_india.utils.get_state",
        "taxsparrow.gst_india.utils.jinja.add_spacing",
        "taxsparrow.gst_india.utils.jinja.get_supply_type",
        "taxsparrow.gst_india.utils.jinja.get_sub_supply_type",
        "taxsparrow.gst_india.utils.jinja.get_e_waybill_qr_code",
        "taxsparrow.gst_india.utils.jinja.get_qr_code",
        "taxsparrow.gst_india.utils.jinja.get_transport_type",
        "taxsparrow.gst_india.utils.jinja.get_transport_mode",
        "taxsparrow.gst_india.utils.jinja.get_ewaybill_barcode",
        "taxsparrow.gst_india.utils.jinja.get_e_invoice_item_fields",
        "taxsparrow.gst_india.utils.jinja.get_e_invoice_amount_fields",
    ],
}

override_doctype_dashboards = {
    "Sales Invoice": (
        "taxsparrow.gst_india.overrides.sales_invoice.get_dashboard_data"
    ),
    "Delivery Note": (
        "taxsparrow.gst_india.overrides.delivery_note.get_dashboard_data"
    ),
    "Purchase Invoice": (
        "taxsparrow.gst_india.overrides.purchase_invoice.get_dashboard_data"
    ),
}

override_doctype_class = {
    "Customize Form": (
        "taxsparrow.audit_trail.overrides.customize_form.CustomizeForm"
    ),
}


# DocTypes to be ignored while clearing transactions of a Company
company_data_to_be_ignored = ["GST Account", "GST Credential"]

# Links to these doctypes will be ignored when deleting a document
ignore_links_on_delete = ["e-Waybill Log", "e-Invoice Log"]

accounting_dimension_doctypes = ["Bill of Entry", "Bill of Entry Item"]

# DocTypes for which Audit Trail must be maintained
audit_trail_doctypes = [
    # To track the "Enable Audit Trail" setting
    "Accounts Settings",
    # ERPNext DocTypes that make GL Entries
    "Dunning",
    "Invoice Discounting",
    "Journal Entry",
    "Payment Entry",
    "Period Closing Voucher",
    "Process Deferred Accounting",
    "Purchase Invoice",
    "Sales Invoice",
    "Asset",
    "Asset Capitalization",
    "Asset Repair",
    "Loan Balance Adjustment",
    "Loan Disbursement",
    "Loan Interest Accrual",
    "Loan Refund",
    "Loan Repayment",
    "Loan Write Off",
    "Delivery Note",
    "Landed Cost Voucher",
    "Purchase Receipt",
    "Stock Entry",
    "Stock Reconciliation",
    "Subcontracting Receipt",
    # Additional  DocTypes that constitute "Books of Account"
    "POS Invoice",
    # Tax Sparrow DocTypes that make GL Entries
    "Bill of Entry",
]

scheduler_events = {
    "cron": {
        "*/5 * * * *": [
            "taxsparrow.gst_india.utils.e_invoice.retry_e_invoice_generation",
            "taxsparrow.gst_india.utils.gstr.download_queued_request",
        ],
    }
}


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/taxsparrow/css/taxsparrow.css"

# include js, css files in header of web template
# web_include_css = "/assets/taxsparrow/css/taxsparrow.css"
# web_include_js = "/assets/taxsparrow/js/taxsparrow.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "taxsparrow/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "taxsparrow.utils.jinja_methods",
# 	"filters": "taxsparrow.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "taxsparrow.install.before_install"

# Uninstallation
# ------------

# before_uninstall = "taxsparrow.uninstall.before_uninstall"
# after_uninstall = "taxsparrow.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "taxsparrow.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"taxsparrow.tasks.all"
# 	],
# 	"daily": [
# 		"taxsparrow.tasks.daily"
# 	],
# 	"hourly": [
# 		"taxsparrow.tasks.hourly"
# 	],
# 	"weekly": [
# 		"taxsparrow.tasks.weekly"
# 	],
# 	"monthly": [
# 		"taxsparrow.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "taxsparrow.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "taxsparrow.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "taxsparrow.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"taxsparrow.auth.validate"
# ]
