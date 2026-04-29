#!/usr/bin/env python3
"""Create all reports for Manchi Pustakam"""

import json
from pathlib import Path

BASE_PATH = Path(__file__).parent / "manchipustakam" / "manchi_pustakam" / "report"

def create_report(folder_name, report_config, query_content):
    """Create a report with JSON and Python files"""
    folder = BASE_PATH / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    with open(folder / "__init__.py", 'w') as f:
        f.write(f"# {report_config['name']}\n")

    # Create JSON file
    with open(folder / f"{folder_name}.json", 'w') as f:
        json.dump(report_config, f, indent=1)

    # Create Python file
    with open(folder / f"{folder_name}.py", 'w') as f:
        f.write(query_content)

    print(f"✓ Created {report_config['name']}")

# 1. Book Catalogue Report
book_catalogue_config = {
    "name": "Book Catalogue",
    "module": "Manchi Pustakam",
    "report_type": "Script Report",
    "is_standard": "Yes",
    "ref_doctype": "Book"
}

book_catalogue_query = '''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
\tcolumns = get_columns()
\tdata = get_data(filters)
\treturn columns, data

def get_columns():
\treturn [
\t\t{"label": "Book Code", "fieldname": "book_code", "fieldtype": "Link", "options": "Book", "width": 120},
\t\t{"label": "Title", "fieldname": "book_title", "fieldtype": "Data", "width": 250},
\t\t{"label": "ISBN", "fieldname": "isbn", "fieldtype": "Data", "width": 130},
\t\t{"label": "Author", "fieldname": "author", "fieldtype": "Data", "width": 150},
\t\t{"label": "Publisher Type", "fieldname": "publisher_type", "fieldtype": "Data", "width": 120},
\t\t{"label": "Subject", "fieldname": "subject", "fieldtype": "Data", "width": 120},
\t\t{"label": "Age Group", "fieldname": "age_group", "fieldtype": "Data", "width": 100},
\t\t{"label": "Language", "fieldname": "language", "fieldtype": "Data", "width": 80},
\t\t{"label": "Selling Price", "fieldname": "standard_selling_price", "fieldtype": "Currency", "width": 100},
\t\t{"label": "Stock Qty", "fieldname": "stock_qty", "fieldtype": "Float", "width": 80},
\t\t{"label": "Reorder Level", "fieldname": "reorder_level", "fieldtype": "Int", "width": 100},
\t\t{"label": "Is Active", "fieldname": "is_active", "fieldtype": "Check", "width": 70}
\t]

def get_data(filters):
\tconditions = []
\tif filters.get("publisher_type"):
\t\tconditions.append(f"publisher_type = '{filters.get('publisher_type')}'")
\tif filters.get("age_group"):
\t\tconditions.append(f"age_group = '{filters.get('age_group')}'")
\tif filters.get("subject"):
\t\tconditions.append(f"subject LIKE '%{filters.get('subject')}%'")
\tif filters.get("is_active") is not None:
\t\tconditions.append(f"is_active = {filters.get('is_active')}")

\twhere_clause = " AND ".join(conditions) if conditions else "1=1"

\tquery = f"""
\t\tSELECT
\t\t\tbook_code,
\t\t\tbook_title,
\t\t\tisbn,
\t\t\tauthor,
\t\t\tpublisher_type,
\t\t\tsubject,
\t\t\tage_group,
\t\t\tlanguage,
\t\t\tstandard_selling_price,
\t\t\treorder_level,
\t\t\tis_active,
\t\t\t0 as stock_qty
\t\tFROM `tabBook`
\t\tWHERE {where_clause}
\t\tORDER BY book_title
\t"""

\treturn frappe.db.sql(query, as_dict=1)
'''

# 2. Sales by Channel Report
sales_by_channel_config = {
    "name": "Sales by Channel",
    "module": "Manchi Pustakam",
    "report_type": "Script Report",
    "is_standard": "Yes",
    "ref_doctype": "MP Sales Invoice"
}

