# Belajar Keyword argument list
# ** = keyword argument list
def create_html(tag, text, **attributes):
  html = f"<{tag}"

  for key, value in attributes.items():
    html = html + f" {key}='{value}'"

  html = html + f">{text}</{tag}>"
  return html

html = create_html("h1", "Hello World", style="font-size: 30px", id="judul")
print(html)