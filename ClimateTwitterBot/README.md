This is a bot I made in python that picks a random place from a JSON of 145k cities on Earth with pop.>1000 (https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/table/?flg=en-us&disjunctive.cou_name_en&sort=name)
Then uses the Meteosource API to get the current temperature at that place's coordinates. Then it gets the temp for that date/place from 40 years ago.
If the difference is positive, the bot uses the Tweepy library to tweet out something like "It's x degrees hotter today in y place than half a century ago. Yikes!!'
If neg difference, new city is fetched just for ease purposes.
Just a fun project I wanted to write up and share, climate change is real!!!
