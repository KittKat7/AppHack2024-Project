import requests, json

def query(query: str) -> str:
    return __queryTest(query)
#query

def __queryTest(query: str) -> str:
    response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
    data = response_API.text
    parse_json = json.loads(data)
    active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
    return "Active cases in South Andaman:" + active_case
#queryTest

def __queryStack(query: str) -> str:
    with open("examplequery.json") as f:
        content = f.read()
    parse_json = json.loads(content)
    parsed = parse_json['items'][0]['tags']
    return parsed
#queryStack

if __name__ == "__main__":
    print(query("hi"))



"""
from stackapi import StackAPI

title_search_string = 'How can I search questions by titles using the StackExchange API?'

SITE = StackAPI('stackoverflow')
questions = SITE.fetch('search/advanced', title = title_search_string)
print(questions)
"""