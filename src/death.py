import random as r


class Death:

    '''
    Controls chance of death, and death events
    '''

    def __init__(self, pmanager):

        self.pop = pmanager
        self.dead = []

        # By chance ways to die
        self.ways_to_die = ['{} dies in their sleep',
                            '{} is lost in the night', '{} drowned']

        # Aging related deaths
        self.old_age = ['{} had a heart attack']

        # Work related deaths
        self.hunter_death = ['{} was lost on a hunt',
                             '{} was mauled to death by bears']
        self.farmer_death = ['{} slipped onto a knife']
        self.woodcutter_death = ['{} was crushed by a tree']
        self.miner_death = ['{} died in a mine collapse']

        # Self-inflicted deaths
        self.suicides = ['{} hangs themself', '{} jumps from a tree']

        self.log = []

    def tick(self):

        for p in self.pop.people:
            self.tick_death(p)

        cp_log = self.log
        self.log = []
        return cp_log

    def tick_death(self, v):
        '''
        Check if the villager will die today by aging
        '''
        '''
    if 0 < v.age < 4: # Infant
      if r.randint(0,64605) == 0:
        self.kill_villager(v)
        return
    elif 4 < v.age < 10: # Child
      if r.randint(0,3041545) == 0: 
        self.kill_villager(v)
        return
    elif 15 < v.age < 24: # Young Adult
      if r.randint(0,696420) == 0: 
        self.kill_villager(v)
        return
    '''
        if 35 < v.age < 50:  # Adult
            if r.randint(0, 241995) == 0:
                self.kill_villager(v)
                return
        elif 50 < v.age < 70:  # Old Person
            if r.randint(0, 29380579) == 0:
                self.kill_villager(v)
                return
        elif v.age > 70:  # Elder
            if r.randint(0, 5475) == 0:
                self.kill_villager(v)
                return

        '''
    Check if the villager is depressed 
    '''
        if v.mood.is_depressed and r.randint(0, 10):
            self.kill_villager(v, r.choice(self.suicides))
            return

        '''
    Check if villager dies on the job
    '''

        '''
    Check if villager starved
    '''
        if v.hunger == 0:
            self.kill_villager(v, '{} starved to death.')
            return

    def kill_villager(self, villager, reason=''):
        '''
        Time to kick the bucket

        1. Pool all possible deaths into a list
        2. Select one and log it
        3. Remove this person from all relationship objects
        '''
        if reason == '':
            reasons = self.ways_to_die
            if villager.job == 'Woodcutter':
                reasons += self.woodcutter_death
            if villager.job == 'Miner':
                reasons += self.hunter_death
            if villager.job == 'Hunter':
                reasons += self.hunter_death
            if villager.job == 'Farmer':
                reasons += self.farmer_death
            reason = r.choice(reasons)

        self.log.append([2, '\u001b[31;1m' +
                        reason.format(villager.name) + '\u001b[0m'])

        # Clean up lists
        self.pop.people.remove(villager)
        self.dead.append(villager)

        # Clean up relationship objects
        for people in self.pop.people:

            # Get rel value and remove the person
            rel_strength = people.relationships.del_relationship(villager)

            # Stronger relationships mean more sadness
            people.mood.death_event(rel_strength, people.name, villager.name)
