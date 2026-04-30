# Manchi Pustakam - Book Publishing & Distribution ERP

A comprehensive Frappe-based application for managing book publishing and distribution operations for **Manchi Pustakam**, a Telugu children's book publisher and distributor.

## 📚 Overview
caratRED
Manchi Pustakam is a complete custom ERP solution built on the Frappe Framework to manage:
- Book inventory (published and distributed titles)
- Multi-channel sales (Counter, Website, Exhibition, Institutional)
- Multi-warehouse stock management
- Payment gateway integration (Razor Pay, Phone Pe)
- Purchase order and supplier management
- Credit management for institutional customers
- Stock reservation for quotations
- GST-compliant invoicing

## 🚀 Key Features

### Master Data Management
- **Books** with ISBN tracking, publisher classification, age groups, subjects
- **Customers** with credit management and discount policies
- **Suppliers** with payment terms and lead times
- **Warehouses** (Nagole - Bulk, Tarnaka - Display)

### Sales Management
- Sales Quotations with **Stock Reservation**
- Multi-channel Sales Invoices (Counter/Website/Exhibition/Institutional)
- Automatic discount application per channel
- Bill rounding to nearest rupee
- GST calculation (0% books, 18% services)

### Payment Management
- Multi-gateway support (Cash, Online, Phone Pe, Razor Pay, Cheque)
- Automatic commission calculation (Razor Pay 2%, Phone Pe 1.5%)
- Settlement tracking and reconciliation
- Credit limit validation

### Reports
- Book Catalogue (searchable by ISBN, age group, subject)
- Sales by Channel Analysis
- Stock Availability with Reservations
- Reorder Report with Supplier Info

## 📦 Installation

The app is already in your apps directory:

```bash
# Install on site
bench --site manchipustkam.local install-app manchipustakam

# Run migrations
bench --site manchipustkam.local migrate

# Clear cache and build
bench --site manchipustkam.local clear-cache
bench build --app manchipustakam

# Restart
bench restart
```

## 🔧 Initial Setup

1. **Create Roles:** MP Manager, MP User
2. **Create Warehouses:** Nagole, Tarnaka
3. **Add Suppliers:** Deccan Press, Distributors
4. **Import Master Data:** Books, Customers

## 📖 Quick Start

### Create Sales Invoice
1. New MP Sales Invoice
2. Select Customer & Sales Channel
3. Add Books
4. System applies discounts, calculates GST, rounds bill
5. Submit to post stock

### Process Payment
1. New MP Payment Entry
2. Select gateway (Razor Pay/Phone Pe)
3. System calculates commission
4. Submit to record payment

## 📊 DocTypes Created

**Master:**
- Book, Book Set Component
- MP Customer, MP Supplier
- MP Warehouse
- Stock Ledger Entry

**Transactions:**
- MP Sales Quotation & Items
- MP Sales Invoice & Items
- MP Purchase Order & Items
- MP Payment Entry
- Payment Gateway Settlement

**Reports:**
- Book Catalogue
- Sales by Channel
- Stock Availability Report
- Reorder Report

## 🎯 Business Rules Implemented

- **Discounts:** Counter/Exhibition 10%, Website 0%, Institutional negotiable
- **GST:** Books 0%, Services 18%
- **Reorder Levels:** Primary 100, Secondary 10
- **Payment Gateways:** Razor Pay 2%, Phone Pe 1.5% commission
- **Bill Rounding:** Always to nearest rupee
- **Stock Reservation:** For pending quotations

## 📚 Documentation

- **BRD Analysis:** `/home/caratred/frappev16/BRD_ANALYSIS_AND_RECOMMENDATIONS.md`
- **Implementation Status:** `IMPLEMENTATION_STATUS.md`
- **Frappe Docs:** https://frappeframework.com/docs

## 📞 Support

Email: info@caratred.com

## 📄 License

MIT

---

**Version:** 1.0.0 | **Status:** Production Ready
**Last Updated:** March 13, 2026
