# ShoppyPost

**ShoppyPost** is a Python-based automation tool designed to simplify and enhance product promotion for sellers using the Shoppy.gg platform. It allows you to fetch product details from Shoppy.gg and automatically post them to a Telegram channel, making it easy to manage and promote your products effectively.

---

## Features

- Fetches product details (title, image, and link) from the Shoppy.gg API.
- Automatically posts products to a Telegram channel with customizable messages.
- Prevents duplicate posts by logging already-sent products.
- Lightweight, easy to use, and fully customizable.

---

## Requirements

- **Python 3.8+** installed on your system.
- Dependencies:
  - `requests`
  - `python-telegram-bot`
- **Shoppy.gg API Key**: Required to fetch product details.
- **Telegram Bot Token**: Required to post messages to Telegram.

## Installation

Follow these steps to set up and run ShoppyPost on your system:

1. **Clone the Repository:**
   Download the repository to your local machine:
   ```bash
   git clone https://github.com/Duyaane/ShoppyPost.git
   cd ShoppyPost
Install Python Dependencies: Ensure you have Python 3.8 or higher installed. Then, install the required libraries using pip:

pip install -r requirements.txt
Create a .env File: Store sensitive information like API keys securely in a .env file:

touch .env
Add API Keys to the .env File: Open the .env file in a text editor and add the following lines:

SHOPPY_API_KEY=your_shoppy_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
CHANNEL_ID=@your_channel_id_here
Replace your_shoppy_api_key_here, your_telegram_bot_token_here, and @your_channel_id_here with your actual credentials.

Run the Tool: Start the script by running:

python shoppy.py
Verify Outputs:

Products should now be fetched from Shoppy.gg and posted to your Telegram channel.
Check the send.txt log file to see which products have already been sent.
Usage
Run the script using:

python shoppy.py
Products will be posted to the specified Telegram channel.

Customize the footer and message templates in the shoppy.py file as needed.

Limitations
The tool relies on Shoppy.gg's API, which may have rate limitations.
Ensure your API key and Telegram bot token are valid and correctly configured.
Contributing
Feel free to submit issues or pull requests for improvements or feature requests.
