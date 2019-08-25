import settings 
import location 
import notify 
import logging 
import event 
import calendar

import time
# TODO:
# - workdays vs weekend - ignore weekend
# - display
# - event management - calendar object stores events
# = interrupts 

class Scheduler:
  def __init__(self,calendar):
    self.logger = logging.getLogger("Scheduler")
    self.logger.info("Scheduler Started")
    
    self.day = Day(calendar)
    self.schedule = [
      (settings.wakeUpTime,self.day.wakeUp),
      (settings.leaveAptTime,self.day.leaveApt),
      (settings.arriveWorkTime,self.day.arriveWork),
      (settings.leaveWorkTime,self.day.leaveWork),
      (settings.arriveAptTime,self.day.arriveApt),
      (settings.prepSleepTime,self.day.prepSleep),
      (settings.goSleepTime,self.day.goSleep),
      (settings.crunchTime,self.day.crunch)]
    
    # hopefully this is not a copy...
    self.day.schedule = self.schedule

  def start(self):
    self.watchdog()
  def watchdog(self):
    self.logger.info("Watchdog started.")
    while(1):
      print("Watchdogging")

      loc = location.get_location()
      current_time = time.localtime(time.time()) 
      for event in self.schedule:
        if event[0].isTime(current_time):
          event[1](loc)
          event[0].is_triggered = True

      time.sleep(settings.watchdog_duty_cycle)




class Day:
  def __init__(self,calendar):
    self.calendar = calendar

  def wakeUp(self,loc):
    if loc == "apt":
      # wake up sequence
      pass
    else:
      # where am i?
      pass

  def leaveApt(self,loc):
    if loc == "train":
      # commuting to work

      # let's look at soem events
      # TODO: some way to increase priority of events from phone 
      notify.email("Upcoming Events",calendar.getAllEventsTxt())
      pass
    else:
      # took a later train? 
      # working from home? 
      pass

  def arriveWork(self,loc):
    if loc == "work":
      # made it to work
      pass 

  def leaveWork(self,loc):
    if loc == "train":
      pass

  def arriveApt(self,loc):
    if loc == "apt":
      # welcome home 
      pass 

  def prepSleep(self,loc):
    if loc == "apt":
      pass

  def goSleep(self,loc):
    if loc == "apt":
      pass
        
  def crunch(self,loc):
    self.calendar.update()
    for event in self.schedule:
      event[0].is_triggered = False

if __name__ == "__main__":
  calendar = calendar.Calendar()
  scheduler = Scheduler(calendar)
  scheduler.start()
