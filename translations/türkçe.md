# ChatGPT.com İçin Selenium Tarayıcı Otomasyonu

## Genel Bakış

Bu proje, **undetected-geckodriver** ve **Firefox** kullanarak ChatGPT ile etkileşimleri otomatikleştiren bir araçtır. **ChatGPT.com** web sitesine yazılı metin göndermenize ve alınan yanıtı kaydetmenize olanak tanır — tarayıcıyı manuel olarak açmaya gerek kalmadan.

https://github.com/user-attachments/assets/4fab5bb3-dfbf-4673-b52f-7efb3c282b3c

## Gereksinimler

**Python 3.11.2 ile test edilmiştir.**

Başlamak için aşağıdaki Python paketlerini kurmanız gerekecek:

```shell
pip install undetected-geckodriver beautifulsoup4 html2text
```

### undetected-geckodriver Gereksinimleri
- Firefox
- Python >= 3.6
- Selenium >= 4.10.0
- Psutil >= 5.8.0

## İş Akışı

1. **Giriş Dosyası**: `prompt.txt` adında bir dosya oluşturun ve ChatGPT'ye göndermek istediğiniz mesajı yazın.
2. **Çıktı Dosyası**: ChatGPT'nin verdiği yanıt, `output.md` dosyasına kaydedilecektir.

## Yazılım Desteği

- **İşletim Sistemi**: Bu araç yalnızca **Linux** üzerinde çalışacak şekilde tasarlanmıştır.
- **Tarayıcı**: Bu script, **Firefox** kullanarak **undetected-geckodriver** ile çalışacak şekilde yapılandırılmıştır.

## Amaç

Bu aracın temel amacı, ChatGPT ile etkileşimleri hızlandırmak ve otomatikleştirerek daha verimli hale getirmektir.

## Kurulum ve Kullanım

### Terminal Komutları

1. Depoyu klonlayın:
   ```shell
   git clone https://github.com/HTTPS-Miner/chatgpt
   cd chatgpt
   ```

2. Sanal bir ortam oluşturun:
   ```shell
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Gerekli bağımlılıkları yükleyin:
   ```shell
   pip install undetected-geckodriver beautifulsoup4 html2text
   ```

4. Bulunduğunuz klasöre bir `prompt.txt` dosyası oluşturun ve ChatGPT'ye göndermek istediğiniz mesajı yazın.

5. Aracı çalıştırmak için:
   ```shell
   python3 main.py
   ```

Tarayıcı ekranının açılmasını istemiyorsanız, işlemi tarayıcıyı açmadan gerçekleştirmek için `main.py` dosyasının 12. satırındaki yorumu kaldırabilirsiniz.