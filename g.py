import requests

def get_location(user_id):
    url = f"https://discordapi.com/api/v9/users/{user_id}/?query=location"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "location" in data:
            return data["location"]
    return None

user_id = input("discorddaki kişinin idsini girin: ")
location = get_location(user_id)
if location:
    print(f"kişinin babaanne konumu: {location}")
else:
    print("konum bulunamadı")
