import shows 
import settings 

class Calendar:
  def __init__(self):
    self.events = []
    self.all_events = []

    self.load() 
    
  def load(self):
    # concerts
    all_shows = list(shows.getShows())
    self.all_events.extend(all_shows)
    self.events.extend(list(shows.filterEvents(all_shows)))

  def getAllEventsTxt(self):
    return str(self.events)

