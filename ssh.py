# Імпорт класа  методів отримання
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu
# Модуль для підключення по SSH
router = CommandItem("DIR 615-E4", "ssh root@192.168.15.25")
Home = CommandItem("Home ms-7519(ivan)", "ssh ivan@192.168.15.102")
Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh ivan@192.168.15.103")
Lenovo = CommandItem("Lenovo B560(diana)", "ssh ivan@192.168.15.105")
Server = CommandItem("Server(home)", "ssh ivan@192.168.15.106")

ssh_menu = CursesMenu("SSH Connect")
ssh_menu.append_item(router)
ssh_menu.append_item(Home)
ssh_menu.append_item(Acer)
ssh_menu.append_item(Lenovo)
ssh_menu.append_item(Server)