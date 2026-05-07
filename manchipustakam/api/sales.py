import frappe
from frappe.utils import flt
from frappe.utils.data import money_in_words
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_sales_invoice_data(doc, method=None):
    if doc.docstatus != 0:
        return

    if not doc.cost_center and doc.company:
        doc.cost_center = frappe.db.get_value("Company", doc.company, "cost_center")

    doc.taxes = [
        d for d in doc.taxes
        if d.account_head != "Miscellaneous Expenses - M"
    ]

    base_total = flt(doc.total) - flt(doc.discount_amount)

    net_total = base_total
    grand_total = base_total

    if doc.custom_other_charges:
        charges = flt(doc.custom_other_charges)
        net_total += charges
        grand_total += charges

        doc.append("taxes", {
            "charge_type": "Actual",
            "account_head": "Miscellaneous Expenses - M",
            "description": "Other Charges",
            "tax_amount": charges,
            "cost_center": doc.cost_center or "Main - M"
        })

    doc.run_method("calculate_taxes_and_totals")

    rounded_total = round(grand_total + flt(doc.rounding_adjustment))
    outstanding_amount = rounded_total

    conversion_rate = flt(doc.conversion_rate) or 1

    base_grand_total = grand_total * conversion_rate
    base_rounded_total = rounded_total * conversion_rate

    doc.net_total = flt(net_total)
    doc.grand_total = flt(grand_total)
    doc.rounded_total = flt(rounded_total)
    doc.outstanding_amount = flt(outstanding_amount)

    doc.base_grand_total = flt(base_grand_total)
    doc.base_rounded_total = flt(base_rounded_total)

    doc.in_words = money_in_words(rounded_total)
    doc.base_in_words = money_in_words(base_rounded_total)

    if not doc.has_value_changed("custom_amount_paid"):
        doc.custom_amount_paid = flt(outstanding_amount)
        
        
@frappe.whitelist()
def get_quotation_data(doc, method=None):
    if doc.docstatus != 0:
        return

    if hasattr(doc, "taxes"):
        doc.taxes = [
            d for d in doc.taxes
            if d.account_head != "Miscellaneous Expenses - M"
        ]

    base_total = flt(doc.get("total")) - flt(doc.get("discount_amount"))
    net_total = base_total
    grand_total = base_total

    if doc.get("custom_other_charges"):
        charges = flt(doc.get("custom_other_charges"))
        net_total += charges
        grand_total += charges

        if hasattr(doc, "taxes"):
            doc.append("taxes", {
                "charge_type": "Actual",
                "account_head": "Miscellaneous Expenses - M",
                "description": "Other Charges",
                "tax_amount": charges
            })

    doc.run_method("calculate_taxes_and_totals")

    rounded_total = round(grand_total + flt(doc.get("rounding_adjustment")))
    conversion_rate = flt(doc.get("conversion_rate")) or 1

    doc.net_total = flt(net_total)
    doc.grand_total = flt(grand_total)
    doc.rounded_total = flt(rounded_total)
    doc.base_grand_total = flt(grand_total * conversion_rate)
    doc.base_rounded_total = flt(rounded_total * conversion_rate)
    doc.in_words = money_in_words(rounded_total)
    doc.base_in_words = money_in_words(doc.base_rounded_total)
    
    
@frappe.whitelist()
def get_purchase_invoice_data(doc, method=None):
    if doc.docstatus != 0:
        return

    doc.taxes = [
        d for d in doc.get("taxes", [])
        if d.account_head != "Miscellaneous Expenses - M"
    ]

    if doc.get("custom_other_charges"):
        charges = flt(doc.get("custom_other_charges"))

        doc.append("taxes", {
            "charge_type": "Actual",
            "account_head": "Miscellaneous Expenses - M",
            "description": "Other Charges",
            "tax_amount": charges,
            "category": "Total",
            "add_deduct_tax": "Add",
            "included_in_print_rate": 0
        })

    doc.run_method("calculate_taxes_and_totals")

    rounded_total = round(doc.grand_total + flt(doc.rounding_adjustment or 0))
    doc.rounded_total = flt(rounded_total)
    doc.in_words = money_in_words(doc.rounded_total)
    doc.base_rounded_total = flt(doc.rounded_total * (doc.conversion_rate or 1))
    doc.base_in_words = money_in_words(doc.base_rounded_total)

@frappe.whitelist()
def make_sales_invoice(docname):
    def set_missing_values(source, target):
        target.customer = source.party_name
        target.currency = source.currency
        target.custom_quotation = source.name

        for item in target.items:
            if not item.income_account:
                item.income_account = frappe.db.get_value(
                    "Item Default",
                    {"parent": item.item_code, "company": target.company},
                    "income_account"
                ) or frappe.db.get_value(
                    "Company",
                    target.company,
                    "default_income_account"
                )

    doc = get_mapped_doc("Quotation", docname, {
        "Quotation": {
            "doctype": "Sales Invoice",
            "field_map": {
                "party_name": "customer",
                "company": "company",
                "currency": "currency"
            }
        },
        "Quotation Item": {
            "doctype": "Sales Invoice Item",
            "field_map": {
                "name": "quotation_item",
                "parent": "quotation",
                "qty": "qty",
                "rate": "rate",
                "uom": "uom"
            }
        },
        "Sales Taxes and Charges": {
            "doctype": "Sales Taxes and Charges"
        }
    }, None, set_missing_values)

    return doc


def update_quotation_status_on_sales_invoice_submit(doc, method=None):
    if doc.docstatus != 1:
        return

    if doc.custom_quotation:
        frappe.db.set_value("Quotation", doc.custom_quotation, "status", "Ordered")
        quotation = frappe.get_doc("Quotation", doc.custom_quotation)
        quotation.reload()