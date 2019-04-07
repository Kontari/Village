class Calendar:

  '''
  Manages time and seasons
  '''
  def __init__(self):

    self.day = 1
    self.month = 3
    self.year = 1
    self.season = 'Spring'
    self.sum_ticks = 0

    self.logs = []

  def tick(self):

    self.sum_ticks += 1
    self.increment_date()

    cp_logs = self.logs
    self.logs = []
    return cp_logs


  def increment_date(self):

    self.day += 1

    if self.day % 10 == 0:
      self.day = 1
      self.month += 1

      self.set_season()

      self.logs.append([0,'It is now month {}'.format(self.month)])
      self.logs.append([0, 'It is now {}'.format(self.season)])

      if self.month % 12 == 0:

        self.year += 1
        self.month = 1
        self.day = 1

        self.logs.append([0,'The year changed to {}'.format(self.year)])


  def set_season(self):

    if self.month in [12, 1]:
      self.season = 'Winter'
    elif self.month in range(2,5):
      self.season = 'Spring'
    elif self.month in range(6,8):
      self.season = 'Summer'
    elif self.month in range(9,11):
      self.season = 'Fall'


  def get_date(self):

    return '{}/{}/{} {}'.format(self.month,self.day,self.year,self.season)








  

