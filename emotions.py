import random as r
import configGlobals


class Mood:

  '''
  Manages daily moods and emotions
  '''
  def __init__(self):

    self.mood = ''
    self.is_depressed = False

    self.happy = 5 # 0-10 scale
    self.sad = 4 # 0-10 scale 
    self.productivity = 1.0 

    # Holds multi-day mood effects
    self.mood_events = []

    self.update_mood()
    self.update_productivity()

    self.log = []


  def tick(self, factors):

    # Manage daily chance of feeling good or bad
    self.daily_mood()

    # Manage Mood events
    count_events = 0
    while count_events < len(self.mood_events):

      delta_mood = self.mood_events[count_events].tick()

      if delta_mood is [-1,-1]:
        del self.mood_events[count_events]
      else:
        self.happy += delta_mood[0]
        self.sad += delta_mood[1]

        count_events += 1

    # People will gradually stabalize to 5/3 by default
    if r.randint(0,2) < 1:
      if self.happy > 5: self.happy -= 1
      if self.happy < 5: self.happy += 1
      if self.sad > 3: self.sad -= 1
      if self.sad < 3: self.sad += 1 

    self.update_mood()

    self.update_productivity()

    cp_log = self.log
    self.log = []
    return cp_log


  def death_event(self, rel_strength, s_name, o_name, txt=''):

    if rel_strength < 1.00:
      self.__mood_event(1,0,2,txt='{} is glad {} died.'.format(s_name, o_name))
    elif 1.00 < rel_strength < 2.00:
      self.__mood_event(0,1,1,txt='{} is indifferent to {}s death.'.format(s_name, o_name))
    elif 2.00 < rel_strength < 4.00:
      self.__mood_event(0,1,3,txt='{} is hurt over {}s death.'.format(s_name, o_name))
    elif 4.00 < rel_strength:
      self.__mood_event(-2,2,10,txt='{} is profoundly damaged over {}s death.'.format(s_name, o_name))


  '''
  Crete a new mood event for this person
  '''
  def __mood_event(self, h_tot, s_tot, dur, txt=''):
    self.mood_events.append(MoodEvent(h_tot,s_tot,dur,txt)) 

  def mod_mood(self, happy, sad):

    '''
    Modify the current moods
    '''
    self.happy += happy
    self.sad += sad

    if self.happy < 0: self.happy = 0
    if self.happy > 10: self.happy = 10

    if self.sad < 0: self.sad = 0
    if self.sad > 10: self.sad = 10

  def update_mood(self):

    '''
    Slap a label on the current emotional state
    '''
    if self.happy == self.sad:
      self.mood = 'Indifferent'
    elif self.happy > self.sad + 3:
      self.mood = 'Joyous'
    elif self.happy > self.sad:
      self.mood = 'Happy'
    elif self.sad > self.happy + 2:
      self.mood = 'Sad'
    elif self.sad > self.happy:
      self.mood = 'Melancholic'

    if (self.happy < 2) and (self.sad > 8):
      self.mood = 'Depressed'
      self.is_depressed = True
    else:
      self.is_depressed = False

  def update_productivity(self):

    '''
    Happy people are more productive
    '''
    if self.happy == self.sad:
      self.productivity = 1.0
    elif self.happy > self.sad:
      self.productivity = 1.2
    else:
      self.productivity = .75

  
  def daily_mood(self):

    '''
    On any given day one can be happy or sad
    '''
    if r.uniform(0.0, 1.0) < configGlobals.AVG_HAPPY:
      # good day
      self.mod_mood(1, -1)
    else:
      # bad day
      self.mod_mood(-1, 1)


class MoodEvent: 

  '''
  Moods can be effected by larger events like having a kid, losing
  a loved one, or getting a promotion at work. These last multiple
  days and effect sadness and happiness daily.
  '''
  def __init__(self, daily_happy, daily_sad, duration, text):

    self.daily_happy = daily_happy
    self.daily_sad = daily_sad
    self.duration = duration
    self.elapsed = 0

  def tick(self):

    if self.elapsed <= self.duration:
      self.elapsed += 1
      return self.daily_happy, self.daily_sad
    else:
      return -1, -1
    