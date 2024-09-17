class Test:
    def public(self):
        print('Публичный метод')

    def _protected(self):
        print("Защищенный метод")

    def __private(self):
        print('Приватный метод')

    def func__private(self): # метод для вызова приватного метода
        self.__private()


test = Test()
test.public()
test._protected()
test.func__private()