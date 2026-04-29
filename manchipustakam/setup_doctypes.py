#!/usr/bin/env python3
"""
Manchi Pustakam - DocType Setup Script
This script creates all the necessary doctypes for the Manchi Pustakam application
"""

import json
import os
from pathlib import Path

# Base path for doctypes
BASE_PATH = Path(__file__).parent / "manchi_pustakam" / "doctype"

# Define all doctypes to be created
DOCTYPES = {
    "mp_warehouse": {
        "name": "MP Warehouse",
        "module": "Manchi Pustakam",
        "autoname": "field:warehouse_name",
        "fields": [
            {"fieldname": "warehouse_name", "fieldtype": "Data", "label": "Warehouse Name", "reqd": 1, "unique": 1},
            {"fieldname": "warehouse_type", "fieldtype": "Select", "label": "Warehouse Type", "options": "\nBulk Storage\nDisplay/Retail"},
            {"fieldname": "column_break_1", "fieldtype": "Column Break"},
            {"fieldname": "address", "fieldtype": "Small Text", "label": "Address"},
            {"fieldname": "city", "fieldtype": "Data", "label": "City"},
            {"fieldname": "contact_section", "fieldtype": "Section Break", "label": "Contact Details"},
            {"fieldname": "contact_person", "fieldtype": "Data", "label": "Contact Person"},
            {"fieldname": "phone", "fieldtype": "Data", "label": "Phone"},
            {"fieldname": "column_break_2", "fieldtype": "Column Break"},
            {"fieldname": "email", "fieldtype": "Data", "label": "Email"},
            {"fieldname": "is_active", "fieldtype": "Check", "label": "Is Active", "default": "1"},
        ]
    },
    "stock_ledger_entry": {
        "name": "Stock Ledger Entry",
        "module": "Manchi Pustakam",
        "autoname": "naming_series:",
        "fields": [
            {"fieldname": "naming_series", "fieldtype": "Select", "label": "Series", "options": "SLE-.YYYY.-", "default": "SLE-.YYYY.-"},
            {"fieldname": "posting_date", "fieldtype": "Date", "label": "Posting Date", "reqd": 1, "default": "Today"},
            {"fieldname": "posting_time", "fieldtype": "Time", "label": "Posting Time", "reqd": 1},
            {"fieldname": "column_break_1", "fieldtype": "Column Break"},
            {"fieldname": "book", "fieldtype": "Link", "label": "Book", "options": "Book", "reqd": 1},
            {"fieldname": "warehouse", "fieldtype": "Link", "label": "Warehouse", "options": "MP Warehouse", "reqd": 1},
            {"fieldname": "stock_section", "fieldtype": "Section Break", "label": "Stock Details"},
            {"fieldname": "actual_qty", "fieldtype": "Float", "label": "Actual Qty", "reqd": 1},
            {"fieldname": "qty_after_transaction", "fieldtype": "Float", "label": "Qty After Transaction", "read_only": 1},
            {"fieldname": "column_break_2", "fieldtype": "Column Break"},
            {"fieldname": "valuation_rate", "fieldtype": "Currency", "label": "Valuation Rate"},
            {"fieldname": "stock_value", "fieldtype": "Currency", "label": "Stock Value", "read_only": 1},
            {"fieldname": "reference_section", "fieldtype": "Section Break", "label": "Reference"},
            {"fieldname": "voucher_type", "fieldtype": "Link", "label": "Voucher Type", "options": "DocType"},
            {"fieldname": "voucher_no", "fieldtype": "Dynamic Link", "label": "Voucher No", "options": "voucher_type"},
            {"fieldname": "column_break_3", "fieldtype": "Column Break"},
            {"fieldname": "stock_uom", "fieldtype": "Link", "label": "Stock UOM", "options": "UOM", "default": "Nos"},
            {"fieldname": "remarks", "fieldtype": "Small Text", "label": "Remarks"},
        ],
        "is_submittable": 1
    },
}

def create_doctype_files(doctype_folder, doctype_info):
    """Create doctype JSON and Python files"""

    # Create __init__.py
    init_file = doctype_folder / "__init__.py"
    with open(init_file, 'w') as f:
        f.write(f"# {doctype_info['name']} DocType\n")

    # Create JSON file
    json_file = doctype_folder / f"{doctype_folder.name}.json"

    # Build field_order
    field_order = [field["fieldname"] for field in doctype_info["fields"]]

    doctype_json = {
        "actions": [],
        "allow_rename": 1,
        "autoname": doctype_info.get("autoname", "hash"),
        "creation": "2026-03-13 00:00:00.000000",
        "doctype": "DocType",
        "editable_grid": 1,
        "engine": "InnoDB",
        "field_order": field_order,
        "fields": doctype_info["fields"],
        "links": [],
        "modified": "2026-03-13 00:00:00.000000",
        "modified_by": "Administrator",
        "module": doctype_info["module"],
        "name": doctype_info["name"],
        "naming_rule": "By fieldname" if "field:" in doctype_info.get("autoname", "") else "Autoincrement",
        "owner": "Administrator",
        "permissions": [
            {
                "create": 1,
                "delete": 1,
                "email": 1,
                "export": 1,
                "print": 1,
                "read": 1,
                "report": 1,
                "role": "System Manager",
                "share": 1,
                "write": 1
            },
            {
                "create": 1,
                "delete": 1,
                "email": 1,
                "export": 1,
                "print": 1,
                "read": 1,
                "report": 1,
                "role": "MP Manager",
                "share": 1,
                "write": 1
            },
            {
                "create": 1,
                "email": 1,
                "export": 1,
                "print": 1,
                "read": 1,
                "report": 1,
                "role": "MP User",
                "share": 1,
                "write": 1
            }
        ],
        "sort_field": "modified",
        "sort_order": "DESC",
        "states": [],
        "track_changes": 1
    }

    if doctype_info.get("is_submittable"):
        doctype_json["is_submittable"] = 1

    with open(json_file, 'w') as f:
        json.dump(doctype_json, f, indent=1)

    # Create Python controller file
    py_file = doctype_folder / f"{doctype_folder.name}.py"
    class_name = "".join([word.capitalize() for word in doctype_info["name"].split()])

    py_content = f'''# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class {class_name}(Document):
\tpass
'''

    with open(py_file, 'w') as f:
        f.write(py_content)

    print(f"Created {doctype_info['name']}")

def main():
    """Main function to create all doctypes"""
    for folder_name, doctype_info in DOCTYPES.items():
        doctype_folder = BASE_PATH / folder_name
        doctype_folder.mkdir(parents=True, exist_ok=True)
        create_doctype_files(doctype_folder, doctype_info)

    print(f"\nCreated {len(DOCTYPES)} doctypes successfully!")

if __name__ == "__main__":
    main()
