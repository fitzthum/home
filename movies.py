# finds good movies in the area

from event import Event
import secrets import fandango_key, fandango_secret

class MovieFinder:
  def __init__(self,zipcode):
    self.zipcode = zipcode 
    

  def getNearbyFilms(self):
    
    

