"""
=============================================================
  SISTEM TODO LIST AKADEMIK
  Tugas Besar Python CLI - Modul 1-6
=============================================================
  Modul 1 : Variabel, Tipe Data, Input/Output
  Modul 2 : Kondisi (if/elif/else)
  Modul 3 : Perulangan (while loop utama)
  Modul 4 : Fungsi
  Modul 5 : List, Dictionary, Set, Tuple
  Modul 6 : File I/O (JSON sebagai database)
=============================================================
"""

import json   # Modul 6 - File I/O
import os

# ===========================================================
# MODUL 5 - Tuple: Konstanta/konfigurasi sistem
# ===========================================================
PRIORITAS_VALID = (1, 2, 3)           # tuple prioritas yang valid
STATUS_VALID    = ("Belum", "Selesai") # tuple status yang valid
FILE_DATABASE   = "todo_database.json" # nama file penyimpanan

# ===========================================================
# MODUL 6 - File I/O: Load & Save Database (JSON)
# ===========================================================

def load_database():
    """Memuat data tugas dari file JSON. Modul 6."""
    # Modul 2 - Kondisi: cek apakah file ada
    if os.path.exists(FILE_DATABASE):
        try:
            with open(FILE_DATABASE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except (json.JSONDecodeError, IOError):
            print("[!] Database rusak. Membuat database baru...")
            return {"tugas": [], "counter": 0}
    else:
        return {"tugas": [], "counter": 0}


def simpan_database(data):
    """Menyimpan data tugas ke file JSON. Modul 6."""
    try:
        with open(FILE_DATABASE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"[!] Gagal menyimpan database: {e}")


# ===========================================================
# MODUL 4 - Fungsi: Validasi Input
# ===========================================================

def validasi_input_kosong(nilai, nama_field):
    """Modul 4 - Fungsi validasi input tidak boleh kosong. Modul 2 - Kondisi."""
    if nilai.strip() == "":
        print(f"[!] {nama_field} tidak boleh kosong.")
        return False
    return True


def validasi_prioritas(nilai_str):
    """Modul 4 - Fungsi validasi prioritas (1-3). Modul 2 - Kondisi."""
    try:
        nilai = int(nilai_str)
        # Modul 2 - Kondisi: cek apakah dalam tuple prioritas valid
        if nilai in PRIORITAS_VALID:
            return nilai
        else:
            print("[!] Prioritas harus angka 1, 2, atau 3.")
            return None
    except ValueError:
        print("[!] Prioritas harus berupa angka (bukan huruf).")
        return None


def validasi_kode_unik(kode, set_kode_ada):
    """Modul 4 - Validasi kode unik menggunakan Set. Modul 5 - Set."""
    # Modul 5 - Set: cek duplikasi O(1)
    if kode.strip().upper() in set_kode_ada:
        print(f"[!] Kode '{kode.upper()}' sudah ada. Gunakan kode lain.")
        return False
    return True


def ambil_set_kode(data):
    """Modul 4+5 - Mengambil semua kode tugas sebagai Set untuk validasi unik."""
    # Modul 5 - Set: kumpulan kode unik
    return {t["kode"].upper() for t in data["tugas"]}


# ===========================================================
# MODUL 4 - Fungsi: Fitur Utama
# ===========================================================

def tambah_tugas(data):
    """
    [+] Tambah Tugas Baru
    Modul 1: Variabel & tipe data
    Modul 2: Kondisi validasi
    Modul 4: Fungsi
    Modul 5: Dictionary untuk menyimpan tugas, Set untuk validasi unik
    Modul 6: Simpan ke JSON
    """
    print("\n" + "="*50)
    print("  [+] TAMBAH TUGAS BARU")
    print("="*50)

    # Modul 5 - Set: ambil semua kode yang ada
    set_kode_ada = ambil_set_kode(data)

    # --- Input Kode Tugas ---
    # Modul 3 - Perulangan: loop sampai input valid
    while True:
        kode = input("  Kode Tugas (unik, contoh: PBO01) : ").strip().upper()
        if not validasi_input_kosong(kode, "Kode Tugas"):
            continue
        if not validasi_kode_unik(kode, set_kode_ada):
            continue
        break

    # --- Input Mata Kuliah ---
    while True:
        matkul = input("  Mata Kuliah                       : ").strip()
        if validasi_input_kosong(matkul, "Mata Kuliah"):
            break

    # --- Input Deskripsi ---
    while True:
        deskripsi = input("  Deskripsi Tugas                   : ").strip()
        if validasi_input_kosong(deskripsi, "Deskripsi"):
            break

    # --- Input Prioritas ---
    while True:
        prioritas_input = input("  Prioritas (1=Tinggi, 2=Sedang, 3=Rendah): ").strip()
        prioritas = validasi_prioritas(prioritas_input)
        if prioritas is not None:
            break

    # Modul 1 - Variabel: counter auto-increment sebagai No urut
    data["counter"] += 1
    no_urut = data["counter"]

    # Modul 5 - Dictionary: struktur data satu tugas
    tugas_baru = {
        "no"       : no_urut,
        "kode"     : kode,
        "matkul"   : matkul,
        "deskripsi": deskripsi,
        "prioritas": prioritas,
        "status"   : "Belum"   # Modul 1 - String default
    }

    # Modul 5 - List: tambahkan ke list tugas
    data["tugas"].append(tugas_baru)

    # Modul 6 - File I/O: simpan ke JSON
    simpan_database(data)

    print(f"\n  [✓] Tugas '{kode}' berhasil ditambahkan!")


def daftar_tugas(data):
    """
    [≡] Daftar Tugas - Tampilkan tabel
    Modul 2: Kondisi filter/tampilan
    Modul 3: Perulangan list
    Modul 4: Fungsi
    Modul 5: List & Dictionary
    """
    print("\n" + "="*75)
    print("  [≡] DAFTAR TUGAS")
    print("="*75)

    # Modul 5 - List: akses list tugas
    list_tugas = data["tugas"]

    # Modul 2 - Kondisi: cek apakah list kosong
    if len(list_tugas) == 0:
        print("  (Belum ada tugas. Silakan tambah tugas terlebih dahulu.)")
        return

    # Header tabel
    print(f"  {'No':<4} {'Kode':<10} {'Mata Kuliah':<18} {'Prioritas':<10} {'Status':<10} Deskripsi")
    print("  " + "-"*73)

    # Modul 3 - Perulangan: iterasi semua tugas
    for t in list_tugas:
        # Modul 2 - Kondisi: label prioritas
        if t["prioritas"] == 1:
            label_p = "★★★ Tinggi"
        elif t["prioritas"] == 2:
            label_p = "★★☆ Sedang"
        else:
            label_p = "★☆☆ Rendah"

        # Modul 1 - String formatting
        deskripsi_pendek = (t["deskripsi"][:25] + "...") if len(t["deskripsi"]) > 25 else t["deskripsi"]
        print(f"  {t['no']:<4} {t['kode']:<10} {t['matkul']:<18} {label_p:<10} {t['status']:<10} {deskripsi_pendek}")

    print("="*75)


def tandai_selesai(data):
    """
    [✓] Tandai Tugas Selesai
    Modul 2: Kondisi pencarian & update status
    Modul 3: Perulangan pencarian
    Modul 4: Fungsi
    Modul 5: Dictionary update
    Modul 6: Simpan perubahan
    """
    print("\n" + "="*50)
    print("  [✓] TANDAI TUGAS SELESAI")
    print("="*50)

    # Tampilkan daftar dulu
    daftar_tugas(data)

    # Modul 2: cek apakah ada tugas
    if len(data["tugas"]) == 0:
        return

    kode_cari = input("\n  Masukkan Kode Tugas yang ingin ditandai selesai: ").strip().upper()

    if not validasi_input_kosong(kode_cari, "Kode Tugas"):
        return

    ditemukan = False
    # Modul 3 - Perulangan: cari tugas berdasarkan kode
    for t in data["tugas"]:
        # Modul 2 - Kondisi: cocokkan kode
        if t["kode"].upper() == kode_cari:
            ditemukan = True
            # Modul 2 - Kondisi: cek apakah sudah selesai
            if t["status"] == "Selesai":
                print(f"  [!] Tugas '{kode_cari}' sudah berstatus Selesai.")
            else:
                # Modul 5 - Dictionary: update value status
                t["status"] = "Selesai"
                # Modul 6 - File I/O: simpan perubahan
                simpan_database(data)
                print(f"  [✓] Tugas '{kode_cari}' berhasil ditandai Selesai!")
            break

    # Modul 2 - Kondisi: jika tidak ditemukan
    if not ditemukan:
        print(f"  [!] Kode tugas '{kode_cari}' tidak ditemukan.")


def hapus_tugas(data):
    """
    [-] Hapus Tugas (hanya tugas berstatus Selesai)
    Modul 2: Kondisi & konfirmasi
    Modul 3: Perulangan pencarian
    Modul 4: Fungsi
    Modul 5: List remove, Dictionary
    Modul 6: Simpan perubahan
    """
    print("\n" + "="*50)
    print("  [-] HAPUS TUGAS")
    print("="*50)
    print("  (Catatan: Hanya tugas berstatus 'Selesai' yang dapat dihapus)")

    # Tampilkan daftar
    daftar_tugas(data)

    # Modul 2: cek apakah ada tugas
    if len(data["tugas"]) == 0:
        return

    kode_cari = input("\n  Masukkan Kode Tugas yang ingin dihapus: ").strip().upper()

    if not validasi_input_kosong(kode_cari, "Kode Tugas"):
        return

    ditemukan = False
    tugas_target = None

    # Modul 3 - Perulangan: cari tugas
    for t in data["tugas"]:
        # Modul 2 - Kondisi: cocokkan kode
        if t["kode"].upper() == kode_cari:
            ditemukan = True
            tugas_target = t
            break

    # Modul 2 - Kondisi: berbagai skenario
    if not ditemukan:
        print(f"  [!] Kode tugas '{kode_cari}' tidak ditemukan.")
        return

    if tugas_target["status"] != "Selesai":
        print(f"  [!] Tugas '{kode_cari}' belum selesai. Hanya tugas Selesai yang bisa dihapus.")
        return

    # Konfirmasi sebelum hapus
    print(f"\n  Tugas yang akan dihapus:")
    print(f"  Kode    : {tugas_target['kode']}")
    print(f"  Matkul  : {tugas_target['matkul']}")
    print(f"  Deskripsi: {tugas_target['deskripsi']}")

    konfirmasi = input("\n  Yakin ingin menghapus? (y/n): ").strip().lower()

    # Modul 2 - Kondisi: konfirmasi
    if konfirmasi == "y":
        # Modul 5 - List: hapus item dari list
        data["tugas"].remove(tugas_target)
        # Modul 6 - File I/O: simpan
        simpan_database(data)
        print(f"  [✓] Tugas '{kode_cari}' berhasil dihapus.")
    else:
        print("  [i] Penghapusan dibatalkan.")


def statistik(data):
    """
    [Σ] Statistik Tugas
    Modul 1: Variabel penghitung
    Modul 2: Kondisi
    Modul 3: Perulangan
    Modul 4: Fungsi
    Modul 5: List, Dictionary
    """
    print("\n" + "="*50)
    print("  [Σ] STATISTIK TUGAS")
    print("="*50)

    list_tugas = data["tugas"]
    total      = len(list_tugas)  # Modul 1 - Variabel integer

    # Modul 2 - Kondisi: jika tidak ada tugas
    if total == 0:
        print("  Belum ada tugas yang tercatat.")
        return

    # Modul 1 - Variabel penghitung
    jumlah_selesai = 0
    jumlah_belum   = 0
    prioritas_1    = 0
    prioritas_2    = 0
    prioritas_3    = 0

    # Modul 3 - Perulangan: hitung tiap status & prioritas
    for t in list_tugas:
        # Modul 2 - Kondisi: hitung berdasarkan status
        if t["status"] == "Selesai":
            jumlah_selesai += 1
        else:
            jumlah_belum += 1

        # Modul 2 - Kondisi: hitung berdasarkan prioritas
        if t["prioritas"] == 1:
            prioritas_1 += 1
        elif t["prioritas"] == 2:
            prioritas_2 += 1
        else:
            prioritas_3 += 1

    # Modul 1 - Variabel float: persentase
    persen_selesai = (jumlah_selesai / total) * 100
    persen_belum   = (jumlah_belum   / total) * 100

    print(f"\n  Total Tugas      : {total}")
    print(f"  ✓ Selesai        : {jumlah_selesai} ({persen_selesai:.1f}%)")
    print(f"  ○ Belum Selesai  : {jumlah_belum} ({persen_belum:.1f}%)")
    print()
    print(f"  Prioritas Tinggi (1): {prioritas_1} tugas")
    print(f"  Prioritas Sedang (2): {prioritas_2} tugas")
    print(f"  Prioritas Rendah (3): {prioritas_3} tugas")

    # Tampilkan tugas tertinggi yang masih belum selesai
    print("\n  --- Tugas Prioritas Tertinggi yang Belum Selesai ---")
    tugas_belum = []
    # Modul 3 - Perulangan: filter tugas belum selesai
    for t in list_tugas:
        # Modul 2 - Kondisi
        if t["status"] == "Belum":
            tugas_belum.append(t)

    # Modul 2 - Kondisi: jika semua selesai
    if len(tugas_belum) == 0:
        print("  Semua tugas sudah selesai. Kerja bagus!")
    else:
        # Urutkan berdasarkan prioritas (Modul 5 - List sort dengan key)
        tugas_belum.sort(key=lambda x: x["prioritas"])
        # Modul 3 - Perulangan: tampilkan top 3 prioritas
        for i, t in enumerate(tugas_belum[:3]):
            print(f"  {i+1}. [{t['kode']}] {t['matkul']} - {t['deskripsi'][:40]}")

    print("="*50)


def tampilkan_menu():
    """Modul 4 - Fungsi: Tampilkan menu utama."""
    print("\n" + "="*50)
    print("       SISTEM TODO LIST AKADEMIK")
    print("="*50)
    print("  [1] [+] Tambah Tugas")
    print("  [2] [≡] Daftar Tugas")
    print("  [3] [✓] Tandai Selesai")
    print("  [4] [-] Hapus Tugas")
    print("  [5] [Σ] Statistik")
    print("  [6] [✗] Keluar")
    print("="*50)


# ===========================================================
# MODUL 3 - Perulangan Utama: while True (Menu Utama)
# ===========================================================

def main():
    """Fungsi utama program. Modul 3 - While loop utama."""

    print("\n" + "#"*50)
    print("#    SELAMAT DATANG DI TODO LIST AKADEMIK    #")
    print("#"*50)

    # Modul 6 - File I/O: load database saat program dimulai
    data = load_database()
    print(f"  [i] Database dimuat. {len(data['tugas'])} tugas tersimpan.")

    # Modul 3 - Perulangan Utama: while True
    while True:
        tampilkan_menu()

        pilihan = input("  Pilih menu [1-6]: ").strip()

        # Modul 2 - Kondisi: routing menu
        if pilihan == "1":
            tambah_tugas(data)

        elif pilihan == "2":
            daftar_tugas(data)

        elif pilihan == "3":
            tandai_selesai(data)

        elif pilihan == "4":
            hapus_tugas(data)

        elif pilihan == "5":
            statistik(data)

        elif pilihan == "6":
            print("\n  [✗] Keluar dari program. Sampai jumpa!")
            break  # Modul 3 - break untuk keluar while loop

        else:
            # Modul 2 - Kondisi: input tidak valid
            print("  [!] Pilihan tidak valid. Masukkan angka 1-6.")

    print("\n" + "#"*50)


# Entry point
if __name__ == "__main__":
    main()
