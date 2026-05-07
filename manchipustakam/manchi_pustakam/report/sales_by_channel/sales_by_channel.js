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
			fieldtype: "Link",
			options: "Sales Channel",
			default: ""
		},
		{
			fieldname: "customer",
			label: "Customer",
			fieldtype: "Link",
			options: "Customer"
		},
		{
			fieldname: "customer_type",
			label: "Customer Type",
			fieldtype: "Select",
			options: "\nIndividual\nIndividual Donor\nInstitution\nInstitutional Donor"
		},
		{
			fieldname: "customer_group",
			label: "Customer Group",
			fieldtype: "Link",
			options: "Customer Group"
		}
	]
};
