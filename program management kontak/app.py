# Program Management Kontak

import function

# List of dictionary
daftar_kontak = []
daftar_kontak.append({
  "nama" : "Ahdan",
  "email" : "AqT0M@example.com",
  "telepon" : "081234567890"
})

# Menu Program
while True:
  print("# Menu")
  print("1. Daftar Kontak")
  print("2. Tambah Kontak")
  print("3. Hapus Kontak")
  print("4. Cari Kontak")
  print("0. Keluar Program")

  menu = input("Pilih menu : ")

  if menu == "0":
    break
  elif menu == "1":
    function.display_kontak(daftar_kontak)
  elif menu == "2":
    kontak = function.new_kontak()
    daftar_kontak.append(kontak)
  elif menu == "3":
    function.hapus_kontak(daftar_kontak)
  elif menu == "4":
    function.cari_kontak(daftar_kontak)
  else:
    print("Menu Tidak Tersedia")

print("Program Selesai")