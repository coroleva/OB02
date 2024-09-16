# базовый класс для всех пользователей
class User:
    def __init__(self, user_id, name):
    # защищенные атрибуты
        self._user_id = user_id
        self._name = name
        self._level = 'user'
# методы для доступа к защищенным атрибутам
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level
    def set_name(self, new_name):
        self._name = new_name

# дочерний класс для администраторов

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'

    def add_user(self, users_list, user):
        users_list.append(user)
        print(f'Пользователь {user.get_name()} добавлен.')

    def remove_user(self, users_list, user_id):
        for user in users_list:
            if user.get_user_id() == user_id:
                users_list.remove(user)
                print(f'Пользователь с ID {user_id} удален.')
                return
        print(f'Пользователь с ID {user_id} не найден.')





users = []
admin = Admin(1, 'Bob')
user1 = User(2, 'Alice')
user2 = User(3, 'Tom')
user3 = User(4, 'Sam')
user4 = User(5, 'Kate')
admin.add_user(users, admin)
admin.add_user(users, user1)
admin.add_user(users, user2)
admin.add_user(users, user3)
admin.add_user(users, user4)


admin.remove_user(users, 2)
print("список пользователей:")
for user in users:
    print(f'ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень: {user.get_level()}')