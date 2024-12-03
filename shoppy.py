import asyncio
import random
import requests
from telegram import Bot
from telegram.constants import ParseMode
import os
import subprocess  # Import subprocess to run another script

# Your API and Telegram configuration
shoppy_api_key = "92AvWtrcVeVy9FuTuvm1MuHCNjDmJXU3cHPyRTUqi5SIbz0GYy"  # Replace with your actual Shoppy.gg API key
telegram_bot_token = "7877790327:AAE4RwQdt_leXA32jpk-x1tktTtCDKUl8kY"  # Replace with your actual Telegram bot token
CHANNEL_ID = "@dujunayanshop"  # Replace with your actual channel ID

# API endpoint to fetch products from Shoppy.gg
shoppy_url = "https://shoppy.gg/api/v1/products"
headers = {
    "Authorization": shoppy_api_key
}

# Path to log file to track sent product titles
log_file_path = "/Users/mac/Desktop/bots/send.txt"  # Update to your preferred path

# Footer for each message
footer = """
———————————————————————

**Telegram Owner**   : [https://t.me/dujunayan](https://t.me/dujunayan)
**Shop Link**               : [https://shoppy.gg/@Dujunayan](https://shoppy.gg/@Dujunayan)
**Payment Methods** : PayPal, BTC, LTC, ETH, Binance, or Other Cryptos
"""

# Async function to send a message for each product
async def send_post(image_url, title, product_link):
    bot = Bot(token=telegram_bot_token)
    caption = f"🔥 **{title}**\n\n✅ Buy Now: {product_link}\n" + footer
    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=image_url,
        caption=caption,
        parse_mode=ParseMode.MARKDOWN
    )

# Load sent product titles to avoid duplicates
def load_sent_titles():
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as file:
            return set(line.strip() for line in file)
    return set()

# Save a new product title to the log
def save_sent_title(title):
    with open(log_file_path, 'a') as file:
        file.write(f"{title}\n")

# Main function to fetch products and send unique random ones to Telegram
async def main():
    # Fetch products from Shoppy.gg API
    response = requests.get(shoppy_url, headers=headers)
    if response.status_code == 200:
        products = response.json()

        # Load sent titles from log file
        sent_titles = load_sent_titles()

        # Filter products to exclude already-sent titles
        unsent_products = [p for p in products if p['title'] not in sent_titles]

        # Select 2 random unsent products if available
        selected_products = random.sample(unsent_products, 2) if len(unsent_products) >= 2 else unsent_products
        
        # Send each selected product to Telegram and log the title
        for product in selected_products:
            image_url = product['image']['url']
            title = product['title']
            product_link = f"https://shoppy.gg/product/{product['id']}"
            await send_post(image_url, title, product_link)
            save_sent_title(title)  # Log the title as sent

    else:
        print("Failed to retrieve products:", response.status_code, response.text)

    # Run smm.py after completion
    print("Running smm.py after sending posts...")
    subprocess.run(["python3", "/Users/mac/Desktop/bots/smm.py"])  # Replace with the actual path to smm.py

# Run the main function
asyncio.run(main())
