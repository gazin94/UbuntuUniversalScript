# Імпорт класа  методів отримання
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu
# Модуль SSH зможливістью запуску програм з графікою
Home = CommandItem("Home ms-7519(ivan)", "ssh -X ivan@192.168.15.102")
Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh -X ivan@192.168.15.103")
Lenovo = CommandItem("Lenovo B560(diana)", "ssh -X ivan@192.168.15.105")
Server = CommandItem("Server(home)", "ssh -X ivan@192.168.15.106")

menu = CursesMenu("SSH connect with X-window support")
menu.append_item(Home)
menu.append_item(Acer)
menu.append_item(Lenovo)
menu.append_item(Server)
