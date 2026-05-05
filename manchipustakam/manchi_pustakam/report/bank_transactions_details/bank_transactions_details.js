// Copyright (c) 2026, caratRED and contributors
// For license information, please see license.txt

frappe.query_reports["Bank Transactions Details"] = {
	filters: [
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.month_start()
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: frappe.datetime.month_end()
		},
		{
			fieldname: "bank_account",
			label: __("Bank Account"),
			fieldtype: "Link",
			options: "Bank Account"
		},
		{
			fieldname: "transaction_type",
			label: __("Transaction Type"),
			fieldtype: "Select",
			options: "\nDeposit\nWithdrawal"
		}
	],
};
