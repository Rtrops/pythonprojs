import requests
from bs4 import *
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def validate(date_text): #to ensure that the input is a valid date format.
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return False
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")
        return True


validating_date = True
while validating_date is True: 
    billboard_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    year = billboard_date[0:4]
    validating_date = validate(billboard_date)
    if validating_date is False:
        break

URL = f"https://www.billboard.com/charts/hot-100/{billboard_date}"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

songs = soup(name="h3", class_="a-no-trucate")
top_songs = [song.getText().strip("\t\n") for song in songs]

bands = soup(name="span", class_="a-no-trucate")
top_bands = [band.getText().strip("\t\n") for band in bands]

top_100 = [f"{song} by {band}" for song, band in zip(top_songs, top_bands)]
#print(top_songs[0], top_bands[0], year)

# with open("new playlist.txt", "w")as f:
#     for each in top_100:
#         f.write(f"{each} \n")


## AUTHS connecting to Spotfiy API using spotipy lib
print("...authenticating with Spotify")
with open("auth.txt", "r") as f:
    auths = f.readlines()
auths = [auth.strip("\n") for auth in auths]
CLIENTID = auths[0]
CLIENTSECRET = auths[1]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=CLIENTID,
    client_secret=CLIENTSECRET,
    show_dialog=True,
    cache_path="token.txt"
    )
)


print("Authenticated... Creating playlist")
## Create new playlist from the scraped data
user_id = sp.current_user()["id"]
hot100_playlist = sp.user_playlist_create(user_id, name=f"{billboard_date} hot 100" ,public=False, collaborative=False, description="Created by using python's Spotipy lib. Scrapes hot 100 list of a specific date then makes a playlist of it")
playlist_id = hot100_playlist["id"]
print("playlist created... Adding songs")

## Error Handling. Some songs may not be in spotify 
valid_items = []
invalid_items = []
query_list = []

for song in top_songs:
    ci = top_songs.index(song)
    artist = top_bands[ci]
    print("\rProcessing index {0}".format(ci), end="")
    query = sp.search(q=f"track:{song}", type='track')
    query_list.append(query)
    try:
        to_be_added  = query['tracks']['items'][0]['uri']
    except IndexError:
        invalid_items.append(artist + " SONG NAME: " + song)
        continue
    else:    
        valid_items.append(to_be_added) 
print(query_list[0])

print(f"invalid item = {invalid_items}\n len of invalid item = {len(invalid_items)}\n len of valid items that was added = {len(valid_items)}")

sp.playlist_add_items(playlist_id, valid_items)









# 2002-06-05










# i = 1
# with open("topsongs.txt", "w") as f:
#     for each in top_100:
#         f.write(f"{i}. {each}\n")
#         i += 1
     










##RANKING <span class="c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet">2</span>
## SONG TITLE <h3 id="title-of-a-story" class="c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only">Bent
## BAND NAME <span class="c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only">matchbox twenty </span> 







# r_top_titles = soup.find_all(name="h3", class_="a-no-trucate")
# top_titles = [title.getText().strip("\t\n") for title in r_top_titles]

# r_top_artists = soup.find_all(name="span", class_="a-no-trucate")
# top_artists = [artist.getText().strip("\t\n") for artist in r_top_artists]

# top_songs = [f"{artist} - {title}" for title, artist in zip(top_titles,top_artists)]

# with open("song-list.txt",mode="w")as file:
#     for playlist in top_songs:
#         file.write(f"{playlist}\n")