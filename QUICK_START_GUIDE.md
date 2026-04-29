# 🚀 Manchi Pustakam - Quick Start Guide

## ✅ System Status

**Site:** frappemanchi.local
**Status:** ✅ Fully Operational
**Workspace:** ✅ Configured with all doctypes

---

## 📍 Accessing the System

1. **Open your browser:**
   ```
   http://frappemanchi.local:8000
   ```

2. **Login** with your administrator credentials

3. **Navigate to Manchi Pustakam workspace:**
   - Click on the **search bar** (or press Ctrl/Cmd + K)
   - Type "Manchi Pustakam"
   - Click on the **Manchi Pustakam** workspace

---

## 🎯 Workspace Overview

The Manchi Pustakam workspace is organized into sections:

### **Master Data**
- 📘 **Book** - Manage all books (primary & secondary)
- 👥 **Customer** - Customer master data
- 🚚 **Supplier** - Supplier master data
- 🏠 **Warehouse** - Warehouse management

### **Sales Transactions**
- 📄 **Sales Quotation** - With stock reservation
- 🧾 **Sales Invoice** - Multi-channel invoicing
- 💰 **Payment Entry** - Payment recording

### **Purchase**
- 🛒 **Purchase Order** - Purchase management
- 📦 **Stock Ledger** - Stock movements

### **Reports**
- 📚 **Book Catalogue** - Complete book list with filters
- 📊 **Sales by Channel** - Channel analysis
- 📦 **Stock Availability** - Stock with reservations
- ⚠️ **Reorder Report** - Reorder alerts

### **Utilities**
- 🔄 **Gateway Settlement** - Payment gateway reconciliation

---

## 📝 Creating Dummy Data (Step-by-Step)

### 1. Create Warehouses

**Steps:**
1. Go to **Manchi Pustakam** workspace
2. Click on **Warehouse**
3. Click **New**
4. Fill in:
   - Warehouse Name: **Nagole**
   - Warehouse Type: **Bulk Storage**
   - City: **Hyderabad**
   - Is Active: ✅ (checked)
5. Click **Save**
6. Repeat for **Tarnaka** warehouse (Warehouse Type: **Display/Retail**)

**Sample Data:**
```
Warehouse 1:
- Name: Nagole
- Type: Bulk Storage
- Address: Plot No. 123, Industrial Area, Nagole, Hyderabad
- City: Hyderabad
- Contact Person: Ravi Kumar
- Phone: +91 9876543210
- Email: nagole@manchipustakam.com

Warehouse 2:
- Name: Tarnaka
- Type: Display/Retail
- Address: Shop No. 45, Main Road, Tarnaka, Hyderabad
- City: Hyderabad
- Contact Person: Lakshmi Devi
- Phone: +91 9876543211
- Email: tarnaka@manchipustakam.com
```

### 2. Create Suppliers

**Steps:**
1. Click on **Supplier**
2. Click **New**
3. Fill in supplier details
4. Click **Save**

**Sample Suppliers:**
```
Supplier 1 - Deccan Press:
- Supplier Name: Deccan Press
- Supplier Type: Printer (Deccan Press)
- Email: orders@deccanpress.com
- Mobile: +91 9876543220
- Contact Person: Suresh Reddy
- Address: Industrial Estate, Balanagar, Hyderabad
- Payment Terms: 30 Days Credit
- Credit Period: 30
- GSTIN: 36AABCD1234E1Z5
- Is Active: ✅

Supplier 2 - Tulika Publishers:
- Supplier Name: Tulika Publishers
- Supplier Type: Distributor
- Email: sales@tulikapublishers.com
- Mobile: +91 9876543221
- Contact Person: Radhika Menon
- Address: 44 Shahpur Jat, New Delhi - 110049
- Payment Terms: 15 Days Credit
- GSTIN: 07AABCT5678F1Z3
- Is Active: ✅

Supplier 3 - Pratham Books:
- Supplier Name: Pratham Books
- Supplier Type: Publisher
- Email: orders@prathambooks.org
- Mobile: +91 9876543222
- Contact Person: Gautam John
- Address: 80 Feet Road, Koramangala, Bangalore
- Payment Terms: 30 Days Credit
- GSTIN: 29AABCP9012G1Z8
- Is Active: ✅
```

