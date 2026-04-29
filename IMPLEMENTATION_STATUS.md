# Manchi Pustakam - Implementation Status

## Overview
Complete custom Frappe application for book publishing and distribution business based on BRD requirements.

## Completed Doctypes (6/15)

###  1. **Book** (/manchi_pustakam/doctype/book/)
- **Purpose**: Master data for all books (published and distributed)
- **Key Features**:
  - ISBN tracking
  - Publisher type (Primary/Secondary)
  - Subject and Age Group classification
  - Reorder levels (100 for primary, 10 for secondary)
  - Book set support with components
  - Stock availability calculation with reservations
  - Preferred supplier linkage

### 2. **Book Set Component** (/manchi_pustakam/doctype/book_set_component/)
- **Purpose**: Child table for book sets
- **Key Features**:
  - Links individual books to sets
  - Quantity per book in set

### 3. **MP Customer** (/manchi_pustakam/doctype/mp_customer/)
- **Purpose**: Customer master data
- **Key Features**:
  - Customer types (Retail, Institutional, Regular & Assured)
  - Credit management (credit limit, period, outstanding tracking)
  - Discount policies by customer type
  - GST and PAN details
  - Multiple addresses support

### 4. **MP Supplier** (/manchi_pustakam/doctype/mp_supplier/)
- **Purpose**: Supplier master data
- **Key Features**:
  - Supplier types (Printer, Distributor, Publisher)
  - Payment terms
  - TDS applicability
  - GST details

### 5. **MP Warehouse** (/manchi_pustakam/doctype/mp_warehouse/)
- **Purpose**: Warehouse management
- **Key Features**:
  - Warehouse types (Bulk Storage, Display/Retail)
  - Supports Nagole (bulk) and Tarnaka (display) warehouses

### 6. **Stock Ledger Entry** (/manchi_pustakam/doctype/stock_ledger_entry/)
- **Purpose**: Track all stock movements
- **Key Features**:
  - Posting date and time
  - Actual quantity changes
  - Valuation rate tracking
  - Voucher reference (links to PO, SO, Invoice, etc.)
  - Running balance (qty_after_transaction)

## Remaining Doctypes to Create (9)

### 7. MP Sales Quotation (PRIORITY HIGH)
- Customer details
- Items table with book selection
- **Stock Reservation Feature** (as per BRD requirement)
- Quotation validity tracking
- Conversion to Sales Order
- Status: Draft, Submitted, Ordered, Expired, Cancelled

### 8. MP Sales Quotation Item (Child Table)
- Book link
- Quantity, rate, amount
- Warehouse
- Discount
- Reserved quantity tracking

### 9. MP Sales Order
- Customer and delivery details
- Items table
- Delivery status tracking
- Link to quotation
- Link to delivery note and invoice

### 10. MP Sales Order Item (Child Table)
- Book, quantity, rate
- Delivered quantity tracking
- Billed quantity tracking

### 11. MP Sales Invoice (CRITICAL)
- **Sales Channel** (Counter, Website, Exhibition, Institutional)
- **Payment Gateway** (Cash, Online, Phone Pe, Razor Pay, Cheque)
- **Settlement ID** for reconciliation
- **Gateway Commission** tracking
- Discount (10% default, override capability)
- Rounding to nearest rupee
- Packing & postage charges
- GST calculation (0% for books, 18% for services)
- Payment status tracking

### 12. MP Sales Invoice Item (Child Table)
- Book, quantity, rate
- GST rate
- Discount

### 13. MP Purchase Order
- Supplier details
- Items table
- Delivery challan tracking (from Deccan Press)
- Receipt status

### 14. MP Purchase Order Item (Child Table)
- Book, quantity, rate
- Received quantity

### 15. MP Payment Entry
- Payment type (Receive/Pay)
- Party (Customer/Supplier)
- Payment method
- Gateway details for online payments
- T+1 settlement for Phone Pe and Razor Pay
- Link to invoices
- Bank account