sales_by_channel_query = '''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import flt

def execute(filters=None):
\tcolumns = get_columns()
\tdata = get_data(filters)
\tchart = get_chart_data(data)
\treturn columns, data, None, chart

def get_columns():
\treturn [
\t\t{"label": "Sales Channel", "fieldname": "sales_channel", "fieldtype": "Data", "width": 150},
\t\t{"label": "Total Invoices", "fieldname": "total_invoices", "fieldtype": "Int", "width": 120},
\t\t{"label": "Total Qty", "fieldname": "total_qty", "fieldtype": "Float", "width": 100},
\t\t{"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 150},
\t\t{"label": "Avg Invoice Value", "fieldname": "avg_invoice_value", "fieldtype": "Currency", "width": 150},
\t\t{"label": "% of Total", "fieldname": "percentage", "fieldtype": "Percent", "width": 100}
\t]

def get_data(filters):
\tconditions = []
\tif filters.get("from_date"):
\t\tconditions.append(f"posting_date >= '{filters.get('from_date')}'")
\tif filters.get("to_date"):
\t\tconditions.append(f"posting_date <= '{filters.get('to_date')}'")

\twhere_clause = " AND ".join(conditions) if conditions else "1=1"

\tquery = f"""
\t\tSELECT
\t\t\tsales_channel,
\t\t\tCOUNT(*) as total_invoices,
\t\t\tSUM(total_qty) as total_qty,
\t\t\tSUM(grand_total) as total_amount,
\t\t\tAVG(grand_total) as avg_invoice_value
\t\tFROM `tabMP Sales Invoice`
\t\tWHERE docstatus = 1 AND {where_clause}
\t\tGROUP BY sales_channel
\t\tORDER BY total_amount DESC
\t"""

\tdata = frappe.db.sql(query, as_dict=1)

\t# Calculate percentage
\ttotal_sales = sum([flt(d.total_amount) for d in data])
\tfor d in data:
\t\td.percentage = (flt(d.total_amount) / total_sales * 100) if total_sales else 0

\treturn data

def get_chart_data(data):
\treturn {
\t\t"data": {
\t\t\t"labels": [d.sales_channel for d in data],
\t\t\t"datasets": [
\t\t\t\t{"name": "Sales Amount", "values": [d.total_amount for d in data]}
\t\t\t]
\t\t},
\t\t"type": "pie"
\t}
'''

# 3. Stock Availability Report
stock_availability_config = {
    "name": "Stock Availability Report",
    "module": "Manchi Pustakam",
    "report_type": "Script Report",
    "is_standard": "Yes",
    "ref_doctype": "Book"
}

