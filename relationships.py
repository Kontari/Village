import random as r

class Relations:

  def __init__(self, my_name, my_id):

    self.my_name = my_name
    self.my_id = my_id 

    # Holds person obj, rel value, text to describe it
    self.rel = [] 
    self.log = []

  def tick(self):
    cp_log = self.log
    self.log = []
    return cp_log

  def get_rels_str(self):
    rels = ''
    for r in self.rel:
      rels += '%.2f'%(r[1]) + ' '
    return rels

  def init_relationships(self, people):
    for p in people:
      self.add_relationship(p)

  def add_relationship(self, person, rel_value=2.0, rel_text=''):
    self.rel.append([person, rel_value, rel_text])

  def del_relationship(self, person):

    '''
    When a villager dies remove the relationship.
    Return strength of relationship and relationship
    text to create a mood event.
    '''
    count = 0
    while count < len(self.rel):

      if self.rel[count][0] == person:
        dead_rel_value = self.rel[count][1]
        del self.rel[count]
        return dead_rel_value

      count += 1


  def mod_relationship(self, value, person):

    for people in self.rel:
      if people[0] == person:

        # Get old relationship text
        old_rel_text = self.get_rel_text(people[1])

        # Update new relationship data
        fin_rel_value = people[1] * value
        people[1] = fin_rel_value

        # Get new relationship text
        rel_text = self.get_rel_text(fin_rel_value)

        # If the relationship catagorychanged
        if old_rel_text != rel_text:

          if rel_text == "Liked":
            rel_text = '\u001b[32m' + rel_text + '\u001b[0m'
          elif rel_text == "Disliked":
            rel_text = '\u001b[31m' + rel_text + '\u001b[0m'
          elif rel_text == "Friendly":
            rel_text = ' \u001b[32;1m' + rel_text + '\u001b[0m'

          new_rel_text = "{} is now {} with {}. ({})".format(self.my_name, rel_text, people[0].name, '%.3f'%(fin_rel_value))

          self.log.append([4, new_rel_text])


  def get_relationship(self, person):

    for people in self.rel:
      if people[0] == person:
        return people[1]

    # Person must not exist so add
    self.rel.append((person,2.0))


  def get_rel_text(self, rel_value):

    if rel_value < 1.00:
      return "Disliked"
    elif 1.00 < rel_value < 2.00:
      return "Neutral"
    elif 2.00 < rel_value < 3.00:
      return "Liked"
    elif 3.00 < rel_value:
      return "Friendly"

