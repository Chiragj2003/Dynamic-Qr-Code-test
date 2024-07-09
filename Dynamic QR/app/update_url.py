import requests

# URL of the web service
service_url = "http://localhost:8000"

# Unique code for the QR
code = "my-unique-code"

# New URL to redirect to
new_url = "https://www.javatpoint.com/generate-a-qr-code-using-python"

# Update the redirection URL
response = requests.post(f"{service_url}/update/{code}", json={"new_url": new_url})

if response.status_code == 200:
    print("URL updated successfully")
else:
    print(f"Failed to update URL: {response.status_code}, {response.text}")
