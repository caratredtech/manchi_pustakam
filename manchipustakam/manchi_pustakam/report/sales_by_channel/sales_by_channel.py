# Copyright (c) 2026, Manchi Pustakam and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	chart = get_chart_data(data)
	return columns, data, None, chart


def get_columns():
	return [
		{"label": "Invoice No", "fieldname": "sales_invoice", "fieldtype": "Link", "options": "Sales Invoice", "width": 150},
		{"label": "Customer", "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 180},
		{"label": "Customer Type", "fieldname": "customer_type", "fieldtype": "Data", "width": 130},
		{"label": "Customer Group", "fieldname": "customer_group", "fieldtype": "Link", "options": "Customer Group", "width": 150},
		{"label": "Sales Channel", "fieldname": "sales_channel", "fieldtype": "Link", "options": "Sales Channel", "width": 150},
		{"label": "Item", "fieldname": "item_name", "fieldtype": "Data", "width": 220},
		{"label": "Quantity", "fieldname": "qty", "fieldtype": "Float", "width": 120},
		{"label": "Rate", "fieldname": "rate", "fieldtype": "Currency", "width": 120},
		{"label": "Amount", "fieldname": "amount", "fieldtype": "Currency", "width": 120},
		{"label": "Discount Amount", "fieldname": "discount_amount", "fieldtype": "Currency", "width": 140},
		{"label": "Total Invoice Value", "fieldname": "total_invoice", "fieldtype": "Currency", "width": 150},
	]


def get_data(filters):
	conditions = []
	values = {}

	if filters.get("from_date"):
		conditions.append("si.posting_date >= %(from_date)s")
		values["from_date"] = filters.get("from_date")

	if filters.get("to_date"):
		conditions.append("si.posting_date <= %(to_date)s")
		values["to_date"] = filters.get("to_date")

	if filters.get("sales_channel"):
		conditions.append("si.custom_sales_channel = %(sales_channel)s")
		values["sales_channel"] = filters.get("sales_channel")

	if filters.get("customer"):
		conditions.append("si.customer = %(customer)s")
		values["customer"] = filters.get("customer")

	if filters.get("customer_type"):
		conditions.append("TRIM(c.customer_type) = TRIM(%(customer_type)s)")
		values["customer_type"] = filters.get("customer_type")

	if filters.get("customer_group"):
		conditions.append("c.customer_group = %(customer_group)s")
		values["customer_group"] = filters.get("customer_group")

	where_clause = " AND ".join(conditions) if conditions else "1=1"

	raw_data = frappe.db.sql(f"""
		SELECT
			si.name as sales_invoice,
			si.customer,
			c.customer_type,
			c.customer_group,
			si.custom_sales_channel as sales_channel,
			si.discount_amount,
			si.total_qty,
			si.total,
			si.grand_total,
			si.rounded_total,
			sii.item_name,
			sii.rate,
			sii.idx
		FROM `tabSales Invoice` si
		LEFT JOIN `tabCustomer` c
			ON c.name = si.customer
		LEFT JOIN `tabSales Invoice Item` sii
			ON sii.parent = si.name
		WHERE si.docstatus = 1 AND {where_clause}
		ORDER BY si.name, sii.idx
	""", values, as_dict=1)

	invoice_meta = {}
	last_item = {}

	for d in raw_data:

		inv = d.sales_invoice

		if inv not in invoice_meta:
			invoice_meta[inv] = {
				"sales_invoice": inv,
				"customer": d.customer,
				"customer_type": d.customer_type,
				"customer_group": d.customer_group,
				"sales_channel": d.sales_channel,
				"qty": d.total_qty or 0,
				"amount": d.total or 0,
				"discount_amount": d.discount_amount or 0,
				"total_invoice": d.rounded_total or 0
			}

		last_item[inv] = {
			"item_name": d.item_name,
			"rate": d.rate or 0
		}

	data = []

	for inv in last_item:
		meta = invoice_meta.get(inv, {})
		item = last_item.get(inv, {})

		data.append({
			"sales_invoice": meta.get("sales_invoice"),
			"customer": meta.get("customer"),
			"customer_type": meta.get("customer_type"),
			"customer_group": meta.get("customer_group"),
			"sales_channel": meta.get("sales_channel"),
			"item_name": item.get("item_name"),
			"qty": meta.get("qty"),
			"rate": item.get("rate"),
			"amount": meta.get("amount"),
			"discount_amount": meta.get("discount_amount"),
			"total_invoice": meta.get("total_invoice")
		})

	return data


def get_chart_data(data):
	if not data:
		return None

	channel_map = {}

	for d in data:
		channel = d.get("sales_channel") or "Others"
		channel_map[channel] = channel_map.get(channel, 0) + (d.get("total_invoice") or 0)

	return {
		"data": {
			"labels": list(channel_map.keys()),
			"datasets": [
				{
					"name": "Amount",
					"values": list(channel_map.values())
				}
			]
		},
		"type": "bar"
	}
