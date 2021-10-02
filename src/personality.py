import random as r


class Personality:

    '''
    Each villager gets a personality archetype which
    effects how social, work, and life events effect them. 
    '''

    def __init__(self, name):

        self.person_traits = []

        self.big_five = []
        for i in range(5):
            self.big_five.append(r.randint(0, 100))

        # Openness
        high_o = ['curious', 'creative', 'artsy']
        low_o = ['cautious', 'dogmatic']
        # Conscientiousness
        high_c = ['organized', 'efficient']
        low_c = ['easy-going', 'careless', 'cheerful']
        # Extraversion
        high_e = ['extroverted', 'outgoing', 'talkative']
        low_e = ['introverted', 'quiet', 'shy']
        # Agreeableness
        high_a = ['friendly', 'compassionate']
        low_a = ['difficult', 'detatched', 'challenging']
        # Neuroticism
        high_n = ['sensitive', 'neurotic']
        low_n = ['secure', 'confident']

        # Openness
        if self.big_five[0] > 50:
            self.person_traits.append(r.choice(high_o))
        else:
            self.person_traits.append(r.choice(low_o))
        # Conscientiousness
        if self.big_five[1] > 50:
            self.person_traits.append(r.choice(high_c))
        else:
            self.person_traits.append(r.choice(low_c))
        # Extraversion
        if self.big_five[2] > 50:
            self.person_traits.append(r.choice(high_e))
        else:
            self.person_traits.append(r.choice(low_e))
        # Agreeableness
        if self.big_five[3] > 50:
            self.person_traits.append(r.choice(high_a))
        else:
            self.person_traits.append(r.choice(low_a))
        # Neuroticism
        if self.big_five[4] > 50:
            self.person_traits.append(r.choice(high_n))
        else:
            self.person_traits.append(r.choice(low_n))

        s_lines = ['{} is also {}.', '{} has a {} side.']
        t_lines = ['{} is {} and {}. ', 'Friends know {} as {} and {}. ',
                   'Dont overlook {}s {} and {} side. ']
        self.story = ''

        self.story += r.choice(t_lines).format(name,
                                               self.person_traits[0], self.person_traits[1])
        self.story += r.choice(t_lines).format(name,
                                               self.person_traits[2], self.person_traits[3])
        self.story += r.choice(s_lines).format(name, self.person_traits[4])

    def get_backstory(self):
        return self.story
