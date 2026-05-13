import frappe


def execute():
    states = {
        "Draft": "Red",
        "Submitted": "Blue",
        "Unpaid": "Orange",
        "Paid": "Green",
        "Return": "Gray",
        "Credit Note Issued": "Gray",
        "Unpaid and Discounted": "Orange",
        "Partly Paid and Discounted": "Yellow",
        "Overdue and Discounted": "Red",
        "Overdue": "Red",
        "Partly Paid": "Yellow",
        "Internal Transfer": "Gray",
        "Cancelled": "Red",
    }

    existing_states = frappe.get_all(
        "DocType State",
        filters={"parent": "Sales Invoice", "parentfield": "states", "parenttype": "DocType"},
        pluck="title",
    )

    for idx, (title, color) in enumerate(states.items(), 1):
        if title in existing_states:
            frappe.db.set_value(
                "DocType State",
                {
                    "parent": "Sales Invoice",
                    "parentfield": "states",
                    "parenttype": "DocType",
                    "title": title,
                },
                {"color": color, "custom": 0, "idx": idx},
            )
            continue

        frappe.get_doc(
            {
                "doctype": "DocType State",
                "parent": "Sales Invoice",
                "parentfield": "states",
                "parenttype": "DocType",
                "title": title,
                "color": color,
                "custom": 0,
                "idx": idx,
            }
        ).insert()

    frappe.clear_cache(doctype="Sales Invoice")
