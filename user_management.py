# Пользовательские исключения

class UserAlreadyExistsError(Exception):
    """Исключение, выбрасываемое при попытке добавить пользователя с уже существующим именем."""
    def __init__(self, username):
        super().__init__(f"User with username '{username}' already exists.")
        self.username = username


class UserNotFoundError(Exception):
    """Исключение, выбрасываемое, если пользователь с указанным именем не найден."""
    def __init__(self, username):
        super().__init__(f"User with username '{username}' not found.")
        self.username = username


# Класс для пользователя

class User:
    """Класс, представляющий пользователя."""

    def __init__(self, username, email, age):
        self.username = username  # Имя пользователя
        self.email = email        # Электронная почта пользователя
        self.age = age            # Возраст пользователя

    def __str__(self):
        """Возвращает строковое представление объекта User."""
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"


# Класс для управления пользователями

class UserManager:
    """Класс для управления пользователями в системе."""

    def __init__(self):
        self.users = {}  # Словарь пользователей, где ключ — имя пользователя

    def add_user(self, user: User):
        """Добавляет пользователя в систему.
        Выбрасывает исключение UserAlreadyExistsError, если пользователь с таким именем уже существует."""
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user

    def remove_user(self, username: str):
        """Удаляет пользователя из системы.
        Выбрасывает исключение UserNotFoundError, если пользователь с таким именем не найден."""
        if username not in self.users:
            raise UserNotFoundError(username)
        del self.users[username]

    def find_user(self, username: str) -> User:
        """Находит пользователя по имени.
        Выбрасывает исключение UserNotFoundError, если пользователь не найден."""
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]



def main():
    user_manager = UserManager()

    # Пробуем добавить пользователей
    try:
        user1 = User("john_doe", "john@example.com", 30)
        user_manager.add_user(user1)
        print(f"Added: {user1}")

        user2 = User("jane_doe", "jane@example.com", 25)
        user_manager.add_user(user2)
        print(f"Added: {user2}")

        # Пробуем добавить пользователя с уже существующим именем
        duplicate_user = User("john_doe", "john_duplicate@example.com", 40)
        user_manager.add_user(duplicate_user)
    except UserAlreadyExistsError as e:
        print(f"Error: {e}")

    # Пробуем найти пользователя
    try:
        found_user = user_manager.find_user("jane_doe")
        print(f"Found: {found_user}")

        # Пробуем найти несуществующего пользователя
        not_existing_user = user_manager.find_user("non_existent")
    except UserNotFoundError as e:
        print(f"Error: {e}")

    # Пробуем удалить пользователя
    try:
        user_manager.remove_user("jane_doe")
        print("User 'jane_doe' removed successfully.")

        # Пробуем удалить несуществующего пользователя
        user_manager.remove_user("non_existent")
    except UserNotFoundError as e:
        print(f"Error: {e}")


# Запуск основной функции
if __name__ == "__main__":
    main()
