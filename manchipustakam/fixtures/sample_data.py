#!/usr/bin/env python3
"""
Sample data creation for Manchi Pustakam ERP
"""

import frappe

def create_sample_data():
    """Create sample master data for Manchi Pustakam"""

    frappe.set_user("Administrator")

    print("\n📦 Creating Sample Data for Manchi Pustakam...")

    # 1. Create Warehouses
    print("\n1️⃣  Creating Warehouses...")
    warehouses = [
        {
            "doctype": "MP Warehouse",
            "warehouse_name": "Nagole",
            "warehouse_type": "Bulk Storage",
            "address": "Plot No. 123, Industrial Area, Nagole, Hyderabad",
            "city": "Hyderabad",
            "state": "Telangana",
            "pincode": "500068",
            "contact_person": "Ravi Kumar",
            "phone": "+91 9876543210",
            "email": "nagole@manchipustakam.com",
            "is_active": 1
        },
        {
            "doctype": "MP Warehouse",
            "warehouse_name": "Tarnaka",
            "warehouse_type": "Display/Retail",
            "address": "Shop No. 45, Main Road, Tarnaka, Hyderabad",
            "city": "Hyderabad",
            "state": "Telangana",
            "pincode": "500017",
            "contact_person": "Lakshmi Devi",
            "phone": "+91 9876543211",
            "email": "tarnaka@manchipustakam.com",
            "is_active": 1
        }
    ]

    for wh_data in warehouses:
        if not frappe.db.exists("MP Warehouse", wh_data["warehouse_name"]):
            wh = frappe.get_doc(wh_data)
            wh.insert(ignore_permissions=True)
            print(f"   ✅ Created warehouse: {wh.warehouse_name}")
        else:
            print(f"   ⏭️  Warehouse already exists: {wh_data['warehouse_name']}")

    # 2. Create Suppliers
    print("\n2️⃣  Creating Suppliers...")
    suppliers = [
        {
            "doctype": "MP Supplier",
            "supplier_name": "Deccan Press",
            "supplier_type": "Printer (Deccan Press)",
            "email": "orders@deccanpress.com",
            "mobile_no": "+91 9876543220",
            "contact_person": "Suresh Reddy",
            "address_line_1": "Industrial Estate, Balanagar",
            "city": "Hyderabad",
            "state": "Telangana",
            "pincode": "500037",
            "payment_terms": "30 Days Credit",
            "credit_period_days": 30,
            "gstin": "36AABCD1234E1Z5",
            "is_active": 1
        },
        {
            "doctype": "MP Supplier",
            "supplier_name": "Tulika Publishers",
            "supplier_type": "Distributor",
            "email": "sales@tulikapublishers.com",
            "mobile_no": "+91 9876543221",
            "contact_person": "Radhika Menon",
            "address_line_1": "44 Shahpur Jat",
            "city": "New Delhi",
            "state": "Delhi",
            "pincode": "110049",
            "payment_terms": "15 Days Credit",
            "credit_period_days": 15,
            "gstin": "07AABCT5678F1Z3",
            "is_active": 1
        },
        {
            "doctype": "MP Supplier",
            "supplier_name": "Pratham Books",
            "supplier_type": "Publisher",
            "email": "orders@prathambooks.org",
            "mobile_no": "+91 9876543222",
            "contact_person": "Gautam John",
            "address_line_1": "80 Feet Road, Koramangala",
            "city": "Bangalore",
            "state": "Karnataka",
            "pincode": "560034",
            "payment_terms": "30 Days Credit",
            "credit_period_days": 30,
            "gstin": "29AABCP9012G1Z8",
            "is_active": 1
        }
    ]

    for sup_data in suppliers:
        if not frappe.db.exists("MP Supplier", sup_data["supplier_name"]):
            sup = frappe.get_doc(sup_data)
            sup.insert(ignore_permissions=True)
            print(f"   ✅ Created supplier: {sup.supplier_name}")
        else:
            print(f"   ⏭️  Supplier already exists: {sup_data['supplier_name']}")

    # 3. Create Customers
    print("\n3️⃣  Creating Customers...")
    customers = [
        {
            "doctype": "MP Customer",
            "customer_name": "Little Stars School",
            "customer_type": "Institutional",
            "customer_group": "Schools",
            "email": "library@littlestars.edu",
            "mobile_no": "+91 9876543230",
            "primary_contact": "Mrs. Prema Kumar",
            "designation": "Librarian",
            "billing_address_line_1": "Little Stars School, Jubilee Hills",
            "billing_city": "Hyderabad",
            "billing_state": "Telangana",
            "billing_pincode": "500033",
            "credit_allowed": 1,
            "credit_limit": 50000,
            "credit_period_days": 30,
            "default_discount_percentage": 15,
            "gstin": "36AABCS1234H1Z9",
            "territory": "Telangana",
            "is_active": 1
        },
        {
            "doctype": "MP Customer",
            "customer_name": "Walk-in Customer",
            "customer_type": "Retail",
            "customer_group": "Individual",
            "mobile_no": "+91 9876543233",
            "credit_allowed": 0,
            "default_discount_percentage": 10,
            "territory": "Telangana",
            "is_active": 1
        },
        {
            "doctype": "MP Customer",
            "customer_name": "City Public Library",
            "customer_type": "Institutional",
            "customer_group": "Libraries",
            "email": "acquisitions@citylibrary.org",
            "mobile_no": "+91 9876543232",
            "primary_contact": "Smt. Vidya Devi",
            "billing_address_line_1": "City Public Library, Abids",
            "billing_city": "Hyderabad",
            "billing_state": "Telangana",
            "billing_pincode": "500001",
            "credit_allowed": 1,
            "credit_limit": 100000,
            "credit_period_days": 60,
            "default_discount_percentage": 25,
            "gstin": "36AABCC9012J1Z5",
            "territory": "Telangana",
            "is_active": 1
        }
    ]

    for cust_data in customers:
        if not frappe.db.exists("MP Customer", cust_data["customer_name"]):
            cust = frappe.get_doc(cust_data)
            cust.insert(ignore_permissions=True)
            print(f"   ✅ Created customer: {cust.customer_name}")
        else:
            print(f"   ⏭️  Customer already exists: {cust_data['customer_name']}")

    # 4. Create Books
    print("\n4️⃣  Creating Books...")
    books = [
        {
            "doctype": "Book",
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
            "standard_selling_price": 150,
            "standard_buying_price": 75,
            "gst_rate": 0,
            "is_stock_item": 1,
            "reorder_level": 100,
            "reorder_qty": 200,
            "preferred_supplier": "Deccan Press",
            "is_active": 1
        },
        {
            "doctype": "Book",
            "book_code": "MP-002",
            "book_title": "వర్ణమాల ఆటలు (Alphabet Games)",
            "isbn": "978-81-1234-002-2",
            "author": "లక్ష్మీ దేవి",
            "language": "Telugu",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Learning",
            "age_group": "0-3 years",
            "category": "Educational",
            "standard_selling_price": 120,
            "standard_buying_price": 60,
            "gst_rate": 0,
            "is_stock_item": 1,
            "reorder_level": 100,
            "reorder_qty": 200,
            "preferred_supplier": "Deccan Press",
            "is_active": 1
        },
        {
            "doctype": "Book",
            "book_code": "MP-003",
            "book_title": "ఎలుకల రాజు (The Mouse King)",
            "isbn": "978-81-1234-003-9",
            "author": "రాధా కృష్ణ",
            "language": "Telugu",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Adventure",
            "age_group": "7-9 years",
            "category": "Story Books",
            "standard_selling_price": 180,
            "standard_buying_price": 90,
            "gst_rate": 0,
            "is_stock_item": 1,
            "reorder_level": 100,
            "reorder_qty": 200,
            "preferred_supplier": "Deccan Press",
            "is_active": 1
        },
        {
            "doctype": "Book",
            "book_code": "MP-004",
            "book_title": "సైన్స్ మేజిక్ (Science Magic)",
            "isbn": "978-81-1234-004-6",
            "author": "సుధాకర్ రెడ్డి",
            "language": "Telugu",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Science",
            "age_group": "10-12 years",
            "category": "Educational",
            "standard_selling_price": 250,
            "standard_buying_price": 125,
            "gst_rate": 0,
            "is_stock_item": 1,
            "reorder_level": 100,
            "reorder_qty": 200,
            "preferred_supplier": "Deccan Press",
            "is_active": 1
        },
        {
            "doctype": "Book",
            "book_code": "TUL-001",
            "book_title": "The Blue Jackal",
            "isbn": "978-81-8146-456-7",
            "author": "Amar Chitra Katha",
            "language": "English",
            "publisher_type": "Secondary (Other Publishers)",
            "subject": "Folk Tales",
            "age_group": "7-9 years",
            "category": "Story Books",
            "standard_selling_price": 100,
            "standard_buying_price": 60,
            "gst_rate": 0,
            "is_stock_item": 1,
            "reorder_level": 10,
            "reorder_qty": 20,
            "preferred_supplier": "Tulika Publishers",
            "is_active": 1
        },
        {
            "doctype": "Book",
            "book_code": "PRA-001",
            "book_title": "Sion Misfortune",
            "isbn": "978-93-5046-123-4",
            "author": "Pratham Books",
            "language": "English",
            "publisher_type": "Secondary (Other Publishers)",
            "subject": "Adventure",
            "age_group": "7-9 years",
            "category": "Story Books",
            "standard_selling_price": 80,
            "standard_buying_price": 48,
            "gst_rate": 0,
            "is_stock_item": 1,
            "reorder_level": 10,
            "reorder_qty": 20,
            "preferred_supplier": "Pratham Books",
            "is_active": 1
        },
        {
            "doctype": "Book",
            "book_code": "WS-001",
            "book_title": "Storytelling Workshop - 2 Hours",
            "author": "Manchi Pustakam Team",
            "language": "Telugu/English",
            "publisher_type": "Primary (Manchi Pustakam)",
            "subject": "Workshop",
            "age_group": "Adult",
            "category": "Workshop Material",
            "standard_selling_price": 5000,
            "gst_rate": 18,
            "is_stock_item": 0,  # Service item
            "is_active": 1
        }
    ]

    for book_data in books:
        if not frappe.db.exists("Book", book_data["book_code"]):
            book = frappe.get_doc(book_data)
            book.insert(ignore_permissions=True)
            print(f"   ✅ Created book: {book.book_code} - {book.book_title}")
        else:
            print(f"   ⏭️  Book already exists: {book_data['book_code']}")

    frappe.db.commit()

    print("\n✅ Sample data creation completed successfully!")
    print("\n📊 Summary:")
    print(f"   - Warehouses: {len(warehouses)}")
    print(f"   - Suppliers: {len(suppliers)}")
    print(f"   - Customers: {len(customers)}")
    print(f"   - Books: {len(books)}")
    print("\n🎯 Next Steps:")
    print("   1. Access the system at: http://frappemanchi.local:8000")
    print("   2. Navigate to Manchi Pustakam workspace")
    print("   3. Start creating transactions!")
    print("\n📚 Happy Publishing!\n")

if __name__ == "__main__":
    create_sample_data()
