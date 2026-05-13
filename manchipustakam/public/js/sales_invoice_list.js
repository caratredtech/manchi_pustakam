let sales_invoice_listview;

frappe.listview_settings["Sales Invoice"] = {
    add_fields: ["rounded_total"],

    onload(listview) {
        sales_invoice_listview = listview;
        add_sales_invoice_compact_list_styles();
        add_rounded_total_column(listview);
        apply_sales_invoice_compact_list_class(listview);
        listview.refresh(true);
    },

    before_render() {
        if (sales_invoice_listview) {
            add_rounded_total_column(sales_invoice_listview);
        }
    },

    refresh(listview) {
        sales_invoice_listview = listview;
        add_rounded_total_column(listview);
        apply_sales_invoice_compact_list_class(listview);
    }
};

function add_rounded_total_column(listview) {
    if (!listview?.columns?.length || has_column(listview, "rounded_total")) {
        return;
    }

    const df = frappe.meta.get_docfield("Sales Invoice", "rounded_total") || {
        fieldname: "rounded_total",
        fieldtype: "Currency",
        label: __("Rounded Total")
    };
    const rounded_total_column = {
        type: "Field",
        df
    };
    const sales_channel_index = listview.columns.findIndex((column) => {
        return column.df?.fieldname === "custom_sales_channel";
    });

    if (sales_channel_index > -1) {
        listview.columns.splice(sales_channel_index, 0, rounded_total_column);
    } else {
        listview.columns.push(rounded_total_column);
    }
}

function has_column(listview, fieldname) {
    return listview.columns.some((column) => column.df?.fieldname === fieldname);
}

function apply_sales_invoice_compact_list_class(listview) {
    listview.$result.addClass("sales-invoice-compact-list");
}

function add_sales_invoice_compact_list_styles() {
    if (document.getElementById("sales-invoice-compact-list-styles")) {
        return;
    }

    const style = document.createElement("style");
    style.id = "sales-invoice-compact-list-styles";
    style.textContent = `
        .sales-invoice-compact-list .level-left .list-row-col {
            margin-right: 8px;
        }

        .sales-invoice-compact-list .level-left .list-row-col.name,
        .sales-invoice-compact-list .level-left .list-row-col.posting_date {
            width: 125px !important;
            flex: 0 0 125px !important;
        }

        .sales-invoice-compact-list .level-left .list-row-col.status,
        .sales-invoice-compact-list .level-left .list-row-col:not(.tag-col):not(.name):not(.posting_date):not(.customer_name):not(.rounded_total):not(.custom_sales_channel) {
            width: 105px !important;
            flex: 0 0 105px !important;
        }

        .sales-invoice-compact-list .level-left .list-row-col.customer_name {
            width: 115px !important;
            flex: 0 0 115px !important;
        }

        .sales-invoice-compact-list .level-left .list-row-col.rounded_total {
            width: 115px !important;
            flex: 0 0 115px !important;
        }

        .sales-invoice-compact-list .level-left .list-row-col.custom_sales_channel {
            width: 95px !important;
            flex: 0 0 95px !important;
        }
    `;
    document.head.appendChild(style);
}
