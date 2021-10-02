import random as r
import math as m
import configGlobals


class SocialEvents:

    def __init__(self, people_objs):

        self.people = people_objs

        self.places = ['street', 'store', 'well', 'bar', 'bakery',
                       'butchery', 'town square', 'forest', 'gardens']

        self.verbs = ['runs into', 'meets',
                      'talks with', 'hangs with', 'spots']

        self.negative_verbs = ['spits on',
                               'gets into a fight with', 'attacks', 'insults']

        self.friendly_events = ['{} {} {} at the {}']
        self.neutral_events = ['{} {} {} at the {}']
        self.disliked_events = ['{} {} {} at the {}']

        self.log = []

    def tick(self):

        prct_tick = configGlobals.SOCIAL_CHANCE
        loops = m.floor(prct_tick * len(self.people.people))

        for _ in range(1, loops):
            self.random_event()

        cp_log = self.log
        self.log = []
        return cp_log

    def random_event(self):

        # add timeouts here
        # Select a random villager to have an event happen
        selected_person = r.choice(self.people.people)
        while selected_person.age < 2:
            selected_person = r.choice(self.people.people)

        another_person = r.choice(self.people.people)

        while (another_person == selected_person) and (another_person.age < 2):
            another_person = r.choice(self.people.people)

        # Now we have two people to trigger an event with
        sel_p_rel = selected_person.relationships.get_relationship(
            another_person)
        ano_p_rel = another_person.relationships.get_relationship(
            selected_person)
        if (sel_p_rel and ano_p_rel):
            sum_relationship = sel_p_rel + ano_p_rel
        else:
            return

        # See if their relationship is bad, neutral, or good
        if sum_relationship < 1:  # Dsliked

            self.negative_event(selected_person, another_person)

        elif 1 < sum_relationship < 3:  # Neutral

            # See if the neutral event will be positive or negative
            if r.uniform(0.00, 1.00) < configGlobals.FRIENDLY_CHANCE:

                self.negative_event(selected_person, another_person)

            else:

                self.positive_event(selected_person, another_person)

        elif 3 < sum_relationship:  # Positive

            self.positive_event(selected_person, another_person)

    def negative_event(self, p_one, p_two):

        event_text = (r.choice(self.disliked_events)).format(
            p_one.name, r.choice(self.negative_verbs), p_two.name, r.choice(self.places))

        p_one.relationships.mod_relationship(0.9, p_two)
        p_two.relationships.mod_relationship(0.9, p_one)

        self.log.append([3, event_text])

    def positive_event(self, p_one, p_two):

        event_text = (r.choice(self.friendly_events)).format(
            p_one.name, r.choice(self.verbs), p_two.name, r.choice(self.places))

        p_one.relationships.mod_relationship(1.1, p_two)
        p_two.relationships.mod_relationship(1.1, p_one)

        self.log.append([3, event_text])
