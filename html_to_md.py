import os
import sys
import html2text
from bs4 import BeautifulSoup

def convert_html_to_md(html_file):
    print(f"İşlem başlatıldı. Girdi dosyası: {html_file}")
    
    # Çıktı dosyasının adını belirle
    md_file = os.path.splitext(html_file)[0] + ".md"
    print(f"Çıktı dosyası: {md_file}")
    
    # HTML dosyasını oku
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        print("HTML dosyası başarıyla okundu.")
    except Exception as e:
        print(f"HTML dosyası okunurken hata oluştu: {e}")
        return
    
    # BeautifulSoup ile HTML temizleme
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        clean_html = soup.prettify()
        print("HTML başarıyla temizlendi ve prettify edildi.")
    except Exception as e:
        print(f"BeautifulSoup işlemi sırasında hata oluştu: {e}")
        return
    
    # HTML'i Markdown'a çevir
    try:
        converter = html2text.HTML2Text()
        converter.ignore_links = False  # Linkleri koru
        converter.ignore_images = False # Görselleri koru
        markdown_content = converter.handle(clean_html)
        print("HTML başarıyla Markdown formatına dönüştürüldü.")
    except Exception as e:
        print(f"Markdown dönüşümü sırasında hata oluştu: {e}")
        return
    
    # Markdown dosyasına yaz
    try:
        with open(md_file, 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        print(f"Dönüştürme tamamlandı: {md_file}")
    except Exception as e:
        print(f"Markdown dosyasına yazılırken hata oluştu: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python script.py <html_dosyası>")
    else:
        html_file = sys.argv[1]
        print(f"Girdi dosyası kontrol ediliyor: {html_file}")
        if os.path.exists(html_file):
            print("Dosya bulundu, işleme başlanıyor...")
            convert_html_to_md(html_file)
        else:
            print("Hata: Belirtilen HTML dosyası bulunamadı.")
