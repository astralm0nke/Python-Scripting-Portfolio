# Based in part off App Brewery's 100 days of code day 45
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
BACKGROUND_COLOR = '#3394FF'

#----------GET SONGS FROM BILLBOARD TOP 100----------
def get_song():
    billb_hot = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
    html_file = billb_hot.content
    soup = BeautifulSoup(html_file, 'html.parser')
    #pretty_soup = soup.prettify()
    #print(pretty_soup)

    songs = soup.select('li ul li h3')
    songs_list = [song.getText().strip() for song in songs]

#----------SPOTIFY API AUTHENTICATION----------

    scope = 'playlist-modify-private'
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            redirect_uri='http://localhost:3000',
            client_id=#CLIENT ID -> str
            client_secret=#CLIENT SECRET -> str,
            show_dialog=True,
            cache_path='token.txt'
        )
    )
    user_id = sp.current_user()["id"]

    song_uris = []
    year = date.split('-')[0]
    for song in songs_list:
        result = sp.search(q=f'track:{song} year:{year}', type='track')
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} isn't on Spotify. Skipped over :( )")
        
#----------CREATE PLAYLIST----------
    playlist = sp.user_playlist_create(user=user_id, 
                                            name=f'Billboard Hot 100 {date}', 
                                            public=True, 
                                            collaborative=False, 
                                            description=f'A playlist of the Billboard Hop 100 songs from {date}')

    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

#----------GUI----------
from tkinter import *
BACKGROUND_COLOR = '#3394FF'
window = Tk()
window.title('Musical Playlist Time Machine')
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

bck_img = PhotoImage(file='//persistence_dali.png')
canvas = Canvas(width=700, height=650)
background = canvas.create_image(350, 350, image=bck_img)
prompt = canvas.create_text((355, 575), text='What day in the past would you like to listen to? (please format as YYYY-MM-DD):', fill='WHITE', font=('Times New Roman', 18, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

date_box = Entry(window, bg='white', relief=RAISED, textvariable=StringVar, width=25)
date_box.grid(row=1, column=0)
date = str(date_box)

travel_button = Button(text='Create Playlist', command=get_song)
travel_button.config(width=25)
travel_button.grid(row=1, column=1)

window.mainloop()