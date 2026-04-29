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
		{"label": "Warehouse", "fieldname": "warehouse", "fieldtype": "Link", "options": "MP Warehouse", "width": 120},
		{"label": "Actual Qty", "fieldname": "actual_qty", "fieldtype": "Float", "width": 100},
		{"label": "Reserved Qty", "fieldname": "reserved_qty", "fieldtype": "Float", "width": 100},
		{"label": "Available Qty", "fieldname": "available_qty", "fieldtype": "Float", "width": 120},
		{"label": "Reorder Level", "fieldname": "reorder_level", "fieldtype": "Int", "width": 120},
		{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100}
	]

def get_data(filters):
	# Get all books
	books = frappe.get_all("Book", filters={"is_stock_item": 1}, fields=["name", "book_title", "reorder_level"])

	data = []
	for book in books:
		# Get stock for each warehouse
		warehouses = frappe.get_all("MP Warehouse", pluck="name")

		for warehouse in warehouses:
			# Calculate actual stock (simplified - would need real stock ledger aggregation)
			actual_qty = 0  # Would sum from Stock Ledger Entry

			# Calculate reserved qty from quotations
			reserved_qty = frappe.db.sql("""
				SELECT SUM(reserved_qty)
				FROM `tabMP Sales Quotation Item`
				WHERE book = %s AND warehouse = %s
				AND parenttype = 'MP Sales Quotation'
				AND parent IN (
					SELECT name FROM `tabMP Sales Quotation`
					WHERE docstatus = 1 AND status = 'Open' AND reserve_stock = 1
				)
			""", (book.name, warehouse))[0][0] or 0

			available_qty = actual_qty - reserved_qty

			# Determine status
			if available_qty <= 0:
				status = "Out of Stock"
				elif available_qty < book.reorder_level:
				status = "Low Stock"
			else:
				status = "In Stock"

			data.append({
				"book": book.name,
				"book_title": book.book_title,
				"warehouse": warehouse,
				"actual_qty": actual_qty,
				"reserved_qty": reserved_qty,
				"available_qty": available_qty,
				"reorder_level": book.reorder_level,
				"status": status
			})

	return data