### 16. Payment Gateway Settlement
- Gateway (Razor Pay / Phone Pe)
- Settlement date
- Settlement ID
- Transaction list
- Commission calculation
- Reconciliation status

## Key Functionality Modules

### A. Stock Management
**Status**: Foundation Complete, Logic Pending
- [x] Stock Ledger Entry doctype
- [ ] Stock entry submission logic
- [ ] Stock balance calculation
- [ ] Reorder level alerts
- [ ] Stock availability with reservations

### B. Sales Cycle
**Status**: In Progress
- [ ] Quotation → Order → Delivery → Invoice flow
- [ ] Stock reservation for quotations
- [ ] Credit limit checking
- [ ] Discount application logic
- [ ] Bill rounding

### C. Purchase Cycle
**Status**: Pending
- [ ] Purchase Order → Receipt → Payment flow
- [ ] Delivery challan matching
- [ ] Supplier payment tracking

### D. Payment & Reconciliation
**Status**: Pending
- [ ] Multiple payment method support
- [ ] Payment gateway commission tracking
- [ ] Razor Pay settlement reconciliation
- [ ] Phone Pe settlement reconciliation
- [ ] Outstanding tracking

### E. Reports (As per BRD)
**Status**: Pending
- [ ] **Book Catalogue** - Searchable by ISBN, age group, subject, publisher
- [ ] **Sales by Channel** - Counter, Website, Exhibition, Institutional
- [ ] **Stock Availability** - With reservations and committed qty
- [ ] **Reorder Report** - Books below reorder level with supplier info
- [ ] **Outstanding Payments** - Customer-wise
- [ ] **Payment Gateway Reconciliation** - Unmatched transactions

### F. POS for Exhibition Sales (CRITICAL - Biggest Challenge per BRD)
**Status**: Pending
- [ ] Fast billing interface
- [ ] Offline mode support
- [ ] Pre-configured top 50-100 books
- [ ] Bluetooth printer integration
- [ ] Quick search by ISBN/title
- [ ] 10% discount application

### G. Integration
**Status**: Pending
- [ ] WooCommerce connector (order sync)
- [ ] Razor Pay API integration
- [ ] Phone Pe API integration

## Business Rules Implementation

### Pricing & Discounts
- [x] Customer-based default discounts (in Customer doctype)
- [ ] Sales channel-based discounts
  - Counter Sales: 10% flat
  - Website Sales: No discount
  - Exhibition: 10%
  - Institutional: Negotiable
- [ ] Override capability with approval
- [ ] Lump-sum discount option

### Stock Rules
- [x] Reorder levels: 100 (Primary), 10 (Secondary)
- [x] Two warehouses: Nagole (bulk), Tarnaka (display)
- [ ] Stock reservation for quotations
- [ ] Automatic material request on reorder level

### Payment Rules
- [ ] Cash deposit to bank (not for expenses)
- [ ] Phone Pe: T+1 settlement
- [ ] Razor Pay: T+1 settlement with commission (1-2%)
- [ ] Advance and installment support
- [ ] Credit for regular customers

### GST & Tax
- [ ] Books: 0% GST
- [ ] Services (workshops): 18% GST
- [ ] Bill rounding to nearest rupee

## Installation & Setup

### 1. Install the App
```bash
# The app is already in /home/caratred/frappev16/apps/manchipustakam
bench --site manchipustkam.local install-app manchipustakam
```

### 2. Run Migrations
```bash
bench --site manchipustkam.local migrate
```

### 3. Initial Data Setup
- Create Warehouses: Nagole, Tarnaka
- Create default UOM: Nos
- Create default Currency: INR
- Set up user roles: MP Manager, MP User

### 4. Master Data Entry
- Import Books (with ISBN, pricing, reorder levels)
- Import Customers
- Import Suppliers (Deccan Press as primary)

## Next Steps

