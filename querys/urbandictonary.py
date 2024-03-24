import requests
import database as db

# Function to search the database for a word
def __search_database(word):
    return db.queryDefinition(word)


def __search_urban_dictionary(word):
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

# Main function to search for a word
def queryUrban(word):
    definition = __search_database(word)
    if definition is not None:
       return (f"Definition from database: {definition}")
    else:
        definition = __search_urban_dictionary(word)
        db.insertDefinition(word, definition)
        return (definition)


