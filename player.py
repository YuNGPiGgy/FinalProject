



class Player:
    def __init__(self):
        self.attack = 0
        self.health = 0

    def set_attack(self, num):
        self.attack += num

    def set_health(self, num):
        self.health += num

    def get_attack(self):
        return self.attack

    def get_health(self):
        return self.health
