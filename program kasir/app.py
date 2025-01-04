import func

while True:
  print("=== Menu Kasir ====\n")
  print("1. Daftar Barang")
  print("2. Saldo")
  print("3. Beli Barang")
  print("4. Keluar\n")
  print("===================\n")

  perintah = input("Pilih Menu : ")

  if perintah == "1":
    func.daftar_barang()
  elif perintah == "2":
    func.saldo()
  elif perintah == "3":
    func.beli_barang()

  if perintah == "4":
    break

print("Program Selesai Kakak 🙏")