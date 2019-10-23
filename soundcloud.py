from bs4 import BeautifulSoup
import urllib.request

url = r'https://soundcloud.com/zach-lefkovitz/sets/dl'
sauce = urllib.request.urlopen(url).read()

soup = BeautifulSoup(sauce, 'lxml')

print('DONWLOADING FROM: ' + soup.title.string.upper().replace(' | FREE LISTENING ON SOUNDCLOUD', '') + '...')