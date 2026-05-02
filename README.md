# 🔍 Instagram Follback Checker

Skrip Python sederhana untuk mengecek siapa saja akun Instagram yang kamu *follow* tetapi tidak mem-*follow back* kamu. Skrip ini bekerja secara lokal menggunakan data resmi dari Instagram sehingga 100% aman tanpa perlu login atau memberikan password.

## ⚖️ Lisensi
Proyek ini bersifat *open-source* dan didistribusikan di bawah lisensi **GNU General Public License v3.0 (GPL-3.0)**. 
Anda bebas untuk menggunakan, menyalin, memodifikasi, dan mendistribusikan ulang kode ini. Namun, setiap karya turunan atau modifikasi yang dibagikan ke publik **wajib** menggunakan lisensi GPL-3.0 yang sama dan harus tetap *open-source*. Lihat file `LICENSE` untuk informasi lebih lengkap.

---

## 🛠️ Persyaratan
- Komputer / Laptop dengan OS Windows, macOS, atau Linux (bisa juga via Termux di Android).
- Sudah menginstal **Python** (versi 3.x ke atas).
- Sudah mengunduh data Instagram kamu (format JSON).

## 📥 Cara Mendapatkan Data Instagram
1. Buka aplikasi Instagram di HP kamu atau via web browser.
2. Pergi ke **Pengaturan dan privasi (Settings and privacy)** > **Pusat Akun (Accounts Center)**.
3. Pilih **Informasi dan izin Anda (Your information and permissions)** > **Unduh informasi Anda (Download your information)**.
4. Buat permintaan unduhan baru. 
5. **PENTING:** Pastikan rentang tanggal adalah "Sepanjang waktu (All time)" dan formatnya adalah **JSON** (bukan HTML).
6. Tunggu email dari Instagram, lalu unduh file `.zip` tersebut.

## 🚀 Cara Menggunakan Skrip
1. Ekstrak file `.zip` data Instagram yang sudah kamu unduh.
2. Buka folder hasil ekstrak, lalu navigasi ke folder: `connections/followers_and_following/`.
3. Di dalam folder tersebut, kamu akan menemukan file:
   - `following.json`
   - `followers_1.json`
4. Buat file baru bernama `cek_follback.py` di dalam **folder yang sama** dengan kedua file JSON di atas.
5. Salin kode Python dari repositori ini ke dalam file `cek_follback.py`.
6. Buka Terminal atau Command Prompt (atau jalankan langsung melalui VS Code) di folder tersebut.
7. Jalankan perintah berikut:
   ```bash
   python cek_follback.py

​Skrip akan langsung menampilkan daftar nama akun yang tidak follback kamu!
​🤝 Kontribusi
​Jika Anda memiliki ide untuk mengembangkan skrip ini, silakan lakukan Fork pada repositori ini, buat perubahan Anda, lalu kirimkan Pull Request. Semua kontribusi sangat dihargai!

​Dibuat oleh Ivan Krisopras Hutabarat
