# Belajar default argument value

def say_hello(name="ahdan", last_name=""):
  print(f"Hello {name} - {last_name}")

say_hello()
say_hello("ahdan", "firdaus")
say_hello(last_name="joko")
say_hello(name="firdaus", last_name="joko")