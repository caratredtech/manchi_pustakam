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
    pe.reference_no = doc.custom_reference_id or doc.name
    pe.reference_date = doc.posting_date
    pe.set_remarks()

    for ref in pe.references:
        ref.allocated_amount = flt(doc.outstanding_amount)

    pe.insert(ignore_permissions=True)
    pe.submit()
    doc.reload()

    if flt(doc.outstanding_amount) <= 0:
        for schedule in doc.payment_schedule:
            frappe.db.set_value(
                "Payment Schedule",
                schedule.name,
                {
                    "paid_amount": schedule.payment_amount,
                    "outstanding": 0,
                    "base_paid_amount": schedule.base_payment_amount,
                    "base_outstanding": 0,
                },
                update_modified=False,
            )

    doc.set_status(update=True)
    doc.reload()
    doc.notify_update()


def update_payment_reference_id(doc, method=None):
    if doc.docstatus != 1:
        return

    reference_no = doc.custom_reference_id or doc.name
    payment_entries = frappe.get_all(
        "Payment Entry Reference",
        filters={
            "reference_doctype": "Sales Invoice",
            "reference_name": doc.name,
            "parenttype": "Payment Entry",
        },
        pluck="parent",
    )

    for payment_entry_name in set(payment_entries):
        payment_entry = frappe.get_doc("Payment Entry", payment_entry_name)

        if payment_entry.docstatus == 2:
            continue

        payment_entry.reference_no = reference_no
        payment_entry.set_remarks()

        frappe.db.set_value(
            "Payment Entry",
            payment_entry.name,
            {
                "reference_no": reference_no,
                "remarks": payment_entry.remarks,
            },
        )
