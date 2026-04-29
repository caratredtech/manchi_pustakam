// Copyright (c) 2026, caratRED and contributors
// For license information, please see license.txt

frappe.query_reports["Sales by Channel"] = {
	filters: [
		{
			fieldname: "from_date",
			label: "From Date",
			fieldtype: "Date",
			default: frappe.datetime.month_start()
		},
		{
			fieldname: "to_date",
			label: "To Date",
			fieldtype: "Date",
			default: frappe.datetime.month_end()
		},
		{
			fieldname: "sales_channel",
			label: "Sales Channel",
			fieldtype: "Select",
			options: "\nCounter Sales\nShopping Cart Sales\nExhibition Sales\nBulk/ Institutional Sales",
			default: ""
		},
		{
			fieldname: "customer",
			label: "Customer",
			fieldtype: "Link",
			options: "Customer"
		}
	]
};