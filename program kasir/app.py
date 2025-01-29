from func import *
import pyfiglet

ucapan_text = pyfiglet.figlet_format("Kasir Canggih", font="slant")

warna_text = Fore.CYAN + ucapan_text  + reset

print(warna_text)

while True:
  print(Fore.CYAN + "=== Menu Kasir ====" + reset + "\n")
  print(Fore.YELLOW + "1. Daftar Barang" + reset)
  print(Fore.GREEN + "2. Saldo" + reset)
  print(Fore.MAGENTA + "3. Beli Barang" + reset)
  print(Fore.RED + "4. Keluar" + reset + "\n")
  print(Fore.CYAN + "===================" + reset + "\n")

  perintah = input("Pilih Menu : ")

  if perintah == "1":
    daftar_barang()
  elif perintah == "2":
    saldo()
  elif perintah == "3":
    beli_barang()

  if perintah == "4":
    break

print(Fore.RED + "Program Selesai Kakak 🙏" + reset)