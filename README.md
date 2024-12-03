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

1. Clone the Repository:
   ```bash
   git clone https://github.com/Duyaane/ShoppyPost.git
   cd ShoppyPost
Install Python Dependencies:

pip install -r requirements.txt
Create a .env File:

touch .env
Add API Keys to the .env File:

SHOPPY_API_KEY=your_shoppy_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
CHANNEL_ID=@your_channel_id_here
Run the Tool:

python shoppy.py
Usage
Run the script using:

python shoppy.py
Products will be posted to the specified Telegram channel.

Customize the footer and message templates in the shoppy.py file as needed.
