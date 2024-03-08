import requests

def get_location(name):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={name}&key=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "OK":
        return data["results"][0]["formatted_address"]
    else:
        return "Başarısız"

name = input("discord ad gir: ")
location = get_location(name)
print(f"Babaannesinin konumu: {location}")
