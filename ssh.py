"""
   Поясенння:
CurseMenu("Назва меню/підменю", "Підназва") - Створює основне меню
CommandItem("Назва","Команда") - Створюэ пункт меню який виконуэ консльну команду
menu.append_item(Пункт_меню) - Команда шо додаэ в CurseMenu пункти
"""

#
# SSH підключення
#

# Імпорт модуля  методів
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu

# Основне меню
menu = CursesMenu("SSH Connect")

# Пунктии меню
router = CommandItem("DIR 615-E4", "ssh root@192.168.15.25")
Home = CommandItem("Home ms-7519(ivan)", "ssh ivan@192.168.15.102")
Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh ivan@192.168.15.103")
Lenovo = CommandItem("Lenovo B560(diana)", "ssh ivan@192.168.15.105")
Server = CommandItem("Server(home)", "ssh ivan@192.168.15.106")

# Додавання пунктів до меню
menu.append_item(router)
menu.append_item(Home)
menu.append_item(Acer)
menu.append_item(Lenovo)
menu.append_item(Server)