### 3. Create Customers

**Steps:**
1. Click on **Customer**
2. Click **New**
3. Fill in customer details
4. Click **Save**

**Sample Customers:**
```
Customer 1 - Little Stars School:
- Customer Name: Little Stars School
- Customer Type: Institutional
- Customer Group: Schools
- Email: library@littlestars.edu
- Mobile: +91 9876543230
- Primary Contact: Mrs. Prema Kumar
- Designation: Librarian
- Billing Address: Little Stars School, Jubilee Hills, Hyderabad
- Credit Allowed: ✅
- Credit Limit: 50000
- Credit Period: 30 days
- Default Discount %: 15
- GSTIN: 36AABCS1234H1Z9
- Territory: Telangana
- Is Active: ✅

Customer 2 - Walk-in Customer:
- Customer Name: Walk-in Customer
- Customer Type: Retail
- Customer Group: Individual
- Mobile: +91 9876543233
- Credit Allowed: ❌
- Default Discount %: 10
- Territory: Telangana
- Is Active: ✅

Customer 3 - City Public Library:
- Customer Name: City Public Library
- Customer Type: Institutional
- Customer Group: Libraries
- Email: acquisitions@citylibrary.org
- Mobile: +91 9876543232
- Primary Contact: Smt. Vidya Devi
- Billing Address: City Public Library, Abids, Hyderabad
- Credit Allowed: ✅
- Credit Limit: 100000
- Credit Period: 60 days
- Default Discount %: 25
- GSTIN: 36AABCC9012J1Z5
- Territory: Telangana
- Is Active: ✅
```

### 4. Create Books

**Steps:**
1. Click on **Book**
2. Click **New**
3. Fill in book details
4. Click **Save**

**Sample Books (Primary - Published by Manchi Pustakam):**
```
Book 1:
- Book Code: MP-001
- Book Title: చిన్ని పిట్టల కథలు (Little Bird Stories)
- ISBN: 978-81-1234-001-5
- Author: వెంకటేశ్వర రావు
- Language: Telugu
- Edition: 2nd Edition
- Publisher Type: Primary (Manchi Pustakam)
- Subject: Stories
- Age Group: 4-6 years
- Category: Story Books
- Standard Selling Price: 150
- Standard Buying Price: 75
- GST Rate: 0
- Is Stock Item: ✅
- Reorder Level: 100
- Reorder Qty: 200
- Preferred Supplier: Deccan Press
- Is Active: ✅

Book 2:
- Book Code: MP-002
- Book Title: వర్ణమాల ఆటలు (Alphabet Games)
- ISBN: 978-81-1234-002-2
- Author: లక్ష్మీ దేవి
- Language: Telugu
- Publisher Type: Primary (Manchi Pustakam)
- Subject: Learning
- Age Group: 0-3 years
- Category: Educational
- Standard Selling Price: 120
- Standard Buying Price: 60
- Reorder Level: 100
- Is Active: ✅

Book 3:
- Book Code: MP-003
- Book Title: ఎలుకల రాజు (The Mouse King)
- ISBN: 978-81-1234-003-9
- Author: రాధా కృష్ణ
- Language: Telugu
- Publisher Type: Primary (Manchi Pustakam)
- Subject: Adventure
- Age Group: 7-9 years
- Standard Selling Price: 180
- Reorder Level: 100
- Is Active: ✅

Book 4:
- Book Code: MP-004
- Book Title: సైన్స్ మేజిక్ (Science Magic)
- ISBN: 978-81-1234-004-6
- Author: సుధాకర్ రెడ్డి
- Language: Telugu
- Publisher Type: Primary (Manchi Pustakam)
- Subject: Science
- Age Group: 10-12 years
- Category: Educational
- Standard Selling Price: 250
- Reorder Level: 100
- Is Active: ✅
```

