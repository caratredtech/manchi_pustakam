// Copyright (c) 2026, caratRED and contributors
// For license information, please see license.txt

frappe.query_reports["Book Catalogue"] = {
    onload: function(report) {
        const download_group = __("Download Report");
        const get_full_url = function(url) {
            if (!url || /^(https?:|data:)/.test(url)) {
                return url || "";
            }

            return frappe.urllib.get_full_url(url);
        };

        const get_image_data_url = async function(url) {
            if (!url || /^data:/.test(url)) {
                return url || "";
            }

            try {
                const response = await fetch(url, { credentials: "same-origin" });
                if (!response.ok) {
                    return "";
                }

                const blob = await response.blob();

                return await new Promise((resolve) => {
                    const reader = new FileReader();
                    reader.onloadend = () => resolve(reader.result || "");
                    reader.onerror = () => resolve("");
                    reader.readAsDataURL(blob);
                });
            } catch (error) {
                console.warn("Unable to load Book Catalogue logo", error);
                return "";
            }
        };

        report.download_book_catalogue_excel = function() {
            const filters = this.get_filter_values(true);
            const applied_filters = this.get_applied_filters(filters);
            const visible_idx = this.datatable?.bodyRenderer.visibleRowIndices || [];

            if (visible_idx.length + 1 === this.data?.length) {
                visible_idx.push(visible_idx.length);
            }

            open_url_post(frappe.request.url, {
                cmd: "frappe.desk.query_report.export_query",
                report_name: this.report_name,
                custom_columns: this.custom_columns?.length ? this.custom_columns : [],
                file_format_type: "Excel",
                filters: filters,
                applied_filters: applied_filters,
                visible_idx: visible_idx,
                include_filters: 1,
                include_hidden_columns: 0
            });
        };

        report.page.add_inner_button(
            __("Excel"),
            () => report.download_book_catalogue_excel(),
            download_group
        );

        report.page.add_inner_button(
            __("PDF"),
            () => report.pdf_report({ orientation: "Portrait" }),
            download_group
        );

        report.pdf_report = async function(print_settings) {
            const custom_format = this.report_settings.html_format;
            const filters = this.get_filter_values();
            const data = this.get_data_for_print();
            const columns = this.get_columns_for_print(print_settings, custom_format);

            const default_company = frappe.defaults.get_default("company") || frappe.boot.sysdefaults?.company;
            const header_info = {
                title: __("Manchi Pustakam Catalogue"),
                subtitle: __("Manchi Pustakam"),
                company_name: default_company || __("Manchi Pustakam"),
                logo: "/files/manchipusthakam1logo.png",
                address_lines: []
            };

            if (default_company) {
                try {
                    const company = await frappe.db.get_value("Company", default_company, ["company_name", "company_logo"]);
                    if (company?.message) {
                        header_info.company_name = company.message.company_name || header_info.company_name;
                    }
                } catch (error) {
                    console.warn("Unable to fetch company details for Book Catalogue PDF", error);
                }

                try {
                    const addresses = await frappe.db.get_list("Address", {
                        fields: ["address_line1", "address_line2", "city", "state", "pincode", "country"],
                        filters: [
                            ["Dynamic Link", "link_doctype", "=", "Company"],
                            ["Dynamic Link", "link_name", "=", default_company],
                            ["Dynamic Link", "parenttype", "=", "Address"]
                        ],
                        order_by: "is_primary_address desc, creation asc",
                        limit: 1
                    });

                    if (addresses && addresses.length) {
                        const address = addresses[0];
                        const city_line = [address.city, address.state, address.pincode].filter(Boolean).join(", ");
                        header_info.address_lines = [
                            address.address_line1,
                            address.address_line2,
                            city_line,
                            address.country
                        ].filter(Boolean);
                    }
                } catch (error) {
                    console.warn("Unable to fetch company address for Book Catalogue PDF", error);
                }
            }

            header_info.logo = await get_image_data_url(header_info.logo) || get_full_url(header_info.logo);

            const content = frappe.render_template(custom_format || "print_grid", {
                title: header_info.title,
                filters: filters,
                data: data,
                original_data: this.data,
                columns: columns,
                report: this,
                print_settings: print_settings,
                header_info: header_info
            });

            const html = `<!DOCTYPE html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title>${header_info.title}</title>
                    </head>
                    <body>${content}</body>
                </html>`;

            frappe.render_pdf(html, {
                orientation: print_settings.orientation || "Portrait",
                report_name: `${header_info.title}.pdf`
            });
        };
    },
    filters: [
        {
            fieldname: "publisher_type",
            label: "Publisher",
            fieldtype: "Link",
            options: "Brand"
        },
        {
            fieldname: "age_group",
            label: "Age Group",
            fieldtype: "Link",
            options: "Age Group"
        },
        {
            fieldname: "subject",
            label: "Subject",
            fieldtype: "Link",
            options: "Item Group"
        },
        {
            fieldname: "language",
            label: "Language",
            fieldtype: "Link",
            options: "Languages"
        },
        {
            fieldname: "catalogue",
            label: "Catalogue",
            fieldtype: "Link",
            options: "Catalogue"
        }
    ]
};
