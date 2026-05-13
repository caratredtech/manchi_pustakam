frappe.ui.form.on('Quotation', {
    onload: function(frm) {
        frm.set_df_property('net_total', 'hidden', 1);
        check_duplicate_items_si(frm);
        set_packed_items(frm);
        update_packed_actual_qty(frm);
    },

    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Print'), function() {
                frm.print_doc();
            }).css('font-weight', 'bold');
        }
        if (!frm.is_new() && frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Create Sales Invoice'), function() {
                frappe.call({
                    method: 'manchipustakam.api.sales.make_sales_invoice',
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(r) {
                        if (r.message) {
                            frappe.model.sync(r.message);
                            frappe.set_route('Form', r.message.doctype, r.message.name);
                        }
                    }
                });
            });
        }
    },

    validate: function(frm) {
        check_duplicate_items_si(frm);
        set_packed_items(frm);
        update_packed_actual_qty(frm);
    }
});

frappe.ui.form.on('Quotation Item', {
    item_code: function(frm, cdt, cdn) {
        check_duplicate_items_si(frm);
    }
});

function check_duplicate_items_si(frm) {
    let seen = {};
    let duplicate_rows = [];
    let duplicate_items = [];

    (frm.doc.items || []).forEach(row => {
        if (row.item_code) {
            if (seen[row.item_code]) {
                duplicate_rows.push(row.name);
                if (!duplicate_items.includes(row.item_name || row.item_code)) {
                    duplicate_items.push(row.item_name || row.item_code);
                }
            } else {
                seen[row.item_code] = true;
            }
        }
    });

    if (duplicate_rows.length) {
        let message = duplicate_items.map(item => `- ${item}`).join('<br>');
        frappe.msgprint({
            title: __('Duplicate Books Found'),
            indicator: 'red',
            message: __('Same Book is selected in multiple rows:<br><br>') + message
        });
        duplicate_rows.forEach(name => {
            frappe.model.clear_doc("Quotation Item", name);
        });
        frm.doc.items = (frm.doc.items || []).filter(row => !duplicate_rows.includes(row.name));
        frm.refresh_field("items");
    }
}

function set_packed_items(frm) {
    if (frm.doc.packed_items && frm.doc.packed_items.length) {
        frm.doc.packed_items.forEach(row => {
            row.warehouse = "Nagole - M";
        });
        frm.refresh_field("packed_items");
    }
}

function update_packed_actual_qty(frm) {
    if (frm.doc.packed_items && frm.doc.packed_items.length) {

        frm.doc.packed_items.forEach(row => {

            if (row.item_code && row.warehouse) {

                frappe.call({
                    method: "erpnext.stock.utils.get_latest_stock_qty",
                    args: {
                        item_code: row.item_code,
                        warehouse: row.warehouse
                    },
                    callback: function(r) {
                        if (r.message !== undefined) {
                            row.actual_qty = r.message;
                            frm.refresh_field("packed_items");
                        }
                    }
                });

            }
        });
    }
}
