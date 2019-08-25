class ETime:
  def __init__(self,hour,minute,day="weekday",minutes_tolerance=6):
    self.hour = hour 
    self.minute = minute 
    self.day = day

    self.has_triggered = False 
    self.minutes_tolerance = minutes_tolerance

  def isTime(self,current_time):
    if not self.has_triggered:
      if (self.day == "all") or (current_time.tm_wday <= 4 and self.day == "weekday") or (current_time.tm_wday >= 5 and self.day == "weekend"):
        # there are some edge cases to be aware of here.
        if current_time.tm_hour == self.hour:
          if current_time.tm_minute >= self.minute:
            if current_time.tm_minute - self.minute <= self.minutes_tolerance:
              return True
    return False

