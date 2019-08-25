import requests
import progressbar
import itertools 
import pickle
import sys

from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup
from collections import Counter

from event import Event 


def processPage(url):
  events = []
  page = requests.get(url)
  if page.status_code >= 300:
      return None 

  soup = BeautifulSoup(page.content,'html.parser')
  try:
    cal = soup.find_all(class_="event-listings")[0]
  except IndexError:
    return None 
  
  for event in cal.find_all("li"):
      date_str = event.get('title')
      if date_str is not None and len(date_str.split()) == 4:
        date = datetime.strptime(date_str,"%A %d %B %Y")
        title = event.find_all(class_="summary")[0].find("strong").get_text()
        
        loc_element = event.find_all(class_="location")[0].find("a")
        if loc_element is not None:
          location = loc_element.get_text()
          events.append(Event(date,title,"music",location))
    
  return events

def getShows():
  shows = []

  base_url = "http://www.songkick.com/metro_areas/7644-us-new-york" 
  start_date = date.today()
  end_date = start_date + timedelta(days=7)
  end_str = end_date.strftime('%m%%2F%d%%2F%Y')
  start_str = start_date.strftime('%m%%2F%d%%2F%Y')
  page = 1 

  request = "{}?filters%5BmaxDate%5D={}&filters%5BminDate%5D={}&page={}".format(base_url,end_str,start_str,page)
  
  page_shows = processPage(request)
  while page_shows is not None:
    shows.extend(page_shows)
    page += 1
    request = "{}?filters%5BmaxDate%5D={}&filters%5BminDate%5D={}&page={}".format(base_url,end_str,start_str,page)
    page_shows = processPage(request)
    print("processing page {}".format(page))

  return shows 

def generateiTunesArtists():
  artist_counts = Counter() 
  xml_path = "/Users/fitzthum/music/iTunes/iTunes Music Library.xml" 
  debug_path = "iTunes Music Library small.xml" 
  with open(xml_path) as f: 
    soup = BeautifulSoup(f,'lxml')
    for song in progressbar.progressbar(soup.find_all('dict')):
      try:
        artist = (str(song).split("<key>Artist</key><string>"))[1].split("</string>")[0]
        artist_counts[artist] += 1
      except IndexError:
        pass

  pickle.dump(artist_counts,open("artists.pkl","wb"))

def loadiTunesArtists():
  return pickle.load(open("artists.pkl","rb"))

def filterEvents(events):
  artist_counts = loadiTunesArtists()
  for event in progressbar.progressbar(events):
    artists = event.title.split(", ")
    if artists[-1].startswith('and'): 
      artists[-1] = artists[-1][4:]
    artists.append(event.title)
    if event.title in artist_counts:
      event.priority = 1
      yield event

