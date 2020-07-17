import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=e13354cee76e4193baef90f119a8f45f')
headlines = []

def GetNews():

    print("-GATHERING NEWS")

    response = requests.get(url)
    response_json = response.json()

    for news in response_json['articles']:
        headlines.append(news['title'])

    return headlines