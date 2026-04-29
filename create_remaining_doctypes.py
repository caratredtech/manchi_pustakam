#!/usr/bin/env python3
"""Create Purchase Order and Payment Entry doctypes"""

import json
from pathlib import Path

BASE_PATH = Path(__file__).parent / "manchipustakam" / "manchi_pustakam" / "doctype"

def create_doctype(folder_name, doctype_config):
    folder = BASE_PATH / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    with open(folder / "__init__.py", 'w') as f:
        f.write(f"# {doctype_config['name']}\n")

    with open(folder / f"{folder_name}.json", 'w') as f:
        json.dump(doctype_config, f, indent=1)

    class_name = "".join([w.capitalize() for w in doctype_config['name'].replace(" ", "").replace("MP", "MP")])
    py_content = f'''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class {class_name}(Document):
\tpass
'''

    with open(folder / f"{folder_name}.py", 'w') as f:
        f.write(py_content)

    print(f"✓ Created {doctype_config['name']}")

# Purchase Order Item
po_item_config = {
    "name": "MP Purchase Order Item",
    "module": "Manchi Pustakam",
    "istable": 1,
    "editable_grid": 1,
    "fields": [
        {"fieldname": "book", "fieldtype": "Link", "label": "Book", "options": "Book", "reqd": 1, "in_list_view": 1},
        {"fieldname": "book_title", "fieldtype": "Data", "label": "Book Title", "fetch_from": "book.book_title", "read_only": 1, "in_list_view": 1},
        {"fieldname": "warehouse", "fieldtype": "Link", "label": "Warehouse", "options": "MP Warehouse", "reqd": 1},
        {"fieldname": "qty", "fieldtype": "Float", "label": "Quantity", "reqd": 1, "in_list_view": 1},
        {"fieldname": "rate", "fieldtype": "Currency", "label": "Rate", "reqd": 1, "in_list_view": 1},
        {"fieldname": "amount", "fieldtype": "Currency", "label": "Amount", "read_only": 1, "in_list_view": 1},
        {"fieldname": "received_qty", "fieldtype": "Float", "label": "Received Qty", "read_only": 1, "default": "0"},
    ],
    "actions": [],
    "links": [],
    "permissions": [],
    "sort_field": "modified",
    "sort_order": "DESC",
}

