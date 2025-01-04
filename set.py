# Belajar Set

# list => []
# tuple => ()
# set => {} => data harus unik tidak boleh duplikat
# tidak bisa akses index
# hanya akses index pakai for loop
# posisi index berubah ubah

nama = {"ahdan", "budi", "firdaus", "budi", "dadan", "firdaus"}
# print(set)

# menambah data
nama.add("joko")

for data in nama:
  print(data)

# menghapus data
nama.remove("firdaus")
print(nama)