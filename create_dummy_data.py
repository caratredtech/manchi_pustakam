#!/usr/bin/env python3
"""Create dummy data for Manchi Pustakam"""

import frappe
from frappe.utils import today, add_days, nowdate

def create_warehouses():
    """Create warehouse master data"""
    warehouses = [
        {
            "warehouse_name": "Nagole",
            "warehouse_type": "Bulk Storage",
            "address": "Plot No. 123, Industrial Area, Nagole, Hyderabad",
            "city": "Hyderabad",
            "contact_person": "Ravi Kumar",
            "phone": "+91 9876543210",
            "email": "nagole@manchipustakam.com",
            "is_active": 1
        },
        {
            "warehouse_name": "Tarnaka",
            "warehouse_type": "Display/Retail",
            "address": "Shop No. 45, Main Road, Tarnaka, Hyderabad",
            "city": "Hyderabad",
            "contact_person": "Lakshmi Devi",
            "phone": "+91 9876543211",
            "email": "tarnaka@manchipustakam.com",
            "is_active": 1
        }
    ]

    for wh in warehouses:
        if not frappe.db.exists("MP Warehouse", wh["warehouse_name"]):
            doc = frappe.get_doc({
                "doctype": "MP Warehouse",
                **wh
            })
            doc.insert(ignore_permissions=True)
            print(f"✓ Created warehouse: {wh['warehouse_name']}")

def create_suppliers():
    """Create supplier master data"""
    suppliers = [
        {
            "supplier_name": "Deccan Press",
            "supplier_type": "Printer (Deccan Press)",
            "email": "orders@deccanpress.com",
            "mobile_no": "+91 9876543220",
            "phone": "+91 40-12345678",
            "contact_person": "Suresh Reddy",
            "designation": "Sales Manager",
            "address": "Industrial Estate, Balanagar, Hyderabad - 500037",
            "payment_terms": "30 Days Credit",
            "default_payment_method": "Bank Transfer",
            "credit_period_days": 30,
            "pan_no": "AABCD1234E",
            "gstin": "36AABCD1234E1Z5",
            "gst_category": "Registered Regular",
            "tds_applicable": 0,
            "is_active": 1
        },
        {
            "supplier_name": "Tulika Publishers",
            "supplier_type": "Distributor",
            "email": "sales@tulikapublishers.com",
            "mobile_no": "+91 9876543221",
            "phone": "+91 11-12345678",
            "contact_person": "Radhika Menon",
            "designation": "Distribution Head",
            "address": "44 Shahpur Jat, New Delhi - 110049",
            "payment_terms": "15 Days Credit",
            "default_payment_method": "Bank Transfer",
            "credit_period_days": 15,
            "pan_no": "AABCT5678F",
            "gstin": "07AABCT5678F1Z3",
            "gst_category": "Registered Regular",
            "tds_applicable": 0,
            "is_active": 1
        },
        {
            "supplier_name": "Pratham Books",
            "supplier_type": "Publisher",
            "email": "orders@prathambooks.org",
            "mobile_no": "+91 9876543222",
            "phone": "+91 80-12345678",
            "contact_person": "Gautam John",
            "designation": "Sales Director",
            "address": "80 Feet Road, Koramangala, Bangalore - 560034",
            "payment_terms": "30 Days Credit",
            "default_payment_method": "Bank Transfer",
            "credit_period_days": 30,
            "pan_no": "AABCP9012G",
            "gstin": "29AABCP9012G1Z8",
            "gst_category": "Registered Regular",
            "tds_applicable": 0,
            "is_active": 1
        }
    ]

    for sup in suppliers:
        if not frappe.db.exists("MP Supplier", sup["supplier_name"]):
            doc = frappe.get_doc({
                "doctype": "MP Supplier",
                **sup
            })
            doc.insert(ignore_permissions=True)
            print(f"✓ Created supplier: {sup['supplier_name']}")

