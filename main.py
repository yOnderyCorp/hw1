import colorama
from inspect import getmembers, isclass, isfunction

# Инициализация (важно для Windows)
colorama.init()

print(f"{colorama.Fore.CYAN}--- Интроспекция библиотеки Colorama ---{colorama.Style.RESET_ALL}\n")

# 1. Основные атрибуты через dir()
all_attributes = dir(colorama)
print(f"Список всех атрибутов: {all_attributes}\n")

# 2. Выделение самых важных атрибутов и методов
important_stuff = {
    "Fore": colorama.Fore,  # Цвета текста
    "Back": colorama.Back,  # Цвета фона
    "Style": colorama.Style,  # Стили (жирный, яркость и т.д.)
    "init": colorama.init  # Функция инициализации
}

print(f"{colorama.Fore.YELLOW}Ключевые компоненты и их описание:{colorama.Style.RESET_ALL}")

for name, obj in important_stuff.items():
    obj_type = type(obj)
    print(f"Элемент: {colorama.Fore.GREEN}{name}{colorama.Style.RESET_ALL}")
    print(f"  - Тип: {obj_type}")

    # Комментарии к работе
    if name == "init":
        print("  - Описание: Настраивает терминал для корректного отображения ANSI-кодов (особенно важно в Windows).")
    elif name in ["Fore", "Back"]:
        print(
            f"  - Описание: Содержит набор строковых констант для смены цвета. Доступные цвета: {', '.join([a for a in dir(obj) if not a.startswith('_')])}")
    elif name == "Style":
        print("  - Описание: Позволяет изменять яркость (BRIGHT, DIM) или сбрасывать настройки (RESET_ALL).")
    print("-" * 30)

# Пример работы
print(f"\n{colorama.Back.BLUE}{colorama.Fore.WHITE} ПРИМЕР: Синий фон, белый текст {colorama.Style.RESET_ALL}")git init