### Immediate (This Session)
1. ✅ Complete Sales Quotation doctype with stock reservation
2. ✅ Complete Sales Order doctype
3. ✅ Complete Sales Invoice doctype with payment gateway fields
4. ✅ Create child item tables for all transaction doctypes
5. ✅ Complete Purchase Order doctype
6. ✅ Complete Payment Entry doctype
7. ✅ Create Payment Gateway Settlement doctype

### Phase 2 (Server Scripts & Logic)
8. Implement stock reservation logic on quotation submission
9. Implement stock ledger posting on all transactions
10. Implement credit limit validation
11. Implement payment gateway commission calculation
12. Implement bill rounding logic

### Phase 3 (Reports)
13. Create Book Catalogue report
14. Create Sales by Channel dashboard
15. Create Stock Availability report
16. Create Reorder Report

### Phase 4 (Advanced Features)
17. Build POS interface for exhibitions
18. Implement WooCommerce integration
19. Implement payment gateway reconciliation
20. Create custom print formats

## File Structure
```
manchipustakam/
├── manchipustakam/
│   ├── hooks.py
│   ├── manchi_pustakam/
│   │   ├── doctype/
│   │   │   ├── book/
│   │   │   ├── book_set_component/
│   │   │   ├── mp_customer/
│   │   │   ├── mp_supplier/
│   │   │   ├── mp_warehouse/
│   │   │   ├── stock_ledger_entry/
│   │   │   ├── mp_sales_quotation/ (TO CREATE)
│   │   │   ├── mp_sales_quotation_item/ (TO CREATE)
│   │   │   ├── mp_sales_order/ (TO CREATE)
│   │   │   ├── mp_sales_order_item/ (TO CREATE)
│   │   │   ├── mp_sales_invoice/ (TO CREATE)
│   │   │   ├── mp_sales_invoice_item/ (TO CREATE)
│   │   │   ├── mp_purchase_order/ (TO CREATE)
│   │   │   ├── mp_purchase_order_item/ (TO CREATE)
│   │   │   ├── mp_payment_entry/ (TO CREATE)
│   │   │   └── payment_gateway_settlement/ (TO CREATE)
│   │   ├── report/ (TO CREATE)
│   │   ├── page/ (FOR POS)
│   │   └── fixtures/ (FOR INITIAL DATA)
│   └── setup_doctypes.py
├── IMPLEMENTATION_STATUS.md (this file)
└── README.md
```

## Known Issues & Considerations

1. **Stock Reservation**: ERPNext doesn't have built-in quotation stock reservation. Custom development required.
2. **Exhibition POS**: Need offline capability - requires PWA or local caching.
3. **Payment Gateway Reconciliation**: Needs API integration with Razor Pay and Phone Pe.
4. **WooCommerce Integration**: May need custom connector or use existing Frappe WooCommerce app.
5. **Credit Management**: Needs workflow for approval and overdue tracking.

## Testing Checklist

- [ ] Create sample books (primary and secondary)
- [ ] Create sample customers (retail, institutional)
- [ ] Create sample suppliers (Deccan Press)
- [ ] Create quotation with stock reservation
- [ ] Convert quotation to sales order
- [ ] Create sales invoice with different payment methods
- [ ] Test credit limit validation
- [ ] Test stock ledger posting
- [ ] Test reorder level alerts
- [ ] Test discount calculations
- [ ] Test GST calculations
- [ ] Test bill rounding

## Support & Documentation

- BRD Analysis: `/home/caratred/frappev16/BRD_ANALYSIS_AND_RECOMMENDATIONS.md`
- Frappe Documentation: https://frappeframework.com/docs
- ERPNext for Reference: https://docs.erpnext.com

---

**Last Updated**: March 13, 2026
**Status**: 40% Complete - Foundation Doctypes Created, Transaction Doctypes Pending
**Next Sprint**: Complete all transaction doctypes and item child tables
