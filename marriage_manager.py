import random as r

# Subclass of the people manager

# 1. Decides who is eligable for Marriage
# 2. Allows romantic events to happen in the 
#    social manager
class Marriage:

  def __init__(self, people):
    self.people = people


  def check_marriage(self):

    # Check for spouse
    if (self.romance == False) and (18 < self.age < 50) and (self.spouse == ''):

      # Now eligable to marry
      self.romance = True

      self.log.append([4,'{} ({}) is looking for a partner.'.format(self.name, self.gender[0])])
