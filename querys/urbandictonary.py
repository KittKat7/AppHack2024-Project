import requests

def queryUrban(word):
    url = f"https://api.urbandictionary.com/v0/define?term={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data["list"]) > 0:
            return data["list"][0]["definition"]
        else:
            return "No definitions found for this term."
    else:
        return "Failed to retrieve data from Urban Dictionary."
