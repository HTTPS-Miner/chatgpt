import os
import html2text
from bs4 import BeautifulSoup

def convert_html_to_md(html_file, md_file):
    # HTML dosyasını oku
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # BeautifulSoup ile HTML temizleme
    soup = BeautifulSoup(html_content, 'html.parser')
    clean_html = soup.prettify()
    
    # HTML'i Markdown'a çevir
    converter = html2text.HTML2Text()
    converter.ignore_links = False  # Linkleri koru
    converter.ignore_images = False # Görselleri koru
    markdown_content = converter.handle(clean_html)
    
    # Markdown dosyasına yaz
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Dönüştürme tamamlandı: {md_file}")

# Dosya yolları
html_file = "./output.html"
md_file = "./output.md"

# Dönüştürme işlemini çalıştır
if os.path.exists(html_file):
    convert_html_to_md(html_file, md_file)
else:
    print("Belirtilen HTML dosyası bulunamadı.")

