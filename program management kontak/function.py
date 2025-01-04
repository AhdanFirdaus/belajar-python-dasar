# Program Management Kontak

def display_kontak(daftar_kontak):
  for kontak in daftar_kontak:
    print("-----")
    print(f"Nama : {kontak['nama']}")
    print(f"Email : {kontak['email']}")
    print(f"No Telepon : {kontak['telepon']}")
    print("-----")

def new_kontak():
  nama = input("Masukan Nama : ")
  email = input("Masukan Email : ")
  telepon = input("Masukan No Telepon : ")

  kontak = {
    "nama" : nama,
    "email" : email,
    "telepon" : telepon
  }

  return kontak

def hapus_kontak(daftar_kontak):
  telepon = input("Masukan No Telepon yang akan di hapus : ")

  index = -1

  for i in range(0, len(daftar_kontak)):
    kontak = daftar_kontak[i]
    if kontak["telepon"] == telepon:
      index = i
      break

  if index == -1:
    print("Data Tidak Ditemukan")
  else:
    del daftar_kontak[index]
    print("Data Berhasil Dihapus")

def cari_kontak(daftar_kontak):
  nama_yang_dicari = input("Masukan Nama yang akan dicari : ")

  for kontak in daftar_kontak:
    nama = kontak["nama"]
    if nama.lower().find(nama_yang_dicari.lower()) != -1:
         print("-----")
         print(f"Nama : {kontak['nama']}")
         print(f"Email : {kontak['email']}")
         print(f"No Telepon : {kontak['telepon']}")
         print("-----")