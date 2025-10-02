# Belajar Keyword Argument List

# # Contoh 1
# def create_html(tag, text):
#     html = f"<{tag}>{text}</{tag}>"
#     return html

# html = create_html("p", "Hello, Python")
# print(html)  # Output: <p>Hello, Python</p>
# html = create_html("a", "Ini link")
# print(html)  # Output: <a>Ini link</a>

# # Contoh 2 // Keyword Argument List, tapi disetiap creat html ada nilai defaultnya
# def create_html(tag, text, href=""):
#     html = f"<{tag}> href='{href}'{text}</{tag}>"
#     return html

# html = create_html("p", "Hello, Python")
# print(html)  
# html = create_html("a", "Ini link", href="https://www.google.com")
# print(html)

# # Contoh 3 // Keyword Argument List, 
# def create_html(tag, text, **attributes):
#     html = f"<{tag}>{text}</{tag}>"
#     print(attributes)  # Menampilkan atribut tambahan sebagai dictionary
#     return html

# html = create_html("p", "Hello, Python", style="paragraf")
# print(html) 
# html = create_html("a", "Ini link", href="https://www.google.com", style="link")
# print(html)  
# # dengan menambahkan **attributes, kita bisa menambahkan atribut tambahan seperti href, style, dll tanpa harus mendefinisikannya satu per satu dalam parameter fungsi.

# Contoh 4 // Keyword Argument List
def create_html(tag, text, **attributes):
    html = f"<{tag}"
    
    for key, value in attributes.items():
        html = html + f" {key}='{value}'"
    
    html= html + f">{text}</{tag}>"
    return html

html = create_html("p", "Hello, Python", style="paragraf")
print(html) 
html = create_html("a", "Ini link", href="https://www.google.com", style="link")
print(html)
html = create_html("div", "Ini div", style="contoh")
print(html)
# menggunakan loop untuk menambahkan semua atribut tambahan ke dalam tag HTML secara dinamis.
# Dengan cara ini, kita dapat menambahkan atribut HTML apa pun tanpa harus mengubah definisi fungsi.


# catatan:
# # 1. Keyword Argument List menggunakan **attributes
# 2. Argument list menggunakan *list
# 3. Default Argument menggunakan param=nilai
# 4. Urutan penulisan param harus: param, default param, *list, **attributes
# kalo kita ingin menambahkan custom param/argumen, kita bisa memanfaatkan fitur keyword argument list ini.
