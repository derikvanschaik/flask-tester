import requests 

# Fetches data from the api 
def fetch_data():
    response = requests.get("https://type.fit/api/quotes") 
    return response.json()
    
# parses the data from the api fetch above into a 
# dict which maps authors to a list of their quotes
# and a list of these authors 
# RETURNS: a list of authors and a dict 
def get_authors_and_quotes():
    data = fetch_data() 
    quotes = {}
    images = {} 
    authors = [] 
    for pair in data:
        # we want to reassign null authors to unknown 
        if not pair['author']:
            pair['author'] = 'Unknown'

        if pair['author'] in quotes: 
            quotes[pair['author']].append(pair['text'])

        else:
            quotes[pair['author']] = [pair['text']]
            authors.append(pair['author'])
    return authors, quotes