# 📚 Sistem ToDo List Akademik - Panduan Lengkap

## 📁 Struktur File
```
todo_akademik/
├── todo_akademik.py       ← File utama program
├── todo_database.json     ← Database otomatis dibuat saat pertama run
└── README.md              ← File ini
```

---

## ▶️ Cara Menjalankan

```bash
python todo_akademik.py
```

> Tidak perlu install library tambahan. Hanya menggunakan Python standar (json, os).

---

## 🗄️ DATABASE (File JSON)

Program menggunakan **file JSON lokal** sebagai database (`todo_database.json`).

### Format database:
```json
{
  "tugas": [
    {
      "no": 1,
      "kode": "PBO01",
      "matkul": "Pemrograman Berorientasi Objek",
      "deskripsi": "Membuat class diagram UML",
      "prioritas": 1,
      "status": "Belum"
    }
  ],
  "counter": 1
}
```

### Keunggulan JSON sebagai database lokal:
- ✅ Tidak perlu instalasi database server
- ✅ Data tersimpan permanen (tidak hilang saat program ditutup)
- ✅ Bisa dibuka & diedit manual dengan Notepad/VS Code
- ✅ Sesuai standar Modul 6 (File I/O)

---

## ☁️ OPSI HOSTING / DEPLOYMENT

### 🥇 Opsi 1 — Jalankan Lokal (Direkomendasikan untuk tugas)
Tidak perlu hosting. Cukup jalankan di komputer sendiri:
```bash
python todo_akademik.py
```
File `todo_database.json` otomatis tersimpan di folder yang sama.

---

### 🥈 Opsi 2 — GitHub (Backup & Pengumpulan Tugas)
Simpan kode ke GitHub agar dosen bisa melihat:

1. Buat akun di https://github.com
2. Buat repository baru (misal: `todo-akademik`)
3. Upload file:
```bash
git init
git add todo_akademik.py README.md
git commit -m "Initial commit - Sistem ToDo Akademik"
git remote add origin https://github.com/username/todo-akademik.git
git push -u origin main
```

---

### 🥉 Opsi 3 — Replit (Jalankan Online, Gratis)
Cocok jika ingin demo online tanpa install Python:

1. Buka https://replit.com
2. Buat akun gratis
3. Klik **+ Create Repl** → pilih **Python**
4. Upload / paste isi `todo_akademik.py`
5. Klik **Run** ▶️
6. Bagikan link Repl ke dosen

> ⚠️ Di Replit, database JSON tersimpan di server Replit (tidak hilang selama Repl aktif).

---

### 🔧 Opsi 4 — PythonAnywhere (Hosting Python Gratis)
1. Daftar di https://www.pythonanywhere.com (gratis)
2. Buka **Files** → Upload `todo_akademik.py`
3. Buka **Bash Console**:
```bash
python todo_akademik.py
```
Database JSON tersimpan di server PythonAnywhere.

---

## 🗺️ Pemetaan Modul (Inline Comment Map)

| Modul | Konsep              | Lokasi di Kode                                    |
|-------|---------------------|---------------------------------------------------|
| 1     | Variabel & Tipe Data | `counter`, `no_urut`, `persen_selesai`, dll       |
| 2     | Kondisi (if/elif)   | Semua fungsi validasi & routing menu              |
| 3     | Perulangan (while)  | `while True` di `main()`, loop validasi input     |
| 4     | Fungsi              | `tambah_tugas()`, `daftar_tugas()`, dll           |
| 5     | List, Dict, Set, Tuple | `data["tugas"]` (List+Dict), `set_kode_ada` (Set), `PRIORITAS_VALID` (Tuple) |
| 6     | File I/O (JSON)     | `load_database()`, `simpan_database()`            |

---

## ✅ Checklist Penilaian

- [x] **40% Fungsionalitas**: Tambah, Daftar, Tandai Selesai, Hapus, Statistik, Keluar
- [x] **30% Penerapan Modul 1-6**: Semua modul digunakan & diberi komentar
- [x] **15% Validasi & Error Handling**: Input kosong, tipe salah, duplikasi, konfirmasi hapus
- [x] **15% Kualitas Kode**: Nama variabel deskriptif, komentar inline, struktur bersih
