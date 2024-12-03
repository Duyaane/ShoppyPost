import requests

# SMM Service API Configuration
smm_api_key = "c5a39d888c0debe81eea9d6875364d1f"  # Replace with your actual SMM API key
smm_api_url = "https://justanotherpanel.com/api/v2"

# Function to add an order for views using the SMM API
def add_order(service_id, link, quantity):
    payload = {
        "key": smm_api_key,
        "action": "add",
        "service": service_id,
        "link": link,
        "quantity": quantity
    }
    response = requests.post(smm_api_url, data=payload)
    return response.json()

# Main function to get input and place an order
def main():
    # Define fixed values for link, service ID, and quantity
    link = input("Enter the link to the Telegram post you want to boost: ") or "@dujunayanshop"
    service_id = 7384    # Correct service ID for Telegram views
    quantity = 150       # Fixed quantity of 300 views

    # Send the order to the SMM API
    response = add_order(service_id, link, quantity)
    
    # Print the result in the terminal
    if "order" in response:
        print(f"✅ Order placed successfully! Order ID: {response['order']}")
    else:
        print("❌ Failed to place order:", response.get("error", "Unknown error"))

# Run the main function
if __name__ == "__main__":
    main()
