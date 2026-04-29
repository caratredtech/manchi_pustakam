# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	return [
		{"label": "Book", "fieldname": "book", "fieldtype": "Link", "options": "Book", "width": 120},
		{"label": "Title", "fieldname": "book_title", "fieldtype": "Data", "width": 200},
		{"label": "Current Stock", "fieldname": "current_stock", "fieldtype": "Float", "width": 120},
		{"label": "Reorder Level", "fieldname": "reorder_level", "fieldtype": "Int", "width": 120},
		{"label": "Reorder Qty", "fieldname": "reorder_qty", "fieldtype": "Int", "width": 120},
		{"label": "Supplier", "fieldname": "preferred_supplier", "fieldtype": "Link", "options": "MP Supplier", "width": 150},
		{"label": "Supplier Contact", "fieldname": "supplier_phone", "fieldtype": "Data", "width": 120},
		{"label": "Lead Time", "fieldname": "supplier_lead_time_days", "fieldtype": "Int", "width": 100}
	]

def get_data(filters):
	query = """
		SELECT
			b.name as book,
			b.book_title,
			0 as current_stock,
			b.reorder_level,
			b.reorder_qty,
			b.preferred_supplier,
			s.phone as supplier_phone,
			b.supplier_lead_time_days
		FROM `tabBook` b
		LEFT JOIN `tabMP Supplier` s ON b.preferred_supplier = s.name
		WHERE b.is_stock_item = 1
			AND b.is_active = 1
		ORDER BY b.book_title
	"""

	return frappe.db.sql(query, as_dict=1)
