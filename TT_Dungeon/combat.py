import random


class Combat(object):
    dodge_limit = 6
    attack_limit = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def inititive(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4