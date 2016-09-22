"""
Thanks pmbarrett314 from curses-menu 0.5
link: https://pypi.python.org/pypi/curses-menu/0.5.0
"""
# Класи для створення меню
from cursesmenu import CursesMenu
from cursesmenu.items import CommandItem, SubmenuItem
from os import getlogin
# Класи дій для підменю
import soft
import ssh
import ssh_X
import remove
import xfce

# Створення основного меню
menu = CursesMenu("Ubuntu universal script", "Hello "+str(getlogin()))
# Створення основних пунктів
update = CommandItem("Update pakages", "sudo apt update")
upgrade = CommandItem("Upgrade pakages", "sudo apt upgrade")
autoremove = CommandItem("Autoremove pakages", "sudo apt autoremove")
remove_kernel = CommandItem("Remove other kernel`s", "bash bash/remove_kernel.sh")
# Відображення підменю
soft = SubmenuItem("Install soft", soft.menu, menu)
remove = SubmenuItem("Remove software", remove.menu, menu)
xfce = SubmenuItem("Xfce soft", xfce.menu, menu)
SSH = SubmenuItem("SSH Connect", ssh.ssh_menu, menu)
SSH_X = SubmenuItem("SSH connect with X-window support", ssh_X.menu, menu)
# Додавання пунктів до основного меню
menu.append_item(update)
menu.append_item(upgrade)
menu.append_item(autoremove)
menu.append_item(remove_kernel)
menu.append_item(soft)
menu.append_item(xfce)
menu.append_item(SSH)
menu.append_item(SSH_X)
# Показ меню
menu.show()
