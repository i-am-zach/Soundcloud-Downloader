from bs4 import BeautifulSoup
import urllib.request
import re

url = r'https://soundcloud.com/zach-lefkovitz/sets/dl'
sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce, 'lxml')

print('DONWLOADING FROM: ' + soup.title.string.upper().replace(' | FREE LISTENING ON SOUNDCLOUD', '') + '...')

links = soup.findAll('a')

usernameRegex = re.compile("\"/([^/]+)")

song_names = []
usernames = []
for link in links:
    if 'url' in str(link):
        if usernameRegex.search(str(link)):
            usernames.append(usernameRegex.search(str(link)).group(1))
        else:
            usernames.append(None)
        song_names.append(link.string)

del song_names[0]
del usernames[0]
songs = []
for i in range(len(song_names)):
  songs.append({song_names[i]: {
      'username': usernames[i],
      'link': '?'
  }})
print(songs)