class Enemy(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def increase_health(self):
        self.health = 100

    def reduce_health(self, value):
        self.health -= value
