# Belajar Method return value
# method biasa = prosedur
# method return value = fungsi

def jumlahkan(*list_angka):
  total = 0
  for angka in list_angka:
    total += angka
  return (list_angka,total) # menggunakan tuple

list_angka, total = jumlahkan(10, 10, 10, 10, 10)

# Mengambil data total?
print(f"Total {list_angka} = {total}")