import settings 
import location 
import notify 
import logging 
import time
import event 
import calendar

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
      (settings.wakeUpTime,day.wakeUp),
      (settings.leaveAptTime,day.leaveApt),
      (settings.arriveWorkTime,day.arriveWork),
      (settings.leaveWorkTime,day.leaveWork),
      (settings.arriveAptTime,day.arriveApt),
      (settings.prepSleepTime,day.prepSleep),
      (settings.goSleepTime,day.goSleep),
      (settings.crunchTime,day.crunch)]
  

  def start(self):
    self.watchdog()
  def watchdog(self):
    self.logger.info("Watchdog started.")
    while(1):
      location = location.get_location()

      time.sleep(10000)




class Day:
  def __init__(self,calendar):
    this.calendar = calendar

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
      notify.email("Upcoming Events",calendar.short_view())
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
    if loc = "apt":
      pass
        
  def crunch(self,loc):
    self.calendar.update()


if __name__ == "__main__":
  calendar = Calendar()
  scheduler = Scheduler(calendar)
  scheduler.run()
