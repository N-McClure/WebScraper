#Imported Libraries:
import requests
from bs4 import BeautifulSoup

#Gets the Site URL to Scrape from User:
url = input("Enter FULL URL of the Site to Scrape: ")
response = requests.get(url)

#Gets the searched tag from the Site's HTML and prints it:
soup = BeautifulSoup(response.text, 'html.parser')
SearchedTag = input("Enter the tag of the Site's HTML that you want to Scrape and See: ")

print(soup.find_all(SearchedTag))
