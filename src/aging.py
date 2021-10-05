import random as r

class Age:
    '''
    Manages birthdays, and age-related job eligability
    '''
    def __init__(self, age, bday=''):

        self.age = age
        self.age_text = ''

        if bday == '':
            self.bday = r.randint(1, 360)
        else:
            self.bday = bday
        self.reassign_age_text()

        self.log = []

    def tick(self) -> None:
        pass

    def reassign_age_text(self) -> None:
        if self.age < 4:
            self.age_text = 'Infant'
        elif 4 < self.age < 10:
            self.age_text = 'Child'
        elif 15 < self.age < 24:
            self.age_text = 'Young Adult'
        elif 25 < self.age < 50:
            self.age_text = 'Adult'
        elif 50 < self.age < 70:
            self.age_text = 'Old Person'
        else:
            self.age_text = 'Elder'