def create_customers():
    """Create customer master data"""
    customers = [
        {
            "customer_name": "Little Stars School",
            "customer_type": "Institutional",
            "customer_group": "Schools",
            "email": "library@littlestars.edu",
            "mobile_no": "+91 9876543230",
            "phone": "+91 40-23456789",
            "primary_contact_person": "Mrs. Prema Kumar",
            "designation": "Librarian",
            "billing_address": "Little Stars School, Jubilee Hills, Hyderabad - 500033",
            "shipping_address": "Little Stars School, Jubilee Hills, Hyderabad - 500033",
            "credit_allowed": 1,
            "credit_limit": 50000,
            "credit_period_days": 30,
            "default_price_list": "Institutional",
            "default_discount_percent": 15,
            "allow_special_discount": 1,
            "maximum_discount_percent": 20,
            "gst_category": "Registered Regular",
            "pan_no": "AABCS1234H",
            "gstin": "36AABCS1234H1Z9",
            "territory": "Telangana",
            "is_active": 1
        },
        {
            "customer_name": "Bright Minds Academy",
            "customer_type": "Institutional",
            "customer_group": "Schools",
            "email": "principal@brightminds.edu",
            "mobile_no": "+91 9876543231",
            "phone": "+91 40-23456790",
            "primary_contact_person": "Dr. Ramesh Rao",
            "designation": "Principal",
            "billing_address": "Bright Minds Academy, Banjara Hills, Hyderabad - 500034",
            "shipping_address": "Bright Minds Academy, Banjara Hills, Hyderabad - 500034",
            "credit_allowed": 1,
            "credit_limit": 75000,
            "credit_period_days": 45,
            "default_price_list": "Institutional",
            "default_discount_percent": 20,
            "allow_special_discount": 1,
            "maximum_discount_percent": 25,
            "gst_category": "Registered Regular",
            "pan_no": "AABCB5678I",
            "gstin": "36AABCB5678I1Z7",
            "territory": "Telangana",
            "is_active": 1
        },
        {
            "customer_name": "City Public Library",
            "customer_type": "Institutional",
            "customer_group": "Libraries",
            "email": "acquisitions@citylibrary.org",
            "mobile_no": "+91 9876543232",
            "phone": "+91 40-23456791",
            "primary_contact_person": "Smt. Vidya Devi",
            "designation": "Chief Librarian",
            "billing_address": "City Public Library, Abids, Hyderabad - 500001",
            "shipping_address": "City Public Library, Abids, Hyderabad - 500001",
            "credit_allowed": 1,
            "credit_limit": 100000,
            "credit_period_days": 60,
            "default_price_list": "Institutional",
            "default_discount_percent": 25,
            "allow_special_discount": 1,
            "maximum_discount_percent": 30,
            "gst_category": "Registered Regular",
            "pan_no": "AABCC9012J",
            "gstin": "36AABCC9012J1Z5",
            "territory": "Telangana",
            "is_active": 1
        },
        {
            "customer_name": "Walk-in Customer",
            "customer_type": "Retail",
            "customer_group": "Individual",
            "email": "retail@manchipustakam.com",
            "mobile_no": "+91 9876543233",
            "billing_address": "Tarnaka Store, Hyderabad",
            "shipping_address": "Tarnaka Store, Hyderabad",
            "credit_allowed": 0,
            "default_price_list": "Counter Sales (10% Off)",
            "default_discount_percent": 10,
            "allow_special_discount": 0,
            "territory": "Telangana",
            "is_active": 1
        },
        {
            "customer_name": "Regular Customer - Arjun Reddy",
            "customer_type": "Regular & Assured",
            "customer_group": "Individual",
            "email": "arjun.reddy@email.com",
            "mobile_no": "+91 9876543234",
            "billing_address": "Flat 101, Green Park, Kondapur, Hyderabad - 500084",
            "shipping_address": "Flat 101, Green Park, Kondapur, Hyderabad - 500084",
            "credit_allowed": 1,
            "credit_limit": 10000,
            "credit_period_days": 15,
            "default_price_list": "Standard Selling",
            "default_discount_percent": 10,
            "allow_special_discount": 0,
            "territory": "Telangana",
            "is_active": 1
        }
    ]

    for cust in customers:
        if not frappe.db.exists("MP Customer", cust["customer_name"]):
            doc = frappe.get_doc({
                "doctype": "MP Customer",
                **cust
            })
            doc.insert(ignore_permissions=True)
            print(f"✓ Created customer: {cust['customer_name']}")

