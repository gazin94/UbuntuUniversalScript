"""
   Поясенння:
CurseMenu("Назва меню/підменю", "Підназва") - Створює основне меню
CommandItem("Назва","Команда") - Створюэ пункт меню який виконуэ консльну команду
menu.append_item(Пункт_меню) - Команда шо додаэ в CurseMenu пункти
"""

# Імпорт модуля методів
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu

#
# Модуль підключення SSH з підтримкою запуска програм з графічним інтерфейсом
#

# Основне меню
menu = CursesMenu("SSH connect with X-window support")

# Пункти
Home = CommandItem("Home ms-7519(ivan)", "ssh -X ivan@192.168.15.102")
Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh -X ivan@192.168.15.103")
Lenovo = CommandItem("Lenovo B560(diana)", "ssh -X ivan@192.168.15.105")
Server = CommandItem("Server(home)", "ssh -X ivan@192.168.15.106")

#  Додаваня пунктів до меню
menu.append_item(Home)
menu.append_item(Acer)
menu.append_item(Lenovo)
menu.append_item(Server)
