import random as r
import math as m
import sample

class JobManager:

  def __init__(self, people_manager, city_stats):

    self.people_manager = people_manager
    self.city_stats = city_stats

    self.job_ratios = {'Farmer':0.30 ,'Woodcutter':0.25,
                       'Miner' :0.25 ,'Hunter':0.2
                      }

    self.rng = sample.RandomEffects()

    self.farmers = []
    self.woodcutters = []
    self.miners = []
    self.hunters = []
    self.mothers = []
    self.unemployed = []

    self.logs = []

    # Init workers jobs
    self.init_workers()


  def tick(self):

    self.age_based_jobs()

    self.assign_workers()

    self.tick_jobs()

    cp_logs = self.logs
    self.logs = []
    return cp_logs


  def age_based_jobs(self):

    for p in self.people_manager.people:

      if (0 < p.age < 5) and (p.job != 'Infant'):
        p.job = 'Infant'
        p.can_work = False

      elif (6 < p.age < 10) and (p.job != 'Child'):
        p.job = 'Child'
        p.can_work = False

      elif (65 < p.age ) and (p.job != 'Old Person'):

        # remove from lists
        p.job = 'Old Person'
        p.can_work = False
        


  def update_unemployed(self):

    # Get a list of unnasigned workers
    unassigned = []
    for person in self.people_manager.people:

      if (person.job is '') and (person.can_work):
        unassigned.append(person)

    self.unemployed = unassigned


  # Call when first init village
  def init_workers(self):

    self.update_unemployed()

    def_jobs = ['Farmer','Woodcutter','Miner','Hunter']

    for i in range(len(self.unemployed)):

      chosen = def_jobs[i % len(def_jobs)]

      self.unemployed[i].job = chosen

      self.logs.append([4, '{} was chosen to be a {}.'.format(self.unemployed[i].name, chosen)])

      if chosen == 'Farmer':
        self.farmers.append(self.unemployed[i])
      elif chosen == 'Woodcutter':
        self.woodcutters.append(self.unemployed[i])
      elif chosen == 'Miner':
        self.miners.append(self.unemployed[i])
      elif chosen == 'Hunter':
        self.hunters.append(self.unemployed[i])

    self.update_unemployed()
    

  def assign_workers(self):

    self.update_unemployed()

    # Find jobs that need to be filled
    pop = len(self.people_manager.people)

    needed_jobs = []
    # Check for farmers
    if (len(self.farmers) / pop) < self.job_ratios['Farmer']:
      needed_jobs.append('Farmer')
    if (len(self.woodcutters) / pop) < self.job_ratios['Woodcutter']:
      needed_jobs.append('Woodcutter')
    if (len(self.miners) / pop) < self.job_ratios['Miner']:
      needed_jobs.append('Miner')
    if (len(self.hunters) / pop) < self.job_ratios['Hunter']:
      needed_jobs.append('Hunter')

    if (not needed_jobs):
      # Give default job
      #TODO: Better fix for no needed jobs being selected
      needed_jobs.append('Farmer')

    # Assign workers to jobs that aren't as filled
    for worker in self.unemployed:

      chosen = r.choice(needed_jobs)

      worker.job = chosen

      self.logs.append([4, '{} was chosen to be a {}.'.format(worker.name, chosen)])

      if chosen == 'Farmer':
        self.farmers.append(worker)
      elif chosen == 'Woodcutter':
        self.woodcutters.append(worker)
      elif chosen == 'Miner':
        self.miners.append(worker)
      elif chosen == 'Hunter':
        self.hunters.append(worker)

    self.update_unemployed()


  def tick_jobs(self):

    self.tick_farmers()
    self.tick_woodcutters()
    self.tick_miners()
    self.tick_hunters()
    self.tick_unemployed()
    self.tick_mothers()


  def tick_farmers(self):

    if len(self.farmers) == 0:
      return 0

    for n in self.farmers:

      # base gathered
      base = 10

      # Get productivity level
      prod = n.mood.productivity

      # Sample by chance productivity
      chance = self.rng.get_mod()

      # Get final gathering quota
      final = m.floor((base * prod) * chance)

      self.logs.append([4,'{} harvests {} crops.'.format(n.name, final) ])

      self.city_stats.food += final


  def tick_woodcutters(self):

    if len(self.woodcutters) == 0:
      return 0

    for n in self.woodcutters:

      # base gathered
      base = 20

      # Get productivity level
      prod = n.mood.productivity

      # Sample by chance productivity
      chance = self.rng.get_mod()

      # Get final gathering quota
      final = m.floor((base * prod) * chance)

      self.logs.append([4,'{} chops {} wood.'.format(n.name, final) ])

      self.city_stats.wood += final

  def tick_miners(self):

    if len(self.miners) == 0:
      return 0

    for n in self.miners:

      # base gathered
      base = 15

      # Get productivity level
      prod = n.mood.productivity

      # Sample by chance productivity
      chance = self.rng.get_mod()

      # Get final gathering quota
      final = m.floor((base * prod) * chance)

      self.logs.append([4,'{} mines {} stone.'.format(n.name, final) ])

      self.city_stats.stone += final

  def tick_hunters(self):

    if len(self.hunters) == 0:
      return 0

    for n in self.hunters:

      # base gathered
      base = 20

      # Get productivity level
      prod = n.mood.productivity

      # Sample by chance productivity
      chance = self.rng.get_mod()

      # Get final gathering quota
      final = m.floor((base * prod) * chance)

      # Hunters are high risk high reward
      if r.randint(0,1) > 0:

        self.logs.append([4,'{} hunts and brings back {} food'.format(n.name, final) ])

        self.city_stats.food += final

      else:

        self.logs.append([4,'{} hunts and catches nothing.'.format(n.name) ])

  def tick_unemployed(self):
    pass

  def tick_mothers(self):

    # check if they drop their child
    # else do nothing

    for n in self.mothers:

      youngest = 99

      for c in n.children:
        if c.age < c:
          youngest = c.age
      
      if youngest > 4:
        n.job = 'Unemployed'

