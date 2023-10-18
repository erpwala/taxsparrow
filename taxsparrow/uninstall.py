import click

from taxsparrow.gst_india.constants import BUG_REPORT_URL
from taxsparrow.gst_india.uninstall import before_uninstall as remove_gst
from taxsparrow.gst_india.uninstall import delete_hrms_custom_fields
from taxsparrow.income_tax_india.uninstall import (
    before_uninstall as remove_income_tax,
)


def before_uninstall():
    try:
        print("Removing TaxSparrow customizations...")
        remove_income_tax()

        print("Removing TaxSparro GST customizations...")
        remove_gst()

    except Exception as e:
        click.secho(
            (
                "Removing customizations for Tax Sparrow failed due to an error."
                " Please try again or"
                f" report the issue on {BUG_REPORT_URL} if not resolved."
            ),
            fg="bright_red",
        )
        raise e


def before_app_uninstall(app_name):
    if app_name == "hrms":
        delete_hrms_custom_fields()
