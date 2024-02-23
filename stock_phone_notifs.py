import requests
from twilio.rest import Client
STOCK_NAME = {STOCK_NAME-> str}
STOCK_KEY = ''
COMPANY_NAME = {NAME-> str}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = os.environ.get('NEWS_API_KEY')
TWILIO_SID = os.environ.get("TWILIO_SID')
TWILIO_AUTH = os.environ.get("TWILIO_AUTH_TOKEN')

stock_params = {'function': 'TIME_SERIES_DAILY', 'symbol': STOCK_NAME, 'apikey': STOCK_KEY}

prices = requests.get(STOCK_ENDPOINT, params=stock_params)
data = prices.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
y_close_price = yesterday_data['4. close']

day_b4_price = data_list[1]
day_b4_close_price = day_b4_price['4. close']

difference = float(y_close_price)-float(day_b4_close_price)
updown = None
if difference > 0:
    updown = '🔺'
else:
    updown = '🔻'

diff_percentage = round((difference/float(y_close_price)) * 100)

if abs(diff_percentage)> 1:
    news_params = {'apiKey': NEWS_KEY, 'qInTitle': COMPANY_NAME}
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news = news_response.json()['articles']
    three_articles = news[:3]
    
    articles_list = [f'{STOCK_NAME}{updown}{diff_percentage}% Headline: {article["title"]}.\nBrief: {article["description"]}.' for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH)

    for article in articles_list:
        message = client.messages.create(
            body = article,
            from_ = {TWILLIO_NUMBER-> str},
            to = {YOUR_NUMBER-> str}
            )
