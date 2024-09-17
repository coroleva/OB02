class Bird():   # родительский класс
    def __init__ (self, name, voice, color): # атрибуты - общие для всех птичек
        self.name = name
        self.voice = voice
        self.color = color
# общие методы для всех птичек
    def fly(self):
        print(f'Птичка {self.name} летит!')
    def eat(self):
        print(f'Птичка {self.name} ест')
    def sinng(self):
        print(f'Птичка {self.name} поет чирик')
    def info(self):
        print(f'Птичка {self.name} цвет {self.color} поёт {self.voice}')

class Pigeon(Bird): # дочерний класс
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color) # обращаемся к родительскому классу и берем общие признаки
    def wolk(self):  # дополнительные методы
        print(f'Птичка {self.name} гуляет')
    def sinng(self): # переопределили методы родительского класса
        print(f'Птичка {self.name} поет курлык - курлык')

bird1 = Bird("Митя", "Чирик", "Коричневый")
bird1.sinng()
bird1.fly()
bird1.eat()
bird1.info()

print("")
bird2 = Pigeon("Гоша", "Курлык", "Белый", "Крошки")
bird2.sinng()
bird2.fly()
bird2.eat()
bird2.info()
bird2.wolk()

