# Database Schema - Toko Online Sederhana

Dokumen ini menjelaskan struktur tabel yang digunakan dalam aplikasi toko online sederhana.

---

## 1. Tabel users

Tabel ini digunakan untuk menyimpan data pengguna aplikasi (admin dan customer).

**Struktur:**

- id (INT, Primary Key, Auto Increment)
- nama (VARCHAR)
- email (VARCHAR, UNIQUE)
- password (VARCHAR)
- role (ENUM: 'admin', 'customer')
- created_at (TIMESTAMP)

---

## 2. Tabel products

Tabel ini digunakan untuk menyimpan data produk yang dijual.

**Struktur:**

- id_produk (INT, Primary Key, Auto Increment)
- nama_produk (VARCHAR)
- deskripsi (TEXT)
- harga (INT)
- stok (INT)
- gambar (VARCHAR)
- created_at (TIMESTAMP)

---

## 3. Tabel orders

Tabel ini digunakan untuk menyimpan data transaksi pembelian.

**Struktur:**

- id_order (INT, Primary Key, Auto Increment)
- id_user (INT, Foreign Key -> users.id)
- total_harga (INT)
- status (ENUM: 'pending', 'dibayar', 'dikirim', 'selesai')
- created_at (TIMESTAMP)

---

## 4. Tabel order_detail

Tabel ini digunakan untuk menyimpan detail produk dalam setiap order.

**Struktur:**

- id_detail (INT, Primary Key, Auto Increment)
- id_order (INT, Foreign Key -> orders.id_order)
- id_produk (INT, Foreign Key -> products.id_produk)
- jumlah (INT)
- harga (INT)

---

## Relasi Antar Tabel

- users → orders (1 ke banyak)
- orders → order_detail (1 ke banyak)
- products → order_detail (1 ke banyak)