**Sample Books (Secondary - Other Publishers):**
```
Book 5:
- Book Code: TUL-001
- Book Title: The Blue Jackal
- ISBN: 978-81-8146-456-7
- Author: Amar Chitra Katha
- Language: English
- Publisher Type: Secondary (Other Publishers)
- Subject: Folk Tales
- Age Group: 7-9 years
- Standard Selling Price: 100
- Standard Buying Price: 60
- Reorder Level: 10
- Reorder Qty: 20
- Preferred Supplier: Tulika Publishers
- Is Active: ✅

Book 6:
- Book Code: PRA-001
- Book Title: Sion Misfortune
- ISBN: 978-93-5046-123-4
- Author: Pratham Books
- Language: English
- Publisher Type: Secondary (Other Publishers)
- Subject: Adventure
- Age Group: 7-9 years
- Standard Selling Price: 80
- Standard Buying Price: 48
- Reorder Level: 10
- Preferred Supplier: Pratham Books
- Is Active: ✅
```

**Service Item (Workshop):**
```
Book 7:
- Book Code: WS-001
- Book Title: Storytelling Workshop - 2 Hours
- Author: Manchi Pustakam Team
- Language: Telugu/English
- Publisher Type: Primary (Manchi Pustakam)
- Subject: Workshop
- Age Group: Adult
- Category: Workshop Material
- Standard Selling Price: 5000
- GST Rate: 18
- Is Stock Item: ❌ (unchecked)
- Is Active: ✅
```

---

## 🧪 Testing Transactions

### Test 1: Create a Sales Quotation with Stock Reservation

**Steps:**
1. Go to **Sales Quotation** > **New**
2. Fill in:
   - Customer: **Little Stars School**
   - Quotation Date: Today
   - Valid Till: +30 days from today
   - Reserve Stock: ✅ (check this!)
3. In Items table, add:
   - Book: **MP-001** (Little Bird Stories)
   - Warehouse: **Nagole**
   - Qty: **50**
   - Rate: **150** (auto-filled)
   - Discount %: **15**
4. Click **Save**
5. Click **Submit**

**Expected Result:**
- ✅ Quotation created with "Reserved" status
- ✅ Stock reserved for 50 units
- ✅ Total calculated with 15% discount
- ✅ Amount rounded to nearest rupee

### Test 2: Create a Sales Invoice (Counter Sales)

**Steps:**
1. Go to **Sales Invoice** > **New**
2. Fill in:
   - Customer: **Walk-in Customer**
   - Sales Channel: **Counter Sales**
   - Payment Gateway: **Cash**
3. In Items table, add:
   - Book: **MP-002** (Alphabet Games)
   - Warehouse: **Tarnaka**
   - Qty: **10**
   - Rate: **120**
   - Discount %: **10**
4. Click **Save**
5. Review calculated totals
6. Click **Submit**

**Expected Result:**
- ✅ Invoice created
- ✅ 10% discount applied automatically
- ✅ GST = 0% (books)
- ✅ Grand Total rounded to nearest rupee
- ✅ Stock ledger entry created (if stock system is active)

### Test 3: Create Payment Entry (Razor Pay)

**Steps:**
1. Go to **Payment Entry** > **New**
2. Fill in:
   - Payment Type: **Receive**
   - Party Type: **MP Customer**
   - Party: **Little Stars School**
   - Posting Date: Today
   - Payment Method: **Razor Pay**
   - Payment Gateway: **Razor Pay**
   - Paid Amount: **10000**
3. Click **Save**

**Expected Result:**
- ✅ Gateway Commission calculated (2% = 200)
- ✅ Net Amount = 10000 - 200 = 9800
- ✅ Settlement Status = Pending

### Test 4: Create Purchase Order

**Steps:**
1. Go to **Purchase Order** > **New**
2. Fill in:
   - Supplier: **Deccan Press**
   - Transaction Date: Today
   - Required By: +7 days
