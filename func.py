# Belajar Module

def say_hello(nama):
  return f"Hello {nama}"

def total(*list_angka):
  total = 0
  for angka in list_angka:
    total += angka
  return total