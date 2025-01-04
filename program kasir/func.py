barang = {
  "apel" : 10000,
  "jeruk" : 20000,
  "mangga" : 30000
}

uangku = 1000000000000000000

def daftar_barang():
  print("Daftar Barang : ")
  for nama, harga in barang.items():
    print(f"- {nama} : Rp. {harga}")

def saldo():
  print(f"Saldo Kamu Kak : Rp. {uangku} \n")

def beli_barang():
  daftar_barang()
  global uangku
  barang_yang_dibeli = input("Silahkan Pilih Barang : ").lower()
  jumlah_barang = int(input("Silahkan Masukan Jumlah Barang : "))
  harga_barang = barang[barang_yang_dibeli]
  total_harga = harga_barang * jumlah_barang
  if total_harga > uangku:
    print("Uangmu ga cukup kakak :) \n")
  else:
    uangku -= total_harga
    print(f"Barang {barang_yang_dibeli} berhasil dibeli \n")
