import requests, os, lxml, pytz
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class PriceBot:
    def __init__(self):
        self.TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
        self.TWILIO_SECRET = os.environ.get('TWILIO_API_SECRET')
        self.TWILIO_SID = os.environ.get('TWILIO_SID')
        self.TWILIO_PHONE = os.environ.get('TWILIO_PHONE_NUMBER')
        self.URL = None
        self.TO_NUMBER = None
        
#Tell bot what course u want to pricetrack
    def Introduce_urself(self):
        course = input(" Hi! I'm a Udemy Price tracker bot. Please provide the URL for the course whose price you'd like to track: ")
        link = course
        number = input('What\'s your phone number? I promise not to share it.')
        self.URL = link
        self.TO_NUMBER = number
        
    def getPrice(self, url):
        self.CHROMEDRIVE_PATH = os.environ.get('CHROMEDRIVER_EXE')
        self.header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    }
#Udemy doesn't allow BeautifulSoup on its site and BS can't handle JS
#response = requests.get(url, headers=header)
#soup = BeautifulSoup(response.content, "lxml")

        options = Options()
        options.add_argument('--headless')
        browser = webdriver.Chrome(executable_path=self.CHROMEDRIVE_PATH, options=options)
        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        
        price = soup.find(class_="ud-sr-only").get_text()
#price_without_currency = price.split("$")[1] not always needed- inspect element
        price_as_float = float(price)
        
        course_name = soup.find(class_="ud-heading-xl clp-lead__title clp-lead__title--small").get_text()
    
#Use Twilio API to send a message when the price falls below an average sale threshold
    def sendNotification(self, price):
            if price < 30.0:
                message = f'Hey! Your wishlist course {self.course_name} might be on sale. Current price: {self.price_as_float}. See here: {self.URL}'
                client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                body = message,
                from_ = {self.TWILIO_PHONE},
                #to = {self.TO_NUMBER->str}
                )
            else:
                message = f'Hey! It doesn\'t look like your wishlist course {self.course_name} is on sale yet. I\'ll keep checking for you :)'
                client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                body = message,
                from_ = {self.TWILIO_PHONE},
                #to = {self.TO_NUMBER->str}
                )

pricebot = PriceBot
pricebot.Introduce_urself()
pricebot.getPrice(url=pricebot.URL)
pricebot.sendNotification(price=pricebot.price_as_float)