def create_books():
    """Create book master data"""
    books = [
        # Primary Books (Published by Manchi Pustakam)
        {
            "book_code": "MP-001",
            "book_title": "చిన్ని పిట్టల కథలు (Little Bird Stories)",
            "isbn": "978-81-1234-001-5",
            "author": "వెంకటేశ్వర రావు",
            "language": "Telugu",
            "edition": "2nd Edition",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Stories",
            "age_group": "4-6 years",
            "category": "Story Books",
            "is_active": 1,
            "standard_selling_price": 150,
            "standard_buying_price": 75,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 100,
            "reorder_qty": 200,
            "preferred_supplier": "Deccan Press",
            "supplier_lead_time_days": 7,
            "is_book_set": 0
        },
        {
            "book_code": "MP-002",
            "book_title": "వర్ణమాల ఆటలు (Alphabet Games)",
            "isbn": "978-81-1234-002-2",
            "author": "లక్ష్మీ దేవి",
            "language": "Telugu",
            "edition": "1st Edition",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Learning",
            "age_group": "0-3 years",
            "category": "Educational",
            "is_active": 1,
            "standard_selling_price": 120,
            "standard_buying_price": 60,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 100,
            "reorder_qty": 250,
            "preferred_supplier": "Deccan Press",
            "supplier_lead_time_days": 7,
            "is_book_set": 0
        },
        {
            "book_code": "MP-003",
            "book_title": "ఎలుకల రాజు (The Mouse King)",
            "isbn": "978-81-1234-003-9",
            "author": "రాధా కృష్ణ",
            "language": "Telugu",
            "edition": "3rd Edition",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Adventure",
            "age_group": "7-9 years",
            "category": "Story Books",
            "is_active": 1,
            "standard_selling_price": 180,
            "standard_buying_price": 90,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 100,
            "reorder_qty": 150,
            "preferred_supplier": "Deccan Press",
            "supplier_lead_time_days": 7,
            "is_book_set": 0
        },
        {
            "book_code": "MP-004",
            "book_title": "సైన్స్ మేజిక్ (Science Magic)",
            "isbn": "978-81-1234-004-6",
            "author": "సుధాకర్ రెడ్డి",
            "language": "Telugu",
            "edition": "1st Edition",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Science",
            "age_group": "10-12 years",
            "category": "Educational",
            "is_active": 1,
            "standard_selling_price": 250,
            "standard_buying_price": 125,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 100,
            "reorder_qty": 150,
            "preferred_supplier": "Deccan Press",
            "supplier_lead_time_days": 10,
            "is_book_set": 0
        },
        {
            "book_code": "MP-005",
            "book_title": "కథల పిట్ట (Story Bird) - Activity Book",
            "isbn": "978-81-1234-005-3",
            "author": "మంచి పుస్తకం టీం",
            "language": "Telugu",
            "edition": "1st Edition",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Activities",
            "age_group": "4-6 years",
            "category": "Activity Books",
            "is_active": 1,
            "standard_selling_price": 200,
            "standard_buying_price": 100,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 100,
            "reorder_qty": 200,
            "preferred_supplier": "Deccan Press",
            "supplier_lead_time_days": 7,
            "is_book_set": 0
        },
        # Secondary Books (from other publishers)
        {
            "book_code": "TUL-001",
            "book_title": "The Blue Jackal",
            "isbn": "978-81-8146-456-7",
            "author": "Amar Chitra Katha",
            "language": "English",
            "edition": "Reprint",
            "publisher_type": "Secondary (Other Publishers)",
            "subject": "Folk Tales",
            "age_group": "7-9 years",
            "category": "Story Books",
            "is_active": 1,
            "standard_selling_price": 100,
            "standard_buying_price": 60,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 10,
            "reorder_qty": 20,
            "preferred_supplier": "Tulika Publishers",
            "supplier_lead_time_days": 14,
            "is_book_set": 0
        },
        {
            "book_code": "TUL-002",
            "book_title": "Following My Paintbrush",
            "isbn": "978-81-8146-987-6",
            "author": "Dulari Devi",
            "language": "English",
            "edition": "1st Edition",
            "publisher_type": "Secondary (Other Publishers)",
            "subject": "Art",
            "age_group": "10-12 years",
            "category": "Reference",
            "is_active": 1,
            "standard_selling_price": 350,
            "standard_buying_price": 210,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 10,
            "reorder_qty": 15,
            "preferred_supplier": "Tulika Publishers",
            "supplier_lead_time_days": 14,
            "is_book_set": 0
        },
        {
            "book_code": "PRA-001",
            "book_title": "Sion Misfortune",
            "isbn": "978-93-5046-123-4",
            "author": "Pratham Books",
            "language": "English",
            "edition": "1st Edition",
            "publisher_type": "Secondary (Other Publishers)",
            "subject": "Adventure",
            "age_group": "7-9 years",
            "category": "Story Books",
            "is_active": 1,
            "standard_selling_price": 80,
            "standard_buying_price": 48,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 10,
            "reorder_qty": 25,
            "preferred_supplier": "Pratham Books",
            "supplier_lead_time_days": 10,
            "is_book_set": 0
        },
        {
            "book_code": "PRA-002",
            "book_title": "The Clever Tailor",
            "isbn": "978-93-5046-234-7",
            "author": "Pratham Books",
            "language": "English",
            "edition": "2nd Edition",
            "publisher_type": "Secondary (Other Publishers)",
            "subject": "Folk Tales",
            "age_group": "4-6 years",
            "category": "Story Books",
            "is_active": 1,
            "standard_selling_price": 90,
            "standard_buying_price": 54,
            "currency": "INR",
            "gst_rate": 0,
            "is_stock_item": 1,
            "default_unit_of_measure": "Nos",
            "reorder_level": 10,
            "reorder_qty": 20,
            "preferred_supplier": "Pratham Books",
            "supplier_lead_time_days": 10,
            "is_book_set": 0
        },
        {
            "book_code": "WS-001",
            "book_title": "Storytelling Workshop - 2 Hours",
            "author": "Manchi Pustakam Team",
            "language": "Telugu/English",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Workshop",
            "age_group": "Adult",
            "category": "Workshop Material",
            "is_active": 1,
            "standard_selling_price": 5000,
            "currency": "INR",
            "gst_rate": 18,
            "is_stock_item": 0,
            "default_unit_of_measure": "Nos",
            "is_book_set": 0
        }
    ]

    for book in books:
        if not frappe.db.exists("Book", book["book_code"]):
            doc = frappe.get_doc({
                "doctype": "Book",
                **book
            })
            doc.insert(ignore_permissions=True)
            print(f"✓ Created book: {book['book_code']} - {book['book_title']}")

def run_all():
    """Run all data creation functions"""
    print("\n=== Creating Dummy Data for Manchi Pustakam ===\n")

    print("1. Creating Warehouses...")
    create_warehouses()
    frappe.db.commit()

    print("\n2. Creating Suppliers...")
    create_suppliers()
    frappe.db.commit()

    print("\n3. Creating Customers...")
    create_customers()
    frappe.db.commit()

    print("\n4. Creating Books...")
    create_books()
    frappe.db.commit()

    print("\n✅ All dummy data created successfully!")
    print("\nNext: Create sample transactions (quotations, invoices, etc.)")

if __name__ == "__main__":
    run_all()
