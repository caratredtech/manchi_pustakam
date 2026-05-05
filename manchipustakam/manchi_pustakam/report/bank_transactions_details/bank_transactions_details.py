# Copyright (c) 2026, caratRED and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	filters = filters or {}
	columns = get_columns()
	data = get_data(filters)
	report_summary = get_report_summary(data)

	return columns, data, None, None, report_summary


def get_columns() -> list[dict]:
	return [
		{"label": _("Date"), "fieldname": "date", "fieldtype": "Date", "width": 110},
		{"label": _("Bank Account"), "fieldname": "bank_account", "fieldtype": "Link", "options": "Bank Account", "width": 220},
		# {"label": _("Branch"), "fieldname": "branch", "fieldtype": "Data", "width": 120},
		# {"label": _("Account Type"), "fieldname": "account_type", "fieldtype": "Data", "width": 120},
		{"label": _("Tran Id"), "fieldname": "tran_id", "fieldtype": "Data", "width": 130},
		{"label": _("UTR Number"), "fieldname": "utr_number", "fieldtype": "Data", "width": 150},
		{"label": _("Instr. Id"), "fieldname": "instr_id", "fieldtype": "Data", "width": 130},
		{"label": _("Withdrawals"), "fieldname": "withdrawals", "fieldtype": "Currency", "options": "currency", "width": 130},
		{"label": _("Deposits"), "fieldname": "deposits", "fieldtype": "Currency", "options": "currency", "width": 130},
		{"label": _("Statement Balance"), "fieldname": "balance", "fieldtype": "Currency", "options": "currency", "width": 150},
		{"label": _("Remarks"), "fieldname": "remarks", "fieldtype": "Small Text", "width": 220},
		{"label": _("Bank Particulars"), "fieldname": "bank_particulars", "fieldtype": "Data", "width": 180},
		{"label": _("Payment/Receipt/Contra"), "fieldname": "paymentreceiptcontra", "fieldtype": "Data", "width": 180},
		{"label": _("Paid to/Received from"), "fieldname": "paid_toreceived_from", "fieldtype": "Data", "width": 200},
		{"label": _("Narration"), "fieldname": "narration", "fieldtype": "Small Text", "width": 240},
		{"label": _("Amount"), "fieldname": "amount", "fieldtype": "Currency", "options": "currency", "width": 130},
		{"label": _("Balance Amount"), "fieldname": "balance_amount", "fieldtype": "Currency", "options": "currency", "width": 150},
		{"label": _("Bank Name/Cash"), "fieldname": "bank_name_cash", "fieldtype": "Data", "width": 160},
		{"label": _("Second Ledger Name"), "fieldname": "second_ledger_name", "fieldtype": "Data", "width": 180}
		# {"label": _("Currency"), "fieldname": "currency", "fieldtype": "Link", "options": "Currency", "width": 90},
		# {"label": _("Document"), "fieldname": "name", "fieldtype": "Link", "options": "Bank Statement", "width": 130},
	]


def get_data(filters: dict) -> list[dict]:
	conditions = ["docstatus < 2"]
	values = {}

	if filters.get("from_date"):
		conditions.append("`date` >= %(from_date)s")
		values["from_date"] = filters.get("from_date")

	if filters.get("to_date"):
		conditions.append("`date` <= %(to_date)s")
		values["to_date"] = filters.get("to_date")

	if filters.get("bank_account"):
		conditions.append("bank_account = %(bank_account)s")
		values["bank_account"] = filters.get("bank_account")

	if filters.get("transaction_type") == "Deposit":
		conditions.append("ifnull(deposits, 0) > 0")
	elif filters.get("transaction_type") == "Withdrawal":
		conditions.append("ifnull(withdrawals, 0) > 0")

	return frappe.db.sql(
		f"""
		SELECT
			name,
			bank_account,
			branch,
			account_type,
			currency,
			`date`,
			tran_id,
			utr_number,
			instr_id,
			withdrawals,
			deposits,
			balance,
			remarks,
			bank_particulars,
			paymentreceiptcontra,
			paid_toreceived_from,
			narration,
			amount,
			balance_amount,
			bank_name_cash,
			second_ledger_name
		FROM `tabBank Statement`
		WHERE {" AND ".join(conditions)}
		ORDER BY `date` DESC, creation DESC
		""",
		values,
		as_dict=1,
	)


def get_report_summary(data: list[dict]) -> list[dict]:
	total_deposits = sum(row.get("deposits") or 0 for row in data)
	total_withdrawals = sum(row.get("withdrawals") or 0 for row in data)
	closing_balance = data[0].get("balance") if data else 0
	currency = data[0].get("currency") if data else "INR"

	return [
		{
			"value": len(data),
			"label": _("Transactions"),
			"datatype": "Int",
			"indicator": "Blue",
		},
		{
			"value": total_deposits,
			"label": _("Total Deposits"),
			"datatype": "Currency",
			"currency": currency,
			"indicator": "Green",
		},
		{
			"value": total_withdrawals,
			"label": _("Total Withdrawals"),
			"datatype": "Currency",
			"currency": currency,
			"indicator": "Red",
		},
		{
			"value": closing_balance,
			"label": _("Total Balance"),
			"datatype": "Currency",
			"currency": currency,
			"indicator": "Blue",
		},
	]
