#!/bin/bash
# Import dummy data for Manchi Pustakam

cd /home/caratred/frappev16

echo "Creating Warehouses..."
bench --site frappemanchi.local execute "frappe.get_doc({'doctype': 'MP Warehouse', 'warehouse_name': 'Nagole', 'warehouse_type': 'Bulk Storage', 'city': 'Hyderabad', 'is_active': 1}).insert(ignore_permissions=True); frappe.db.commit()"

bench --site frappemanchi.local execute "frappe.get_doc({'doctype': 'MP Warehouse', 'warehouse_name': 'Tarnaka', 'warehouse_type': 'Display/Retail', 'city': 'Hyderabad', 'is_active': 1}).insert(ignore_permissions=True); frappe.db.commit()"

echo "Creating Suppliers..."
bench --site frappemanchi.local execute "frappe.get_doc({'doctype': 'MP Supplier', 'supplier_name': 'Deccan Press', 'supplier_type': 'Printer (Deccan Press)', 'email': 'orders@deccanpress.com', 'is_active': 1}).insert(ignore_permissions=True); frappe.db.commit()"

echo "Creating Customers..."
bench --site frappemanchi.local execute "frappe.get_doc({'doctype': 'MP Customer', 'customer_name': 'Walk-in Customer', 'customer_type': 'Retail', 'customer_group': 'Individual', 'is_active': 1}).insert(ignore_permissions=True); frappe.db.commit()"

echo "Creating Books..."
bench --site frappemanchi.local execute "frappe.get_doc({'doctype': 'Book', 'book_code': 'MP-001', 'book_title': 'Little Bird Stories', 'publisher_type': 'Primary (Manchi Pustakam)', 'standard_selling_price': 150, 'is_stock_item': 1, 'reorder_level': 100, 'is_active': 1}).insert(ignore_permissions=True); frappe.db.commit()"

echo "✅ Sample data created!"
