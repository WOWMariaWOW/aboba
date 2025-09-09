import getpass

# База данных пользователей (в реальном приложении используйте БД)
users = {
    "admin": "password123",
    "user1": "hello123",
    "test": "test123"
}

def login():
    print("=== СИСТЕМА АВТОРИЗАЦИИ ===")
    
    username = input("Введите логин: ")
    password = getpass.getpass("Введите пароль: ")
    
    if username in users and users[username] == password:
        print(f"Добро пожаловать, {username}!")
        return True
    else:
        print("Неверный логин или пароль!")
        return False

def main_menu():
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print("1. Посмотреть информацию")
    print("2. Настройки")
    print("3. Выход")
    
    choice = input("Выберите пункт меню: ")
    return choice

def main():
    # Попытка авторизации
    if not login():
        print("Авторизация не удалась. Выход...")
        return
    
    # Основной цикл программы
    while True:
        choice = main_menu()
        
        if choice == "1":
            print("Это секретная информация!")
        elif choice == "2":
            print("Настройки системы...")
        elif choice == "3":
            print("Выход из системы...")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()