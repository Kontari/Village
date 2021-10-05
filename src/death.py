import random as r
import markov

class Death:

    '''
    Controls chance of death, and death events
    '''

    def __init__(self, pmanager, mark):

        self.pop = pmanager
        self.mark = mark
        self.dead = []

        # By chance ways to die
        self.ways_to_die = ['{} dies in their sleep',
                            '{} is lost in the night', '{} drowned']

        # Aging related deaths
        self.old_age = ['{} had a heart attack']

        # TODO: Work related deaths

        # Self-inflicted deaths
        self.suicides = ['{} hangs themself', '{} jumps from a tree']

        self.log = []

    def tick(self) -> str:

        for p in self.pop.people:
            self.tick_death(p)

        cp_log = self.log
        self.log = []
        return cp_log

    def tick_death(self, v) -> None:
        '''
        Check if the villager will die today by aging
        '''

        # TODO: refactor < 35 random death

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
            #self.kill_villager(v, r.choice(self.suicides))
            self.kill_villager(v, '{} loses the will to exist -- ' + self.mark.get_death())
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

    def kill_villager(self, villager, reason='') -> None:
        '''
        Time to kick the bucket
        '''
        if reason == '':
            reason = self.mark.get_death()
        if 'starved' in reason:
            reason = '{}\'s hunger lead them to ' + self.mark.get_death()

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
