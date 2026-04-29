#!/usr/bin/env python3
"""
Generate all transaction doctypes for Manchi Pustakam
This creates Sales Quotation, Sales Order, Sales Invoice, Purchase Order, Payment Entry, and Settlement doctypes
"""

import json
import os
from pathlib import Path

BASE_PATH = Path(__file__).parent / "manchipustakam" / "manchi_pustakam" / "doctype"

def create_doctype(folder_name, doctype_config):
    """Create a complete doctype with JSON and Python files"""
    folder = BASE_PATH / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    with open(folder / "__init__.py", 'w') as f:
        f.write(f"# {doctype_config['name']}\n")

    # Create JSON file
    with open(folder / f"{folder_name}.json", 'w') as f:
        json.dump(doctype_config, f, indent=1)

    # Create Python file
    class_name = "".join([w.capitalize() for w in doctype_config['name'].replace(" ", "").replace("MP", "MP")])

    py_content = f'''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt, rounded

class {class_name}(Document):
\tpass
'''

    with open(folder / f"{folder_name}.py", 'w') as f:
        f.write(py_content)

    print(f"✓ Created {doctype_config['name']}")

# Define all transaction doctypes

# 1. MP Sales Quotation Item (Child Table)
sq_item_config = {
    "name": "MP Sales Quotation Item",
    "module": "Manchi Pustakam",
    "istable": 1,
    "editable_grid": 1,
    "fields": [
        {"fieldname": "book", "fieldtype": "Link", "label": "Book", "options": "Book", "reqd": 1, "in_list_view": 1},
        {"fieldname": "book_title", "fieldtype": "Data", "label": "Book Title", "fetch_from": "book.book_title", "read_only": 1, "in_list_view": 1},
        {"fieldname": "warehouse", "fieldtype": "Link", "label": "Warehouse", "options": "MP Warehouse", "reqd": 1},
        {"fieldname": "qty", "fieldtype": "Float", "label": "Quantity", "reqd": 1, "in_list_view": 1, "default": "1"},
        {"fieldname": "rate", "fieldtype": "Currency", "label": "Rate", "reqd": 1, "in_list_view": 1},
        {"fieldname": "discount_percent", "fieldtype": "Percent", "label": "Discount %", "default": "10"},
        {"fieldname": "amount", "fieldtype": "Currency", "label": "Amount", "read_only": 1, "in_list_view": 1},
        {"fieldname": "reserved_qty", "fieldtype": "Float", "label": "Reserved Qty", "read_only": 1, "default": "0"},
    ],
    "actions": [],
    "links": [],
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC",
}

