import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://old.reddit.com/r/confessions/hot/"
SUBREDDIT_NAME_IN_SMALLS = 'confessions'
string_to_strip = f'(self.{SUBREDDIT_NAME_IN_SMALLS})'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
titles_with_spaces = soup.find_all('p', class_='title')
titles = [x.strip().strip(string_to_strip) for x in titles_with_spaces]
