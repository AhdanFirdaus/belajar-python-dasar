from colorama import Fore, Style

reset = Style.RESET_ALL

barang = {
  "apel" : 10000,
  "jeruk" : 20000,
  "mangga" : 30000
}

uangku = 1000000000000000000

def daftar_barang():
  print(Fore.YELLOW + "Daftar Barang" + reset)
  for nama, harga in barang.items():
    print(f'- {nama} : {Fore.YELLOW + "Rp." + str(harga) + reset}')

def saldo():
  print(f'Saldo Kamu Kak : {Fore.GREEN + "Rp." + str(uangku)} \n')

def beli_barang():
    global uangku

    barang_yang_dibeli = input("Silahkan Pilih Barang : ").lower()
    jumlah_barang = int(input("Silahkan Masukan Jumlah Barang : "))

    # Gunakan .get() untuk menghindari KeyError
    harga_barang = barang.get(barang_yang_dibeli)

    if harga_barang is None:
        print(f"{Fore.RED}Barang tidak ada kakak :({Style.RESET_ALL}\n")
    elif total_harga := harga_barang * jumlah_barang > uangku:
        print(f"{Fore.YELLOW}Uangmu ga cukup kakak :){Style.RESET_ALL}\n")
    else:
        uangku -= total_harga
        print(f"{Fore.MAGENTA}Barang {barang_yang_dibeli} berhasil dibeli{Style.RESET_ALL}\n")
