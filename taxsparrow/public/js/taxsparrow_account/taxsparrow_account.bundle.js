import Vue from "vue";
import VueRouter from "vue-router";
import Vuex from "vuex";

import router from "./router";
import store from "./store/index";
import TaxSparrowAccountApp from "./TaxSparrowAccountApp.vue";
import { get_api_secret } from "./services/AuthService";

class TaxSparrowAccountPage {
    constructor(wrapper) {
        this.pageName = "tax-sparrow";
        this.containerId = "tax-sparrow-app-container";

        // Why need container? Because Vue replaces the element with the component.
        // So, if we don't have a container, the component will be rendered on the #body
        // and removes the element #page-tax-sparrow,
        // which is required by frappe route in order to work it properly.
        $(wrapper).html(`<div id="${this.containerId}"></div>`);
        this.setTitle();
        this.show();
    }

    setTitle() {
        frappe.utils.set_title(__("Tax Sparrow Account"));
    }

    show() {
        Vue.use(VueRouter);
        Vue.use(Vuex);

        new Vue({
            el: `#${this.containerId}`,
            router,
            store,
            render: (h) => h(TaxSparrowAccountApp),
        });

        $(frappe.pages[this.pageName]).on("show", () => {
            this.setTitle();
            router.replace({name: store.getters.isLoggedIn ? "home": "auth"});
        });
    }
}

frappe.provide("taxsparrow.pages");
taxsparrow.pages.TaxSparrowAccountPage = TaxSparrowAccountPage;

frappe.provide("taxsparrow.gst_api");
taxsparrow.gst_api.call = async function (endpoint, options) {
    try {
        const base_url = "https://asp.sparrownova.com/v1/";
        const url = base_url + endpoint;

        const headers = { "Content-Type": "application/json" };
        if (options.headers) Object.assign(headers, options.headers);

        if (options.with_api_secret || options.api_secret) {
            const api_secret = options.api_secret || (await get_api_secret());
            headers["x-api-key"] = api_secret;
        }

        const args = {
            method: options.method || "POST",
            headers,
            mode: "cors",
        };

        if (options.body) args.body = JSON.stringify(options.body);

        const response = await fetch(url, args);
        const data = await response.json();
        if (response.ok) return { success: true, ...data };

        throw new UnsuccessfulResponseError(data);
    } catch (e) {
        const error =
            e.message || "Something went wrong, Please try again later!";

        if (!options.fail_silently) {
            frappe.msgprint({
                message: error,
                title: "Error",
                indicator: "red",
            });
        }

        return {
            ...e.response,
            success: false,
            error,
            invalid_token: e.response.exc_type?.includes(
                "InvalidAuthorizationToken"
            ),
        };
    }
};

function extract_error_message(responseBody) {
    const { exc_type, exception, _server_messages } = responseBody;
    if (!exception) {
        if (_server_messages) {
            const server_messages = JSON.parse(_server_messages);
            return server_messages
                .map((message) => JSON.parse(message).message || "")
                .join("\n");
        }
        return "Something went wrong, Please try again later!";
    }
    return exception
        .replace(new RegExp(".*" + exc_type + ":", "gi"), "")
        .trim();
}

class UnsuccessfulResponseError extends Error {
    constructor(response) {
        super(extract_error_message(response));
        this.response = response;
    }
}
