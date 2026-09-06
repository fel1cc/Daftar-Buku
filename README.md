# Kasir-git
Program ini dirancang untuk mensimulasikan alur transaksi kasir toko secara terstruktur, mulai dari pencarian kode barang, penentuan kuantitas dan diskon, hingga pembuatan ringkasan struk belanja di akhir transaksi.

## 🎯 Fitur Utama
- **Pencarian Kode Barang Otomatis:** Menggunakan pemetaan *dictionary* untuk mengenali nama barang dan harga satuan berdasarkan kode input (`B123`, `M243`, dll).
- **Penanganan Input Case-Insensitive:** Pengguna dapat menginput kode barang dan perintah (`Y`/`T`) menggunakan huruf kapital maupun huruf kecil (`.upper()`).
- **Kalkulasi Subtotal & Diskon:** Menghitung total harga per item berdasarkan kuantitas yang dibeli dikurangi diskon spesifik (jika ada).
- **Akumulasi Keranjang Belanja:** Menyimpan riwayat barang yang dibeli selama sesi transaksi dan menjumlahkan total keseluruhan secara otomatis.
- **Validasi Input:** Memastikan perintah perulangan hanya menerima pilihan `Y` atau `T` serta memberikan notifikasi jika kode barang tidak ditemukan.
- **Cetak Ringkasan Struk:** Menampilkan struk pembayaran yang terformat rapi setelah transaksi selesai.
