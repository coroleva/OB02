class User:
    def __init__(self, user_id: int, name: str):
        self.__user_id = user_id  # защищенный атрибут ID
        self.__name = name  # защищенный атрибут имени
        self.__access_level = 'user'  # уровень доступа по умолчанию 'user'

    # Методы доступа к атрибутам
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Метод для изменения имени
    def set_name(self, new_name: str):
        self.__name = new_name


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'  # уровень доступа для администраторов

    # Метод для добавления пользователя в систему
    def add_user(self, users_list: list, user: User):
        users_list.append(user)
        print(f'Пользователь {user.get_name()} добавлен.')

    # Метод для удаления пользователя из системы по ID
    def remove_user(self, users_list: list, user_id: int):
        for user in users_list:
            if user.get_user_id() == user_id:
                users_list.remove(user)
                print(f'Пользователь с ID {user_id} удален.')
                return
        print(f'Пользователь с ID {user_id} не найден.')

    # Метод для проверки уровня доступа администратора
    def get_admin_access_level(self):
        return self.__admin_access_level


# Пример использования:

users = []

# Создаем обычных пользователей
user1 = User(1, "Иван Иванов")
user2 = User(2, "Мария Петрова")

# Создаем администратора
admin = Admin(3, "Алексей Сидоров")

# Администратор добавляет пользователей в систему
admin.add_user(users, user1)
admin.add_user(users, user2)

# Проверяем список пользователей
for user in users:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

# Администратор удаляет пользователя
admin.remove_user(users, 1)

# Проверяем список пользователей после удаления
for user in users:
    print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")
