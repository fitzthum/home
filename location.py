import settings

from locationsharinglib import Service
from geopy.distance import geodesic
import pickle


def get_location():
  cookies_file = 'location_sharing.cookies'
  google_email = 'pocketg99@gmail.com'


  service = Service(cookies_file=cookies_file, authenticating_account=google_email)

  person = list(service.get_all_people())[0]
  for location in settings.locations:
    print(person.longitude,person.latitude)
    dist = geodesic((person.latitude,person.longitude),location[1]).miles 
    print(dist)
    if dist <= location[2]:
      return location[0]

if __name__ == "__main__":
  print(get_location())
