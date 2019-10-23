from bs4 import BeautifulSoup
import urllib.request
import re
import subprocess
import sys
import os

arg = list(sys.argv)
commands = {
    '--url': None,
    '--output_dir': None
}
if len(arg) > 1:
    for i in range(1, len(arg), 2):
        assert len(arg) > i+1 and arg[i] and arg[i+1], 'Imcomplete arguments'
        if arg[i] in commands.keys():
            commands[arg[i]] = arg[i+1]
assert commands['--url'], 'No url given, make sure to include --url [url]'


if commands['--output_dir']:
    output_dir = commands['--output_dir']
else:
    output_dir = os.getcwd() + os.sep + 'Soundcloud-Downloaded-Songs'
    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass
url = commands['--url']

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
  songs.append({
      'name': song_names[i],
      'username': usernames[i],
      'url': 'https://soundcloud.com' + song_urls[i]
  }
)


#scdl -l *songurl* --path *path to folder*
for song in songs:
    subprocess.Popen(['scdl', '-l', song['url'], '--path', output_dir])

print('Completed Download')