import sys
from undetected_geckodriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from selenium.webdriver.firefox.options import Options
import os

# Check if a file argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
output_basename = os.path.splitext(filename)[0] + "-output"

# Set Firefox options
options = Options()
# options.add_argument("--headless")  # Enable headless mode

# Start the browser with the headless option
driver = Firefox(options=options)

# Open the webpage
driver.get("https://www.chatgpt.com")

# Wait for a specific element to be visible
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.ProseMirror#prompt-textarea'))
    )
    print("Element is now visible.")
except Exception as e:
    print(f"Web page could not load within 10 seconds. Error: {str(e)}")
    driver.quit()
    exit()

# Read file and submit input
try:
    with open(filename, 'r', encoding='utf-8') as file:
        text_content = file.read()
    
    # Write the text to the input field and press Enter
    element.send_keys(text_content)
    element.send_keys(Keys.ENTER)
    
    print("Text successfully submitted.")
except Exception as e:
    print(f"Failed to read the file: {filename}. Error: {str(e)}")
    driver.quit()
    exit()

try:
    # Find the element initially
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-streaming"))
    )

    # Capture the initial content
    previous_content = element.get_attribute("innerHTML")
    start_time = time.time()

    while True:
        current_content = element.get_attribute("innerHTML")
        if current_content != previous_content:
            previous_content = current_content
            start_time = time.time()
        else:
            time.sleep(1)
            new_check = element.get_attribute("innerHTML")
            if new_check == current_content:
                break

        if time.time() - start_time > 20:
            raise TimeoutError("Content did not stabilize, timeout!")

    # Wait for final class change
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "markdown"))
    )

    html_content = element.get_attribute("innerHTML")

    html_output_file = f"{output_basename}.html"
    with open(html_output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Content change complete, HTML saved to {html_output_file}.")

except Exception as e:
    print(f"Content or class change failed! Error: {str(e)}")

finally:
    driver.quit()

try:
    # Run the script
    md_output_file = f"{output_basename}.md"
    result = subprocess.run(["python3", "html_to_md.py", html_output_file], capture_output=True, text=True)
    print(result.stdout)
except Exception as e:
    print(f"html to md error: {str(e)}")
