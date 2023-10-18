frappe.pages["tax-sparrow"].on_page_load = async function (wrapper) {
    await frappe.require([
        "taxsparrow_account.bundle.js",
        "taxsparrow_account.bundle.css",
    ]);

    icAccountPage = new taxsparrow.pages.TaxSparrowAccountPage(wrapper, PAGE_NAME);
};
