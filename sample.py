import random as r

class RandomEffects:

  def __init__(self):

    pass

  def get_mod(self):

    p = r.randint(0,100)

    if p in range(0,80):
      return 1.0
    elif p in range(81,95):
      return 1.5
    elif p in range(96,100):
      return 2.0
    else:
      return 1.0

  # Returns output for a day of farming
  def get_farming(self):

    p = r.randint(0,100)

    if p in range(0,80):
      return 1.0
    elif p in range(81,95):
      return 1.5
    elif p in range(96,100):
      return 2.0
    else:
      return 1.0

  


    



