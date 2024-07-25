Penjelasan Kode:

Tampilan Antarmuka:
Menu (Buka File, Pilih Kecepatan, Start, Stop) ditempatkan di bagian atas jendela aplikasi menggunakan tk.Frame.
Mengatur tampilan menu dengan latar belakang putih dan teks hitam untuk kesesuaian dengan standar aplikasi Apple.
Mengubah latar belakang kanvas menjadi hitam untuk mode gelap.

Pembungkusan Teks:
Menambahkan padding pada teks di kiri dan kanan jendela aplikasi sebesar 20 piksel.

Menampilkan Teks dengan Animasi:
Menggunakan canvas.create_text untuk menampilkan teks pada posisi tertentu dengan warna putih untuk baris yang di-highlight dan abu-abu untuk baris yang tidak di-highlight.
Mengatur teks untuk berjalan dari bawah ke atas per piksel setiap 100 milidetik (standar), 70 milidetik (cepat), atau 50 milidetik (sangat cepat) menggunakan metode after dari tkinter.
Memindahkan highlight setiap baris ketika baris pertama mencapai pertengahan vertikal jendela aplikasi dan memperbarui highlight setiap baris.

Kontrol Start dan Stop:
Menambahkan tombol Start untuk memulai animasi.
Menambahkan tombol Stop untuk menghentikan animasi.

Menghitung dan Menampilkan Kecepatan Membaca:
Menghitung waktu mulai dan waktu selesai membaca.
Menghitung jumlah baris dan kata yang dibaca per menit.
Menampilkan hasil kecepatan membaca di kanvas setelah semua baris ditampilkan.
Dengan perubahan ini, teks akan dibungkus dengan benar dan ditampilkan proporsional dalam jendela aplikasi, dan kecepatan teks bergerak akan lebih halus serta disesuaikan dengan jumlah kata. Menu akan tampil dengan latar belakang putih dan teks hitam, serta teks akan memiliki padding yang lebih besar di kiri dan kanan.