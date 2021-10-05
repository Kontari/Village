import namegen
import random as r


class CityManager:

    '''
    Manages the villages stockpiles and items
    '''

    def __init__(self, people):

        self.name = namegen.get_name()

        self.pop = people
        self.population = len(self.pop.people)

        self.wood = 20
        self.stone = 20
        self.food = 0

        self.log = []

    def tick(self) -> list:

        self.population = len(self.pop.people)

        self.food_eaten()
        self.wood_burned()
        self.log_stats()

        cp_log = self.log
        self.log = []
        return cp_log

    def log_stats(self) -> list:

        self.log.append([0, 'Pop:{} Wood:{} Stone:{} Food:{}\n'.format(
            self.population, self.wood, self.stone, self.food)])

    def food_eaten(self) -> None:

        sum_food = 0

        for p in self.pop.people:

            if 0 < p.age < 4:
                sum_food += 3
            if 4 < p.age < 10:
                sum_food += 4
            else:
                sum_food += 5

        self.food -= sum_food

        if self.food < 0:
            self.food = 0
            self.log.append([2, 'Food stocks are empty! Bad times are ahead'])

            for p in self.pop.people:
                p.hunger -= 1

        else:
            self.log.append([2, 'The citizens eat {} food'.format(sum_food)])

            for p in self.pop.people:
                if p.hunger < 11:
                    p.hunger += 1

    def wood_burned(self) -> None:

        sum_burned_cook = 5
        sum_burned_warmth = 5

        self.wood -= (sum_burned_cook + sum_burned_warmth)

        if self.wood < 0:
            self.wood = 0
            self.log.append([2, 'Wood stocks are empty! Bad times are ahead'])
        else:
            self.log.append(
                [2, 'The citizens burn {} wood to cook'.format(sum_burned_cook)])
            self.log.append(
                [2, 'The citizens burn {} wood to stay warm'.format(sum_burned_warmth)])
