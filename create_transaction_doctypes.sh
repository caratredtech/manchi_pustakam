#!/bin/bash
# Script to create all transaction doctypes for Manchi Pustakam

cd /home/caratred/frappev16/apps/manchipustakam

# Create directories
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_sales_quotation
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_sales_quotation_item
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_sales_order
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_sales_order_item
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_sales_invoice
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_sales_invoice_item
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_purchase_order
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_purchase_order_item
mkdir -p manchipustakam/manchi_pustakam/doctype/mp_payment_entry
mkdir -p manchipustakam/manchi_pustakam/doctype/payment_gateway_settlement

echo "All transaction doctype directories created successfully!"
