# belajar argument list
# dinamis dan bentuknya list []
# kalau mau menambahkan parameter yang lain, maka argument list harus di akhiri dengan * dan ada di akhir

def jumlahkan(x, *list_angka):
  total = 0
  for angka in list_angka:
    total += angka
  print(f"Total {list_angka} = {total}")

jumlahkan(10, 10, 10, 10, 10, 10)