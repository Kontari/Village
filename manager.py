import calendar
import city
import death
import namegen
import people
import logging
import jobs
import configGlobals
import social


class Instance:

  def __init__(self):

    # Controls the incrementing of date
    self.cal = calendar.Calendar()

    # Controls logging events
    self.log = logging.HistoryManager(self.cal)

    # Create some people
    self.villagers = people.PeopleManager()

    # Controls city metrics and stockpiles
    self.stats = city.CityManager(self.villagers)

    # Controls who has what job
    self.prof = jobs.JobManager(self.villagers, self.stats)

    # Make social events happen
    self.social_events = social.SocialEvents(self.villagers)

    # Controls death and dying events
    self.reaper = death.Death(self.villagers)



    # Holds a list of all known objects that need to tick 
    self.managers = []

    self.managers.append(self.log) # Create a new logging entry for the day
    
    self.managers.append(self.cal) # Date goes up

    self.managers.append(self.stats) # People eat and food is lost
    
    self.managers.append(self.villagers) # Villagers tick
    
    self.managers.append(self.prof) # Professions are managed, jobs reassigned
    
    self.managers.append(self.social_events) # Random social events occur

    self.managers.append(self.reaper) # Sometimes people kick the bucket
    


  def tick_month(self):
    for i in range(1,10):
      self.next_tick()
  
    self.log.list_todays_events()


  def tick_day(self):

    self.next_tick() 

    self.log.list_todays_events()


  def next_tick(self):

    for manager in self.managers:

      #print('Calling: {}'.format(manager))
      # Tick current manager and record output
      self.log.add_events(manager.tick())
      #print(manager)


      










      









      
