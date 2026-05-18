# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe
from frappe.desk.utils import provide_binary_file
from frappe.utils.xlsxutils import make_xlsx

def execute(filters=None):
    filters = filters or {}
    columns = get_columns()
    data = get_data(filters)
    return columns, data

@frappe.whitelist()
def download_excel(filters=None):
    filters = frappe.parse_json(filters or "{}")
    columns = get_columns()
    data = get_data(filters)
    header_info = get_header_info()

    xlsx_data = [
        [header_info["title"]],
        [header_info["company_name"]],
    ]

    for address_line in header_info["address_lines"]:
        xlsx_data.append([address_line])

    xlsx_data.append([])
    header_index = len(xlsx_data)
    xlsx_data.append([column["label"] for column in columns])

    for row in data:
        xlsx_data.append([row.get(column["fieldname"]) for column in columns])

    column_widths = [max(10, min(40, int((column.get("width") or 100) / 7))) for column in columns]
    content = make_xlsx(
        xlsx_data,
        "Book Catalogue",
        column_widths=column_widths,
        header_index=header_index,
    ).getvalue()

    provide_binary_file("Manchi Pustakam Catalogue", "xlsx", content)

def get_header_info():
    default_company = frappe.defaults.get_defaults().get("company") or frappe.db.get_single_value("Global Defaults", "default_company")
    header_info = {
        "title": "Manchi Pustakam Catalogue",
        "company_name": default_company or "Manchi Pustakam",
        "address_lines": [],
    }

    if default_company:
        company = frappe.db.get_value("Company", default_company, ["company_name"], as_dict=True)
        if company:
            header_info["company_name"] = company.company_name or header_info["company_name"]

        address = frappe.db.sql(
            """
            SELECT
                a.address_line1,
                a.address_line2,
                a.city,
                a.state,
                a.pincode,
                a.country
            FROM `tabAddress` a
            INNER JOIN `tabDynamic Link` dl ON dl.parent = a.name
            WHERE dl.link_doctype = 'Company'
                AND dl.link_name = %(company)s
                AND dl.parenttype = 'Address'
            ORDER BY a.is_primary_address DESC, a.creation ASC
            LIMIT 1
            """,
            {"company": default_company},
            as_dict=True,
        )

        if address:
            address = address[0]
            city_line = ", ".join(filter(None, [address.city, address.state, address.pincode]))
            header_info["address_lines"] = [
                address.address_line1,
                address.address_line2,
                city_line,
                address.country,
            ]
            header_info["address_lines"] = [line for line in header_info["address_lines"] if line]

    return header_info

def get_columns():
    return [
        {"label": "Title", "fieldname": "item_name", "fieldtype": "Data", "width": 250},
        {"label": "Author", "fieldname": "custom_author", "fieldtype": "Data", "width": 180},
        {"label": "Publisher", "fieldname": "publisher", "fieldtype": "Data", "width": 180},
        {"label": "Year", "fieldname": "year", "fieldtype": "Data", "width": 80},
        {"label": "Pages", "fieldname": "pages", "fieldtype": "Int", "width": 80},
        {"label": "Price", "fieldname": "standard_selling_price", "fieldtype": "Currency", "width": 100},
        {"label": "Subject", "fieldname": "subject", "fieldtype": "Data", "width": 150},
        {"label": "Language", "fieldname": "language", "fieldtype": "Data", "width": 100},
        {"label": "Age Group", "fieldname": "age_group", "fieldtype": "Data", "width": 120},
        {"label": "Catalogue", "fieldname": "catalogue", "fieldtype": "Data", "width": 150},
        {"label": "Store Rack No", "fieldname": "rack_no", "fieldtype": "Data", "width": 120},
        {"label": "Book Series", "fieldname": "series", "fieldtype": "Int", "width": 120},
    ]

def get_data(filters):
    conditions = []
    values = {}

    if filters.get("publisher_type"):
        conditions.append("i.brand = %(publisher_type)s")
        values["publisher_type"] = filters.get("publisher_type")

    if filters.get("age_group"):
        conditions.append("i.custom_age_group = %(age_group)s")
        values["age_group"] = filters.get("age_group")

    if filters.get("subject"):
        conditions.append("i.item_group = %(subject)s")
        values["subject"] = filters.get("subject")

    if filters.get("language"):
        conditions.append("i.custom_languages = %(language)s")
        values["language"] = filters.get("language")

    if filters.get("catalogue"):
        conditions.append("i.custom_catalogue_ = %(catalogue)s")
        values["catalogue"] = filters.get("catalogue")

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    query = f"""
        SELECT
            i.item_name,
            i.custom_author,
            i.brand AS publisher,
            i.custom_year_of_publication AS year,
            i.custom_pages AS pages,
            ip.price_list_rate AS standard_selling_price,
            i.item_group AS subject,
            i.custom_languages AS language,
            i.custom_age_group AS age_group,
            i.custom_catalogue_ AS catalogue,
            i.custom_store_rack_no AS rack_no,
            i.custom_series AS series
        FROM `tabItem` i
        LEFT JOIN (
            SELECT
                item_code,
                MAX(price_list_rate) AS price_list_rate
            FROM `tabItem Price`
            WHERE selling = 1
            GROUP BY item_code
        ) ip ON ip.item_code = i.name
        WHERE {where_clause}
        ORDER BY series ASC
    """

    return frappe.db.sql(query, values, as_dict=1)
