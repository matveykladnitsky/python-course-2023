import requests

# KEYS
WEATHER_API_KEY = '38976e12e5d7df6074ef54aba51ca4ec'
# 	newsapi.org
NEWS_API_KEY = '82bdde466d9540bcad4c1544d49379c2'

# WEATHER
CITY_NAME = "Saint-Petersburg"


def make_request_to_weather_api():
    LAT = 59
    LON = 30
    return f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={WEATHER_API_KEY}'


def format_weather_data(data):
    print(f'Погода в городе {CITY_NAME}:\n')
    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    print(f'Погода: {weather} - {description}')
    print(f'Влажность: {humidity}')
    print(f'Давление: {pressure}')


def fetch_weather():
    try:
        result = requests.get(make_request_to_weather_api()).json()
        format_weather_data(result)
    except:
        print('Не удалось вывести погоду в городе ' + CITY_NAME)

# NEWS


def make_request_to_news_api():
    return f'https://newsapi.org/v2/everything?q=AI&from=2024-01-01&sortBy=popularity&apiKey={NEWS_API_KEY}'


def format_articles(articles):
    for article in articles:
        print(
            f'author - {article["author"]}\ntitle - {article["title"]}\nurl - {article["url"]}\n\n')


def fetch_news():
    try:
        result = requests.get(make_request_to_news_api()).json()
        articles = result['articles']
        format_articles(articles)
    except:
        print('Не удалось вывести новости')


fetch_weather()
fetch_news()
