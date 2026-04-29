import frappe
from frappe.utils import flt
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry

@frappe.whitelist()
def create_transaction(doc, method=None):
    if doc.docstatus != 1:
        return

    if doc.custom_mode_of_payment == "Credit":
        return

    if flt(doc.outstanding_amount) <= 0:
        return

    if frappe.db.exists("Payment Entry Reference", {
        "reference_name": doc.name,
        "reference_doctype": "Sales Invoice"
    }):
        return

    pe = get_payment_entry("Sales Invoice", doc.name)

    pe.paid_amount = flt(doc.outstanding_amount)
    pe.received_amount = flt(doc.outstanding_amount)
    pe.mode_of_payment = doc.custom_mode_of_payment
    pe.reference_no = doc.name
    pe.reference_date = doc.posting_date

    for ref in pe.references:
        ref.allocated_amount = flt(doc.outstanding_amount)

    pe.insert(ignore_permissions=True)
    pe.submit()
    doc.reload()