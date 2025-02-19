### English Version - README.md

# Selenium Browser Automation for ChatGPT.com

## Overview

This project automates interactions with ChatGPT on the [ChatGPT.com](https://chat.openai.com/) website using **undetected-geckodriver** and **Firefox**. The script allows you to send text input from a file, receive the response from ChatGPT, and save it to an output file — all without manually opening a browser.

https://github.com/user-attachments/assets/4fab5bb3-dfbf-4673-b52f-7efb3c282b3c

## Requirements

**Tested with Python 3.11.2**

To get started, you'll need to install the following Python packages:

```shell
pip install undetected-geckodriver beautifulsoup4 html2text
```

### **undetected-geckodriver Requirements**
- Firefox
- Python >= 3.6
- Selenium >= 4.10.0
- Psutil >= 5.8.0

## Workflow

1. **Input File**: Create a file called `prompt.txt` and write your message to ChatGPT.
2. **Output File**: The response from ChatGPT will be saved in the `output.md` file.

## Software Support

- **Operating System**: This tool is designed to run on **Linux** only.
- **Browser**: **Firefox** is required to run this script using **undetected-geckodriver**.

## Purpose

The primary goal of this tool is to streamline and automate interactions with ChatGPT, making it faster and more efficient.

## Installation and Usage

### Terminal Commands

1. Clone the repository:
   ```shell
   git clone https://github.com/HTTPS-Miner/chatgpt
   cd chatgpt
   ```

2. Create a virtual environment:
   ```shell
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the required dependencies:
   ```shell
   pip install undetected-geckodriver beautifulsoup4 html2text bs4
   ```

4. Create a `prompt.txt` file in the current directory and write the message you want to send to ChatGPT.

5. To run the tool:
   ```shell
   python3 main.py prompt.txt
   ```

If you want to avoid opening the browser window, simply uncomment line 12 in main.py to perform the operation without opening the browser.