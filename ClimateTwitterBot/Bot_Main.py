import tweepy, logging, json, random, requests, os
from dotenv import load_dotenv

logger = logging.getLogger()
load_dotenv()

##CREATE BOT
class TwitterBot:
    def __init__(self):
        self.CONSUMER_KEY = os.environ.get('TWEEPY_CONSUMER_KEY')
        self.CONSUMER_SECRET = os.environ.get('TWEEPY_CONSUMER_SECRET')
        self.ACCESS_TOKEN = os.environ.get('TWEEPY_ACCESS_TOKEN')
        self.ACCESS_TOKEN_SECRET = os.environ.get('TWEEPY_ACCESS_TOKEN_SECRET')
        self.METEO_API_KEY = os.environ.get('METEO_API_KEY')
        self.city_name = None
        self.city_lat = None
        self.city_lon = None
        
    def link_api(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET,
                                   self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        twitx_api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
        try:
            twitx_api.verify_credentials()
        except Exception as e:
            logger.error("Error establishing link to API", exc_info=True)
            raise e
        logger.info("API Link Successful")
        return twitx_api
    
#CREATING THE TWEET
    def post_tweet(self, tweet_body):
        api = self.twitx_api
        api.update_status(tweet_body)

#FOLLOW SOMEONE
    def follow(self, handle):
        api = self.twitx_api
        api.create_friendship(handle)
        
#GET PLACE ON EARTH
    def fetch_city(self):
    #Gets random place from a JSON of over 140k cities on Earth with pop.>1000 (Geonames)
        with open('geonames-all-cities-with-a-population-1000.json') as f:
            place_data = json.load(f)
            city = random.choice(place_data)
            self.city_name = city['name']
            self.city_lon, self.city_lat = city['coordinates']['lon'], city['coordinates']['lat']
        print(self.city_name, self.city_lat, self.city_lon)
        
    def get_current_temp(self):
#WEATHER API
#Uses Meteosource API
        METEO_PARAMS = {'key': self.METEO_API_KEY,
              'lat': f'{self.city_lat}',
              'lon': f'{self.city_lon}',
              'sections': 'current',
              'units': 'metric'
              }
        METEO_URL = "https://www.meteosource.com/api/v1/free/point"
        current_weather_data = requests.get(METEO_URL, METEO_PARAMS).json()
        current_temp = current_weather_data['current']['temperature']
        print(f'{current_temp} degrees Celsius.')
        
    def get_historical_temp(self, date):
        TIMEMACHINE_PARAMS = {'key': '71txkt4dwksxfdns83srpyffchv1v92qi5pba0ir',
              'lat': f'{self.city_lat}',
              'lon': f'{self.city_lon}',
              'date': 'YYY-MM-DD',
              'units': 'metric'
              }
        TIMEMACHINE_URL = ''
        timemachine_data = requests.get(TIMEMACHINE_URL, TIMEMACHINE_PARAMS).json()
        hist_temp = timemachine_data['data']['surface_temperature']
    
    def get_temp_difference(self, current_temp, past_temp):
            temp_difference = current_temp - past_temp


#BOT LOGIC
bot = TwitterBot()

def botlogic(TwitterBot):
    try:
        TwitterBot.fetch_city()
        TwitterBot.get_current_temp()
        difference = TwitterBot.get_temp_difference(TwitterBot.current_temp, TwitterBot.hist_temp)
        if difference > 0:
            tweet = f'It\'s {difference} degrees hotter today in {TwitterBot.city_name} than half a century ago. Yikes!!'
            TwitterBot.post_tweet(tweet_body=tweet)
        else:
            botlogic()
    except:
        raise tweepy.errors.TweepyException('Tweepy Error! Something went wrong')

botlogic(TwitterBot=bot)
