import requests

# Shoppy.gg API configuration
shoppy_api_key = "92AvWtrcVeVy9FuTuvm1MuHCNjDmJXU3cHPyRTUqi5SIbz0GYy"  # Replace with your actual Shoppy.gg API key
shoppy_url = "https://shoppy.gg/api/v1/products"  # The endpoint for fetching products

# Headers with the API key
headers = {
    "Authorization": f"Bearer {shoppy_api_key}"
}

# Make the GET request
response = requests.get(shoppy_url, headers=headers)

# Check the response
if response.status_code == 200:
    print("Successfully fetched products:")
    print(response.json())  # Print the JSON response
else:
    print(f"Failed to fetch products. Status Code: {response.status_code}")
    print(f"Response: {response.text}")
