# Belajar Tipe Data Dictionary

pelanggan = {
  "Name" : "Ahdan",
  "Age" : 17,
  "Address" : "Semarang"
}

name = pelanggan["Name"]
age = pelanggan["Age"]
address = pelanggan["Address"]

# for key in pelanggan:
#   value = pelanggan[key]
#   print(f"{key} : {value}")

# print(pelanggan.items())
# dict_items([('Name', 'Ahdan'), ('Age', 17), ('Address', 'Semarang')])

# for key in pelanggan.items():
#   print(f"{key[0]} : {key[1]}")

# menambahkan 
pelanggan["Gender"] = "Laki-laki"

# mengubah
pelanggan["Age"] = 16

# menghapus
del pelanggan["Address"]

for key, value in pelanggan.items():
  print(f"{key} : {value}")