3. In Items table, add:
   - Book: **MP-001**
   - Warehouse: **Nagole**
   - Qty: **200**
   - Rate: **75**
4. Click **Save**
5. Click **Submit**

**Expected Result:**
- ✅ Purchase Order created
- ✅ Total calculated
- ✅ Status = Submitted

---

## 📊 Testing Reports

### Test Report 1: Book Catalogue

**Steps:**
1. Go to **Book Catalogue** report
2. Apply filters:
   - Publisher Type: **Primary (Manchi Pustakam)**
   - Age Group: **4-6 years**
3. Click **Refresh**

**Expected Result:**
- Shows all primary books for 4-6 years age group
- Display includes: Title, ISBN, Author, Price, Stock, Reorder Level

### Test Report 2: Sales by Channel

**Steps:**
1. Go to **Sales by Channel** report
2. Set date range: Last 30 days
3. Click **Refresh**

**Expected Result:**
- Shows sales breakdown by channel
- Displays chart (pie/bar)
- Shows total amount, qty, avg invoice value per channel

### Test Report 3: Stock Availability

**Steps:**
1. Go to **Stock Availability Report**
2. Click **Refresh**

**Expected Result:**
- Shows all books with stock status
- Displays: Actual Qty, Reserved Qty, Available Qty
- Color-coded status (In Stock, Low Stock, Out of Stock)

### Test Report 4: Reorder Report

**Steps:**
1. Go to **Reorder Report**
2. Click **Refresh**

**Expected Result:**
- Shows books below reorder level
- Includes supplier contact information
- Shows lead time

---

## 🎯 Key Features to Test

### ✅ Stock Reservation
- Create quotation with "Reserve Stock" checked
- Verify stock is reserved
- Cancel quotation and verify stock is released

### ✅ Multi-Channel Discounts
- Counter Sales: Auto-applies 10% discount
- Website Sales: No discount
- Exhibition Sales: 10% discount
- Institutional: Custom discount per customer

### ✅ Payment Gateway Commission
- Razor Pay: 2% commission calculated
- Phone Pe: 1.5% commission calculated
- Net amount = Gross - Commission

### ✅ Bill Rounding
- All invoices round to nearest rupee
- Check Grand Total is always a whole number

### ✅ GST Calculation
- Books: 0% GST
- Services/Workshops: 18% GST

### ✅ Credit Limit Validation
- Try creating invoice that exceeds customer credit limit
- System should show warning/error

---

## 🔧 Common Operations

### Daily Operations

**Morning:**
1. Check **Reorder Report** for low stock items
2. Review pending **Sales Quotations**
3. Process **Sales Invoices** from previous day

**During Day:**
1. Create **Sales Quotations** for inquiries
2. Convert approved quotations to **Sales Orders**
3. Generate **Sales Invoices** for deliveries
4. Record **Payments** received

**Evening:**
1. Review day's sales via **Sales by Channel** report
2. Update **Stock Ledger** if manual adjustments needed
3. Process **Payment Gateway Settlements**

### Monthly Operations

**Month End:**
1. Run **Sales by Channel** report for full month
2. Check **Outstanding Payments** from customers
3. Review **Reorder Report** and create **Purchase Orders**
4. Reconcile **Payment Gateway Settlements**
5. Review **Stock Availability** across warehouses

---

## 📞 Need Help?

### Documentation
- Full README: `/home/caratred/frappev16/apps/manchipustakam/README.md`
- Implementation Status: `/home/caratred/frappev16/apps/manchipustakam/IMPLEMENTATION_STATUS.md`
- Migration Guide: `/home/caratred/frappev16/apps/manchipustakam/MIGRATION_SUCCESS.md`

### Support
- Email: info@caratred.com
- Developer: caratRED

---

## 🎊 You're All Set!

Your **Manchi Pustakam ERP system** is fully configured and ready to use!

**Next Steps:**
1. ✅ Create master data using steps above
2. ✅ Test all transactions
3. ✅ Train your team
4. ✅ Go live!

**Happy Publishing! 📚**
