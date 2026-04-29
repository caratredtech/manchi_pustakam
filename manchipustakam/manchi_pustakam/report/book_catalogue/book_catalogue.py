# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    filters = filters or {}
    columns = get_columns()
    data = get_data(filters)
    return columns, data

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
            i.standard_rate AS standard_selling_price,
            i.item_group AS subject,
            i.custom_languages AS language,
            i.custom_age_group AS age_group,
            i.custom_catalogue_ AS catalogue,
            i.custom_store_rack_no AS rack_no,
            i.custom_series AS series
        FROM `tabItem` i
        WHERE {where_clause}
        ORDER BY series ASC
    """

    return frappe.db.sql(query, values, as_dict=1)