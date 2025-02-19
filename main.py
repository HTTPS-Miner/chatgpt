import os
import sys
import time
import subprocess
from undetected_geckodriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# Komut satırından input dosyasını al
if len(sys.argv) < 2:
    print("Kullanım: python script.py <input_file>")
    sys.exit(1)

input_file = sys.argv[1]

# Benzersiz işlem ID oluştur
process_id = str(os.getpid())
output_file = f"output_{process_id}.html"

# prompt.txt içeriğini önceden cache'le
with open(input_file, 'r', encoding='utf-8') as file:
    cached_prompt = file.read()

def initialize_driver():
    options = Options()
    # options.add_argument("--headless")  # Başsız mod aktif etmek için yorum satırını kaldırın
    return Firefox(options=options)

def submit_prompt(driver):
    try:
        driver.get("https://www.chatgpt.com")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ProseMirror#prompt-textarea'))
        )
        element.send_keys(cached_prompt)
        element.send_keys(Keys.ENTER)
        print("Metin başarıyla gönderildi.")
    except Exception as e:
        print(f"Metin gönderme başarısız! Hata: {str(e)}")
        driver.quit()
        exit()

def wait_for_response(driver, output_file):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "result-streaming"))
        )
        previous_content = element.get_attribute("innerHTML")
        start_time = time.time()
        
        while True:
            current_content = element.get_attribute("innerHTML")
            if current_content != previous_content:
                previous_content = current_content
                start_time = time.time()
            else:
                time.sleep(1)
                if element.get_attribute("innerHTML") == current_content:
                    break
            if time.time() - start_time > 20:
                raise TimeoutError("İçerik zamanında değişmedi!")

        final_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "markdown"))
        )
        html_content = final_element.get_attribute("innerHTML")
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"Yanıt kaydedildi: {output_file}")
    except Exception as e:
        print(f"Yanıt alınamadı! Hata: {str(e)}")
    finally:
        driver.quit()

def convert_to_markdown(output_file):
    try:
        result = subprocess.run(["python", "html_to_md.py", output_file], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"HTML'den Markdown'a dönüşüm hatası: {str(e)}")

if __name__ == "__main__":
    driver = initialize_driver()
    submit_prompt(driver)
    wait_for_response(driver, output_file)
    convert_to_markdown(output_file)
