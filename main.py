from undetected_geckodriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from selenium.webdriver.firefox.options import Options

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
    with open('./prompt.txt', 'r') as file:
        text_content = file.read()
    
    # Write the text to the input field and press Enter
    element.send_keys(text_content)
    element.send_keys(Keys.ENTER)
    
    print("Text successfully submitted.")
except Exception as e:
    print(f"Failed to read the file: prompt.txt. Error: {str(e)}")
    driver.quit()
    exit()

try:
    # Old and new class values
    old_class = "result-streaming markdown prose w-full break-words dark:prose-invert dark"
    new_class = "markdown prose w-full break-words dark:prose-invert dark"

    # Find the element with the old class initially
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "result-streaming"))
    )

    # Capture the initial content
    previous_content = element.get_attribute("innerHTML")

    # Start the wait time (maximum 20 seconds)
    start_time = time.time()

    while True:
        current_content = element.get_attribute("innerHTML")

        # If content is still changing, keep waiting
        if current_content != previous_content:
            previous_content = current_content  # Update with new content
            start_time = time.time()  # Reset the timer
        else:
            # If content stops changing, wait for 1 second and check again
            time.sleep(1)
            new_check = element.get_attribute("innerHTML")
            if new_check == current_content:  # If content hasn't changed, proceed
                break

        # If maximum wait time (20 seconds) has passed, exit
        if time.time() - start_time > 20:
            raise TimeoutError("Content did not stabilize, timeout!")

    # After content has stopped changing, check for the class change
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "markdown"))
    )

    # If the class change is complete, save the HTML content to a file
    html_content = element.get_attribute("innerHTML")

    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Content change complete, and class has successfully changed! HTML saved to file.")

except Exception as e:
    print(f"Content or class change failed! Error: {str(e)}")

finally:
    driver.quit()

try:
    # Run the script
    result = subprocess.run(["python", "html_to_md.py"], capture_output=True, text=True)

    # Print the output
    print(result.stdout)
except Exception as e:
    print(f"html to md error: {str(e)}")
