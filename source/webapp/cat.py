from random import randint


class Cat:
    def __init__(self, name: str, age=1, fill=40, happiness=40, awake: bool = True):
        self.name = name
        self.age = age
        self.fill = fill
        self.happiness = happiness
        self.awake = awake

    def dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "fill": self.fill,
            "happiness": self.happiness,
            "pic": self.pic()
        }

    def play(self):
        if self.awake:
            if randint(1, 4) > 1:
                self.happiness = min(self.happiness + 15, 100)
            else:
                self.happiness = 0
            self.fill = max(self.fill - 10, 0)
        else:
            self.awake = True
            self.happiness -= 5

    def feed(self):
        if self.awake:
            self.fill += 15
            if self.fill > 100:
                self.happiness = max(self.happiness - 30, 0)
                self.fill = 100
            else:
                self.happiness += 5

    def sleep(self):
        self.awake = False

    def pic(self):
        if self.happiness < 30:
            return "/static/images/sad.jpg"
        elif self.happiness < 70:
            return "/static/images/cat.JPG"
        else:
            return "/static/images/lucky.png"