stock_availability_query = '''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
\tcolumns = get_columns()
\tdata = get_data(filters)
\treturn columns, data

def get_columns():
\treturn [
\t\t{"label": "Book", "fieldname": "book", "fieldtype": "Link", "options": "Book", "width": 120},
\t\t{"label": "Title", "fieldname": "book_title", "fieldtype": "Data", "width": 200},
\t\t{"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "MP Warehouse", "width": 120},
\t\t{"label": "Actual Qty", "fieldname": "actual_qty", "fieldtype": "Float", "width": 100},
\t\t{"label": "Reserved Qty", "fieldname": "reserved_qty", "fieldtype": "Float", "width": 100},
\t\t{"label": "Available Qty", "fieldname": "available_qty", "fieldtype": "Float", "width": 120},
\t\t{"label": "Reorder Level", "fieldname": "reorder_level", "fieldtype": "Int", "width": 120},
\t\t{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100}
\t]

def get_data(filters):
\t# Get all books
\tbooks = frappe.get_all("Book", filters={"is_stock_item": 1}, fields=["name", "book_title", "reorder_level"])

\tdata = []
\tfor book in books:
\t\t# Get stock for each warehouse
\t\twarehouses = frappe.get_all("MP Warehouse", pluck="name")

\t\tfor warehouse in warehouses:
\t\t\t# Calculate actual stock (simplified - would need real stock ledger aggregation)
\t\t\tactual_qty = 0  # Would sum from Stock Ledger Entry

\t\t\t# Calculate reserved qty from quotations
\t\t\treserved_qty = frappe.db.sql("""
\t\t\t\tSELECT SUM(reserved_qty)
\t\t\t\tFROM `tabMP Sales Quotation Item`
\t\t\t\tWHERE book = %s AND warehouse = %s
\t\t\t\tAND parenttype = 'MP Sales Quotation'
\t\t\t\tAND parent IN (
\t\t\t\t\tSELECT name FROM `tabMP Sales Quotation`
\t\t\t\t\tWHERE docstatus = 1 AND status = 'Open' AND reserve_stock = 1
\t\t\t\t)
\t\t\t""", (book.name, warehouse))[0][0] or 0

\t\t\tavailable_qty = actual_qty - reserved_qty

\t\t\t# Determine status
\t\t\tif available_qty <= 0:
\t\t\t\tstatus = "Out of Stock"
\t\t\t\telif available_qty < book.reorder_level:
\t\t\t\tstatus = "Low Stock"
\t\t\telse:
\t\t\t\tstatus = "In Stock"

\t\t\tdata.append({
\t\t\t\t"book": book.name,
\t\t\t\t"book_title": book.book_title,
\t\t\t\t"warehouse": warehouse,
\t\t\t\t"actual_qty": actual_qty,
\t\t\t\t"reserved_qty": reserved_qty,
\t\t\t\t"available_qty": available_qty,
\t\t\t\t"reorder_level": book.reorder_level,
\t\t\t\t"status": status
\t\t\t})

\treturn data
'''

# 4. Reorder Report
reorder_report_config = {
    "name": "Reorder Report",
    "module": "Manchi Pustakam",
    "report_type": "Script Report",
    "is_standard": "Yes",
    "ref_doctype": "Book"
}

reorder_report_query = '''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
\tcolumns = get_columns()
\tdata = get_data(filters)
\treturn columns, data

def get_columns():
\treturn [
\t\t{"label": "Book", "fieldname": "book", "fieldtype": "Link", "options": "Book", "width": 120},
\t\t{"label": "Title", "fieldname": "book_title", "fieldtype": "Data", "width": 200},
\t\t{"label": "Current Stock", "fieldname": "current_stock", "fieldtype": "Float", "width": 120},
\t\t{"label": "Reorder Level", "fieldname": "reorder_level", "fieldtype": "Int", "width": 120},
\t\t{"label": "Reorder Qty", "fieldname": "reorder_qty", "fieldtype": "Int", "width": 120},
\t\t{"label": "Supplier", "fieldname": "preferred_supplier", "fieldtype": "Link", "options": "MP Supplier", "width": 150},
\t\t{"label": "Supplier Contact", "fieldname": "supplier_phone", "fieldtype": "Data", "width": 120},
\t\t{"label": "Lead Time", "fieldname": "supplier_lead_time_days", "fieldtype": "Int", "width": 100}
\t]

def get_data(filters):
\tquery = """
\t\tSELECT
\t\t\tb.name as book,
\t\t\tb.book_title,
\t\t\t0 as current_stock,
\t\t\tb.reorder_level,
\t\t\tb.reorder_qty,
\t\t\tb.preferred_supplier,
\t\t\ts.phone as supplier_phone,
\t\t\tb.supplier_lead_time_days
\t\tFROM `tabBook` b
\t\tLEFT JOIN `tabMP Supplier` s ON b.preferred_supplier = s.name
\t\tWHERE b.is_stock_item = 1
\t\t\tAND b.is_active = 1
\t\tORDER BY b.book_title
\t"""

\treturn frappe.db.sql(query, as_dict=1)
'''

# Create all reports
print("Creating reports for Manchi Pustakam...\n")

create_report("book_catalogue", book_catalogue_config, book_catalogue_query)
create_report("sales_by_channel", sales_by_channel_config, sales_by_channel_query)
create_report("stock_availability_report", stock_availability_config, stock_availability_query)
create_report("reorder_report", reorder_report_config, reorder_report_query)

print("\n✓ Successfully created 4 reports!")