# 2. MP Sales Quotation (Parent)
sq_config = {
    "name": "MP Sales Quotation",
    "module": "Manchi Pustakam",
    "is_submittable": 1,
    "autoname": "naming_series:",
    "field_order": ["naming_series", "customer", "customer_name", "quotation_date", "valid_till", "column_break_1",
                    "territory", "contact_person", "contact_mobile", "status", "stock_reservation_section", "reserve_stock",
                    "reservation_status", "column_break_res", "valid_till_extended", "items_section", "items",
                    "totals_section", "total_qty", "total", "column_break_total", "discount_amount", "grand_total",
                    "notes_section", "terms", "internal_notes"],
    "fields": [
        {"fieldname": "naming_series", "fieldtype": "Select", "label": "Series", "options": "SQ-.YYYY.-\nSQ-EX-.YYYY.-\nSQ-IN-.YYYY.-", "reqd": 1, "default": "SQ-.YYYY.-"},
        {"fieldname": "customer", "fieldtype": "Link", "label": "Customer", "options": "MP Customer", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "customer_name", "fieldtype": "Data", "label": "Customer Name", "fetch_from": "customer.customer_name", "read_only": 1},
        {"fieldname": "quotation_date", "fieldtype": "Date", "label": "Quotation Date", "reqd": 1, "default": "Today"},
        {"fieldname": "valid_till", "fieldtype": "Date", "label": "Valid Till", "reqd": 1},
        {"fieldname": "column_break_1", "fieldtype": "Column Break"},
        {"fieldname": "territory", "fieldtype": "Data", "label": "Territory", "fetch_from": "customer.territory"},
        {"fieldname": "contact_person", "fieldtype": "Data", "label": "Contact Person"},
        {"fieldname": "contact_mobile", "fieldtype": "Data", "label": "Mobile"},
        {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\nOpen\nOrdered\nExpired\nCancelled", "default": "Draft", "read_only": 1},
        {"fieldname": "stock_reservation_section", "fieldtype": "Section Break", "label": "Stock Reservation"},
        {"fieldname": "reserve_stock", "fieldtype": "Check", "label": "Reserve Stock", "default": "0"},
        {"fieldname": "reservation_status", "fieldtype": "Select", "label": "Reservation Status", "options": "Not Reserved\nReserved\nExpired\nReleased", "default": "Not Reserved", "read_only": 1},
        {"fieldname": "column_break_res", "fieldtype": "Column Break"},
        {"fieldname": "valid_till_extended", "fieldtype": "Date", "label": "Extended Validity"},
        {"fieldname": "items_section", "fieldtype": "Section Break", "label": "Items"},
        {"fieldname": "items", "fieldtype": "Table", "label": "Items", "options": "MP Sales Quotation Item", "reqd": 1},
        {"fieldname": "totals_section", "fieldtype": "Section Break", "label": "Totals"},
        {"fieldname": "total_qty", "fieldtype": "Float", "label": "Total Quantity", "read_only": 1},
        {"fieldname": "total", "fieldtype": "Currency", "label": "Total", "read_only": 1},
        {"fieldname": "column_break_total", "fieldtype": "Column Break"},
        {"fieldname": "discount_amount", "fieldtype": "Currency", "label": "Discount Amount"},
        {"fieldname": "grand_total", "fieldtype": "Currency", "label": "Grand Total", "read_only": 1},
        {"fieldname": "notes_section", "fieldtype": "Section Break", "label": "Terms & Notes"},
        {"fieldname": "terms", "fieldtype": "Text Editor", "label": "Terms and Conditions"},
        {"fieldname": "internal_notes", "fieldtype": "Text", "label": "Internal Notes"},
    ],
    "actions": [],
    "links": [],
    "permissions": [
        {"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 1, "cancel": 1, "amend": 1},
        {"role": "MP Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 1, "cancel": 1, "amend": 1},
        {"role": "MP User", "read": 1, "write": 1, "create": 1},
    ],
    "sort_field": "modified",
    "sort_order": "DESC",
    "track_changes": 1,
}

# 3. MP Sales Invoice Item (Child Table)
si_item_config = {
    "name": "MP Sales Invoice Item",
    "module": "Manchi Pustakam",
    "istable": 1,
    "editable_grid": 1,
    "fields": [
        {"fieldname": "book", "fieldtype": "Link", "label": "Book", "options": "Book", "reqd": 1, "in_list_view": 1},
        {"fieldname": "book_title", "fieldtype": "Data", "label": "Book Title", "fetch_from": "book.book_title", "read_only": 1, "in_list_view": 1},
        {"fieldname": "warehouse", "fieldtype": "Link", "label": "Warehouse", "options": "MP Warehouse", "reqd": 1},
        {"fieldname": "qty", "fieldtype": "Float", "label": "Quantity", "reqd": 1, "in_list_view": 1},
        {"fieldname": "rate", "fieldtype": "Currency", "label": "Rate", "reqd": 1, "in_list_view": 1},
        {"fieldname": "discount_percent", "fieldtype": "Percent", "label": "Discount %", "default": "10"},
        {"fieldname": "amount", "fieldtype": "Currency", "label": "Amount", "read_only": 1, "in_list_view": 1},
        {"fieldname": "gst_rate", "fieldtype": "Percent", "label": "GST %", "default": "0"},
        {"fieldname": "gst_amount", "fieldtype": "Currency", "label": "GST Amount", "read_only": 1},
    ],
    "actions": [],
    "links": [],
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC",
}

# 4. MP Sales Invoice (Parent) - CRITICAL DOCTYPE
si_config = {
    "name": "MP Sales Invoice",
    "module": "Manchi Pustakam",
    "is_submittable": 1,
    "autoname": "naming_series:",
    "field_order": ["naming_series", "customer", "customer_name", "posting_date", "due_date", "column_break_1",
                    "sales_channel", "payment_gateway", "settlement_id", "status", "items_section", "items",
                    "pricing_section", "total_qty", "total", "column_break_pricing", "discount_amount", "additional_discount_percent",
                    "charges_section", "packing_charges", "postage_charges", "transportation_charges", "other_charges",
                    "tax_section", "total_before_tax", "gst_amount", "column_break_tax", "rounded_total", "grand_total",
                    "payment_section", "payment_gateway_commission", "net_amount_received", "column_break_payment",
                    "outstanding_amount", "paid_amount", "payment_status", "notes_section", "terms", "internal_notes"],
    "fields": [
        {"fieldname": "naming_series", "fieldtype": "Select", "label": "Series", "options": "SI-.YYYY.-\nSI-CNT-.YYYY.-\nSI-WEB-.YYYY.-\nSI-EX-.YYYY.-\nSI-IN-.YYYY.-", "reqd": 1, "default": "SI-.YYYY.-"},
        {"fieldname": "customer", "fieldtype": "Link", "label": "Customer", "options": "MP Customer", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "customer_name", "fieldtype": "Data", "label": "Customer Name", "fetch_from": "customer.customer_name", "read_only": 1},
        {"fieldname": "posting_date", "fieldtype": "Date", "label": "Posting Date", "reqd": 1, "default": "Today"},
        {"fieldname": "due_date", "fieldtype": "Date", "label": "Due Date"},
        {"fieldname": "column_break_1", "fieldtype": "Column Break"},
        {"fieldname": "sales_channel", "fieldtype": "Select", "label": "Sales Channel", "options": "\nCounter Sales\nWebsite Sales\nExhibition Sales\nInstitutional Sales", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "payment_gateway", "fieldtype": "Select", "label": "Payment Gateway", "options": "\nCash\nOnline Transfer\nPhone Pe\nRazor Pay\nCheque"},
        {"fieldname": "settlement_id", "fieldtype": "Data", "label": "Settlement ID"},
        {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\nUnpaid\nPartly Paid\nPaid\nOverdue\nCancelled", "default": "Draft", "read_only": 1},
        {"fieldname": "items_section", "fieldtype": "Section Break", "label": "Items"},
        {"fieldname": "items", "fieldtype": "Table", "label": "Items", "options": "MP Sales Invoice Item", "reqd": 1},
        {"fieldname": "pricing_section", "fieldtype": "Section Break", "label": "Pricing"},
        {"fieldname": "total_qty", "fieldtype": "Float", "label": "Total Quantity", "read_only": 1},
        {"fieldname": "total", "fieldtype": "Currency", "label": "Total", "read_only": 1},
        {"fieldname": "column_break_pricing", "fieldtype": "Column Break"},
        {"fieldname": "discount_amount", "fieldtype": "Currency", "label": "Item Discount Amount", "read_only": 1},
        {"fieldname": "additional_discount_percent", "fieldtype": "Percent", "label": "Additional Discount %"},
        {"fieldname": "charges_section", "fieldtype": "Section Break", "label": "Additional Charges"},
        {"fieldname": "packing_charges", "fieldtype": "Currency", "label": "Packing Charges", "default": "0"},
        {"fieldname": "postage_charges", "fieldtype": "Currency", "label": "Postage Charges", "default": "0"},
        {"fieldname": "transportation_charges", "fieldtype": "Currency", "label": "Transportation Charges", "default": "0"},
        {"fieldname": "other_charges", "fieldtype": "Currency", "label": "Other Charges", "default": "0"},
        {"fieldname": "tax_section", "fieldtype": "Section Break", "label": "Tax & Total"},
        {"fieldname": "total_before_tax", "fieldtype": "Currency", "label": "Total Before Tax", "read_only": 1},
        {"fieldname": "gst_amount", "fieldtype": "Currency", "label": "GST Amount", "read_only": 1},
        {"fieldname": "column_break_tax", "fieldtype": "Column Break"},
        {"fieldname": "rounded_total", "fieldtype": "Currency", "label": "Rounded Total", "read_only": 1},
        {"fieldname": "grand_total", "fieldtype": "Currency", "label": "Grand Total", "read_only": 1},
        {"fieldname": "payment_section", "fieldtype": "Section Break", "label": "Payment Details"},
        {"fieldname": "payment_gateway_commission", "fieldtype": "Currency", "label": "Gateway Commission", "read_only": 1},
        {"fieldname": "net_amount_received", "fieldtype": "Currency", "label": "Net Amount Received", "read_only": 1},
        {"fieldname": "column_break_payment", "fieldtype": "Column Break"},
        {"fieldname": "outstanding_amount", "fieldtype": "Currency", "label": "Outstanding Amount", "read_only": 1},
        {"fieldname": "paid_amount", "fieldtype": "Currency", "label": "Paid Amount", "read_only": 1},
        {"fieldname": "payment_status", "fieldtype": "Select", "label": "Payment Status", "options": "Unpaid\nPartly Paid\nPaid", "default": "Unpaid"},
        {"fieldname": "notes_section", "fieldtype": "Section Break", "label": "Terms & Notes"},
        {"fieldname": "terms", "fieldtype": "Text Editor", "label": "Terms and Conditions"},
        {"fieldname": "internal_notes", "fieldtype": "Text", "label": "Internal Notes"},
    ],
    "actions": [],
    "links": [],
    "permissions": [
        {"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 1, "cancel": 1, "amend": 1},
        {"role": "MP Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 1, "cancel": 1, "amend": 1},
        {"role": "MP User", "read": 1, "write": 1, "create": 1},
    ],
    "sort_field": "modified",
    "sort_order": "DESC",
    "track_changes": 1,
}

# 5. Payment Gateway Settlement
pgs_config = {
    "name": "Payment Gateway Settlement",
    "module": "Manchi Pustakam",
    "is_submittable": 1,
    "autoname": "naming_series:",
    "field_order": ["naming_series", "gateway", "settlement_date", "settlement_id", "column_break_1",
                    "from_date", "to_date", "status", "transactions_section", "total_transactions",
                    "total_amount", "column_break_trans", "total_commission", "net_settlement_amount",
                    "reconciliation_section", "reconciled_transactions", "unreconciled_transactions",
                    "notes_section", "notes"],
    "fields": [
        {"fieldname": "naming_series", "fieldtype": "Select", "label": "Series", "options": "PGS-.YYYY.-", "reqd": 1, "default": "PGS-.YYYY.-"},
        {"fieldname": "gateway", "fieldtype": "Select", "label": "Payment Gateway", "options": "\nRazor Pay\nPhone Pe", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "settlement_date", "fieldtype": "Date", "label": "Settlement Date", "reqd": 1, "default": "Today"},
        {"fieldname": "settlement_id", "fieldtype": "Data", "label": "Settlement ID", "reqd": 1, "unique": 1},
        {"fieldname": "column_break_1", "fieldtype": "Column Break"},
        {"fieldname": "from_date", "fieldtype": "Date", "label": "From Date"},
        {"fieldname": "to_date", "fieldtype": "Date", "label": "To Date"},
        {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\nReconciled\nPartially Reconciled\nUnreconciled", "default": "Draft"},
        {"fieldname": "transactions_section", "fieldtype": "Section Break", "label": "Settlement Summary"},
        {"fieldname": "total_transactions", "fieldtype": "Int", "label": "Total Transactions", "read_only": 1},
        {"fieldname": "total_amount", "fieldtype": "Currency", "label": "Total Transaction Amount", "read_only": 1},
        {"fieldname": "column_break_trans", "fieldtype": "Column Break"},
        {"fieldname": "total_commission", "fieldtype": "Currency", "label": "Total Commission", "read_only": 1},
        {"fieldname": "net_settlement_amount", "fieldtype": "Currency", "label": "Net Settlement Amount", "read_only": 1},
        {"fieldname": "reconciliation_section", "fieldtype": "Section Break", "label": "Reconciliation Status"},
        {"fieldname": "reconciled_transactions", "fieldtype": "Int", "label": "Reconciled Transactions", "read_only": 1},
        {"fieldname": "unreconciled_transactions", "fieldtype": "Int", "label": "Unreconciled Transactions", "read_only": 1},
        {"fieldname": "notes_section", "fieldtype": "Section Break", "label": "Notes"},
        {"fieldname": "notes", "fieldtype": "Text", "label": "Notes"},
    ],
    "actions": [],
    "links": [],
    "permissions": [
        {"role": "System Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 1, "cancel": 1},
        {"role": "MP Manager", "read": 1, "write": 1, "create": 1, "delete": 1, "submit": 1, "cancel": 1},
        {"role": "MP User", "read": 1},
    ],
    "sort_field": "modified",
    "sort_order": "DESC",
    "track_changes": 1,
}

# Create all doctypes
print("Creating Transaction DocTypes for Manchi Pustakam...\n")

create_doctype("mp_sales_quotation_item", sq_item_config)
create_doctype("mp_sales_quotation", sq_config)
create_doctype("mp_sales_invoice_item", si_item_config)
create_doctype("mp_sales_invoice", si_config)
create_doctype("payment_gateway_settlement", pgs_config)

print("\n✓ Successfully created 5 critical transaction doctypes!")
print("\nNext steps:")
print("1. bench --site manchipustkam.local migrate")
print("2. Create server scripts for business logic")
print("3. Create reports")
print("4. Build POS interface")
