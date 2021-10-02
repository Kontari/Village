import random as r
import logging
import namegen
import emotions
import math as m
import personality
import configGlobals
import relationships
import random as r


class PeopleManager:

    def __init__(self):

        self.people = []

        self.init_population(configGlobals.STARTING_POP)

        # Give all existing people relationship objects
        self.init_pop_relationships()

        # Used to only sort when size changes
        self.last_pop = 0

        self.log = []

    def init_population(self, to_generate):

        if to_generate < 4:
            to_generate = 4

        for i in range(to_generate):
            if r.randint(0, 1) < 1:
                self.people.append(Person(age=r.randint(10, 30), gender=1))
                self.people.append(Person(age=r.randint(10, 30), gender=0))
            else:
                self.people.append(Person(age=r.randint(10, 30), gender=0))
                self.people.append(Person(age=r.randint(10, 30), gender=1))

    def init_pop_relationships(self):

        for p in self.people:
            # Every person has a relationship with every
            # other person
            p.init_relationships(self.people)

    # TODO

    def add_new_relationsip(self, person):

        # for p in self.people:
        #    p.init_relationships(self.people)
        pass

    def marriage_manager(self):

        single_men = []
        single_women = []

        for p in people:

            if p.gender == 'M' and p.romance:
                single_men.append(p)
            elif p.gender == 'F' and p.romance:
                single_women.append(p)

    def add_child(self, father, mother):

        mother.job = ''
        child = Person()
        child.lname = father.lname

    def settlers(self):

        if r.randint(configGlobals.SETTLER_CHANCE, 360) == 360:

            num_settlers = r.randint(10, 20)

            for i in range(num_settlers):
                self.people.append(Person(age=r.randint(4, 60)))

            self.log.append(
                [0, '{}  new settlers have arrived!'.format(num_settlers)])

    def children(self):

        if r.randint(1, 20) > 19:
            self.people.append(Person(age=r.randint(1, 60)))

            # Init persons relationships
            self.people[-1].relationships.init_relationships(self.people)

            # Update everyone but the persons relationship
            # objects to include the new person
            for p in self.people[:-1]:
                p.relationships.add_relationship(self.people[-1])

            self.log.append(
                [0, '{} has appeared!'.format(self.people[-1].name)])

        # Adding a child
        if r.randint(1, 25) == 1:

            # Create a new person object
            self.people.append(Person(age=1))

            # Init childs relationships
            self.people[-1].relationships.init_relationships(self.people)

            # Update everyone but the childs relationship
            # objects to include the new child
            for p in self.people[:-1]:
                p.relationships.add_relationship(self.people[-1])

            # Log the event
            self.log.append([0, '{} was born!'.format(self.people[-1].name)])

    def sort_people(self, sort_by):

        if sort_by == 'job':

            '''
            Perform a radix style sort by profession
            '''
            radix = [['Woodcutter'], ['Miner'], ['Hunter'], [
                'Farmer'], ['Child'], ['Infant'], ['None'], ['']]

            for p in self.people:
                radix[[item[0] for item in radix].index(p.job)].append(p)

            updated_ppl = []

            for r in radix:
                for per_job in range(1, len(r)):
                    updated_ppl.append(r[per_job])

            self.people = updated_ppl

    def tick(self):

        # only sort when needed
        if len(self.people) != self.last_pop:
            # Sorts the people
            self.sort_people('job')
            self.last_pop = len(self.people)

        # Check if a child is randomly born
        self.children()

        # Tick if new settlers arrive
        self.settlers()

        # Tick people
        for p in self.people:
            self.log += p.tick()

        # Get stats
        for p in self.people:
            self.log.append([0, p.show_stats()])

        cp_log = self.log
        self.log = []
        return cp_log


class Person:

    def __init__(self, job='', gender=-1, age=0):

        # Unique identifier
        self.id_num = r.getrandbits(128)

        # Assigned a name
        self.name = namegen.get_name()
        self.lname = namegen.get_last_name()

        # Assign job
        self.can_work = False
        if 0 < age < 5:
            self.job = 'Infant'
        if 4 < age < 10:
            self.job = 'Child'
        else:
            self.job = job
            self.can_work = True

        self.age = age

        # Assign gender
        if gender == 0:
            self.gender = 'Male'
        elif gender == 1:
            self.gender = 'Female'
        elif r.randint(0, 1) < 1:
            self.gender = 'Male'
        else:
            self.gender = 'Female'

        # Personality information
        self.pers = personality.Personality(self.name)
        self.mood = emotions.Mood()

        self.romance = False
        self.spouse = ''

        # Relationship objects
        self.relationships = relationships.Relations(self.name, self.id_num)

        # Statuses
        '''
    Hunger
    Scale from 1-10
    1 = Starving
    2-5 = Hungry
    6-8 = Sated
    9-10 = Fed
    '''
        self.hunger = 5

        self.history_log = []
        self.log = []

        # Log about the person when they are made
        self.log.append([2, self.pers.get_backstory()])

    def tick(self):

        self.log += self.relationships.tick()

        # Manage mood
        self.mood.tick('')

        # Manage romance
        self.check_marriage()
        # TODO
        # else: # Roll for spouse
        #  pass

        if 4 < self.age < 10:
            self.job = 'Child'

        cp_log = self.log
        self.log = []
        return cp_log

    def init_relationships(self, people):
        self.relationships.init_relationships(people)

    # todo put in romance manager?
    def check_marriage(self):

        # Check for spouse
        if (self.romance == False) and (18 < self.age < 50) and (self.spouse == ''):

            # Now eligable to marry
            self.romance = True

            self.log.append(
                [2, '{} ({}) is looking for a partner.'.format(self.name, self.gender[0])])

        elif self.romance == True:

            # Looking for a partner
            pass

    def set_spouse(self, person):
        self.spouse = person

    def show_stats(self):

        symb = '\u001b[34m♂\u001b[0m'
        if self.gender == 'Female':
            symb = '\u001b[35;1m♀\u001b[0m'

        job = self.job
        if not self.job:
            job = 'None'

        if job == 'Farmer':
            job = '\u001b[34m' + job + '\u001b[0m'
        elif job == 'Woodcutter':
            job = '\u001b[33m' + job + '\u001b[0m'
        elif job == 'Miner':
            job = '\u001b[35m' + job + '\u001b[0m'
        elif job == 'Hunter':
            job = '\u001b[32m' + job + '\u001b[0m'
        else:
            job = '\u001b[36m' + job + '\u001b[0m'

        # Basic information about a villager
        basic_info = '{}  {}  Age:{} {} {}'.format('{0: <10}'.format(
            self.name), '{0: <20}'.format(job), self.age, symb, self.mood.mood)

        # Relationship info about a villager
        rel_info = '\n{}'.format(self.relationships.get_rels_str())

        # Advanced information on a villager
        show_rel = '--'
        if self.romance == True and self.spouse == '':
            show_rel = 'Single'
        elif self.romance == True and self.spouse != '':
            show_rel = 'Married'

        # Show mood
        mood = self.mood.mood

        adv_info = '\n{} | {} '.format(mood, show_rel)

        return basic_info #+ rel_info + adv_info
