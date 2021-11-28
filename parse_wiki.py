from bs4 import BeautifulSoup
import requests

def get_image_from_wiki(name):
    url = "https://en.wikipedia.org/wiki/" + name 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    try:
        # first image on any wikipedia page is usually the one we need 
        image = soup.find("a", class_="image")
        # comes without the https:// part so we need to add this in 
        return "https:" + image.img['src']
    except Exception as e:
        return None 
 