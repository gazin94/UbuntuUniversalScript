# Імпорт класа  методів отримання
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu
# Модуль SSH зможливістью запуску програм з графікою
Home = CommandItem("Home ms-7519(ivan)", "ssh -X ivan@192.168.15.102")
Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh -X ivan@192.168.15.103")
Lenovo = CommandItem("Lenovo B560(diana)", "ssh -X ivan@192.168.15.105")
Server = CommandItem("Server(home)", "ssh -X ivan@192.168.15.106")

ssh_x = CursesMenu("SSH connect with X-window support")
ssh_x.append_item(Home)
ssh_x.append_item(Acer)
ssh_x.append_item(Lenovo)
ssh_x.append_item(Server)
