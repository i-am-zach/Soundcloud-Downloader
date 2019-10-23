from bs4 import BeautifulSoup
import urllib.request
import re

url = r'https://soundcloud.com/zach-lefkovitz/sets/dl'
sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce, 'lxml')

print('DONWLOADING FROM: ' + soup.title.string.upper().replace(' | FREE LISTENING ON SOUNDCLOUD', '') + '...')

links = soup.findAll('a')

usernameRegex = re.compile("\"/([^/]+)")
linkRegex = re.compile("/([^/]+)/([^\"]+)")

song_names = []
usernames = []
song_urls = []
for link in links:
    if 'url' in str(link):
        if usernameRegex.search(str(link)):
            usernames.append(usernameRegex.search(str(link)).group(1))
        else:
            usernames.append(None)
        if linkRegex.search(str(link)):
            song_urls.append(linkRegex.search(str(link)).group())
        else:
            song_urls.append(None)
        song_names.append(link.string)

del song_names[0]
del usernames[0]
del song_urls[0]
songs = []
for i in range(len(song_names)):
  songs.append({song_names[i]: {
      'username': usernames[i],
      'url': 'soundcloud.com' + song_urls[i]
  }})