# Purchase Order
po_config = {
    "name": "MP Purchase Order",
    "module": "Manchi Pustakam",
    "is_submittable": 1,
    "autoname": "naming_series:",
    "field_order": ["naming_series", "supplier", "supplier_name", "transaction_date", "required_by", "column_break_1",
                    "contact_person", "contact_mobile", "status", "items_section", "items",
                    "totals_section", "total_qty", "total", "column_break_total", "gst_amount", "grand_total",
                    "delivery_section", "delivery_challan_no", "delivery_challan_date", "column_break_delivery",
                    "received_status", "notes_section", "terms", "internal_notes"],
    "fields": [
        {"fieldname": "naming_series", "fieldtype": "Select", "label": "Series", "options": "PO-.YYYY.-", "reqd": 1, "default": "PO-.YYYY.-"},
        {"fieldname": "supplier", "fieldtype": "Link", "label": "Supplier", "options": "MP Supplier", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "supplier_name", "fieldtype": "Data", "label": "Supplier Name", "fetch_from": "supplier.supplier_name", "read_only": 1},
        {"fieldname": "transaction_date", "fieldtype": "Date", "label": "Order Date", "reqd": 1, "default": "Today"},
        {"fieldname": "required_by", "fieldtype": "Date", "label": "Required By"},
        {"fieldname": "column_break_1", "fieldtype": "Column Break"},
        {"fieldname": "contact_person", "fieldtype": "Data", "label": "Contact Person"},
        {"fieldname": "contact_mobile", "fieldtype": "Data", "label": "Mobile"},
        {"fieldname": "status", "fieldtype": "Select", "label": "Status", "options": "Draft\nSubmitted\nReceived\nPartly Received\nCancelled", "default": "Draft", "read_only": 1},
        {"fieldname": "items_section", "fieldtype": "Section Break", "label": "Items"},
        {"fieldname": "items", "fieldtype": "Table", "label": "Items", "options": "MP Purchase Order Item", "reqd": 1},
        {"fieldname": "totals_section", "fieldtype": "Section Break", "label": "Totals"},
        {"fieldname": "total_qty", "fieldtype": "Float", "label": "Total Quantity", "read_only": 1},
        {"fieldname": "total", "fieldtype": "Currency", "label": "Total", "read_only": 1},
        {"fieldname": "column_break_total", "fieldtype": "Column Break"},
        {"fieldname": "gst_amount", "fieldtype": "Currency", "label": "GST Amount"},
        {"fieldname": "grand_total", "fieldtype": "Currency", "label": "Grand Total", "read_only": 1},
        {"fieldname": "delivery_section", "fieldtype": "Section Break", "label": "Delivery Details"},
        {"fieldname": "delivery_challan_no", "fieldtype": "Data", "label": "Delivery Challan No"},
        {"fieldname": "delivery_challan_date", "fieldtype": "Date", "label": "Delivery Challan Date"},
        {"fieldname": "column_break_delivery", "fieldtype": "Column Break"},
        {"fieldname": "received_status", "fieldtype": "Select", "label": "Received Status", "options": "Not Received\nPartly Received\nFully Received", "default": "Not Received"},
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

# Payment Entry
pe_config = {
    "name": "MP Payment Entry",
    "module": "Manchi Pustakam",
    "is_submittable": 1,
    "autoname": "naming_series:",
    "field_order": ["naming_series", "payment_type", "party_type", "party", "party_name", "column_break_1",
                    "posting_date", "reference_no", "reference_date", "payment_section", "payment_method",
                    "payment_gateway", "mode_of_payment", "column_break_payment", "paid_amount", "gateway_commission",
                    "net_amount", "settlement_section", "settlement_id", "settlement_date", "column_break_settlement",
                    "settlement_status", "reference_section", "references", "accounting_section", "bank_account",
                    "column_break_acc", "remarks"],
    "fields": [
        {"fieldname": "naming_series", "fieldtype": "Select", "label": "Series", "options": "PE-.YYYY.-", "reqd": 1, "default": "PE-.YYYY.-"},
        {"fieldname": "payment_type", "fieldtype": "Select", "label": "Payment Type", "options": "Receive\nPay", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "party_type", "fieldtype": "Select", "label": "Party Type", "options": "\nMP Customer\nMP Supplier", "reqd": 1},
        {"fieldname": "party", "fieldtype": "Dynamic Link", "label": "Party", "options": "party_type", "reqd": 1, "in_standard_filter": 1},
        {"fieldname": "party_name", "fieldtype": "Data", "label": "Party Name", "read_only": 1},
        {"fieldname": "column_break_1", "fieldtype": "Column Break"},
        {"fieldname": "posting_date", "fieldtype": "Date", "label": "Posting Date", "reqd": 1, "default": "Today"},
        {"fieldname": "reference_no", "fieldtype": "Data", "label": "Reference No"},
        {"fieldname": "reference_date", "fieldtype": "Date", "label": "Reference Date"},
        {"fieldname": "payment_section", "fieldtype": "Section Break", "label": "Payment Details"},
        {"fieldname": "payment_method", "fieldtype": "Select", "label": "Payment Method", "options": "\nCash\nOnline Transfer\nPhone Pe\nRazor Pay\nCheque\nUPI", "reqd": 1},
        {"fieldname": "payment_gateway", "fieldtype": "Select", "label": "Payment Gateway", "options": "\nRazor Pay\nPhone Pe", "depends_on": "eval:['Phone Pe', 'Razor Pay'].includes(doc.payment_method)"},
        {"fieldname": "mode_of_payment", "fieldtype": "Data", "label": "Mode of Payment"},
        {"fieldname": "column_break_payment", "fieldtype": "Column Break"},
        {"fieldname": "paid_amount", "fieldtype": "Currency", "label": "Paid Amount", "reqd": 1},
        {"fieldname": "gateway_commission", "fieldtype": "Currency", "label": "Gateway Commission", "default": "0"},
        {"fieldname": "net_amount", "fieldtype": "Currency", "label": "Net Amount", "read_only": 1},
        {"fieldname": "settlement_section", "fieldtype": "Section Break", "label": "Settlement Details", "depends_on": "eval:doc.payment_gateway"},
        {"fieldname": "settlement_id", "fieldtype": "Data", "label": "Settlement ID"},
        {"fieldname": "settlement_date", "fieldtype": "Date", "label": "Settlement Date"},
        {"fieldname": "column_break_settlement", "fieldtype": "Column Break"},
        {"fieldname": "settlement_status", "fieldtype": "Select", "label": "Settlement Status", "options": "Pending\nSettled\nFailed", "default": "Pending"},
        {"fieldname": "reference_section", "fieldtype": "Section Break", "label": "Reference"},
        {"fieldname": "references", "fieldtype": "Text", "label": "Invoice References"},
        {"fieldname": "accounting_section", "fieldtype": "Section Break", "label": "Accounting"},
        {"fieldname": "bank_account", "fieldtype": "Data", "label": "Bank Account"},
        {"fieldname": "column_break_acc", "fieldtype": "Column Break"},
        {"fieldname": "remarks", "fieldtype": "Small Text", "label": "Remarks"},
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

# Create all doctypes
print("Creating remaining transaction doctypes...\n")
create_doctype("mp_purchase_order_item", po_item_config)
create_doctype("mp_purchase_order", po_config)
create_doctype("mp_payment_entry", pe_config)

print("\n✓ Successfully created Purchase Order and Payment Entry doctypes!")
