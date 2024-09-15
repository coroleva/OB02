class Bird():
    def __init__ (self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f'Птичка {self.name} летит!')
    def eat(self):
        print(f'Птичка {self.name} ест')
    def sinng(self):
        print(f'Птичка {self.name} поет {self.voice}')
    def info(self):
        print(f'Птичка {self.name} цвет {self.color} поёт {self.voice}')
class Pigeon(Bird):
    pass

bird1 = Bird("Гоша", "Курлык", "Белый")
bird1.sinng()
bird1.fly()
bird1.eat()
bird1.info()

