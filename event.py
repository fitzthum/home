# a class for events 
import datetime 

class Event:
  def __init__(self,date,title,etype,location,description = ""):
    self.date = date
    self.title = title
    self.event_type = etype
    self.location = location
    self.description = description

    self.priority = 0

  def __repr__(self):
    return "({}) {} at {} on {} \n".format(self.event_type,self.title,self.location,self.HumanDate)


  @property
  def HumanDate(self):
    return self.date.strftime("%A %d %B")
