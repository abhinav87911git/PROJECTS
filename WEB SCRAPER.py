#  web scraper for news website
#  here just give the url of the news website and it will print the top 5 headlines

import requests 
from bs4 import BeautifulSoup 

def get_news_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find_all('h3', class_= 'news-title')  # h2, h1, h4, h5, h6
    for headline in headlines[:5]:
        print(headline.get_text())

if __name__ == "__main__":
    news_url = input("Enter the url of the news website: ") # here we can provide a by_default url of any website so that it always give news from there
    get_news_headlines(news_url)        