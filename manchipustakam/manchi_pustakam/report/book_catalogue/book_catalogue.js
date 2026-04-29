// Copyright (c) 2026, caratRED and contributors
// For license information, please see license.txt

frappe.query_reports["Book Catalogue"] = {
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