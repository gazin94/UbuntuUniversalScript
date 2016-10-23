"""
    Подяка:
Thanks pmbarrett314 from curses-menu 0.5
link: https://pypi.python.org/pypi/curses-menu/0.5.0
Need: Python 2.7, 3.3, 3.4, and 3.5

    Read me!!:
Ubuntu need packages:
pip3(sudo apt-get install python3-pip)
pip install curses-menu
pip3 install curses-menu(Python3+)

    Поясенння:
CurseMenu("Назва меню/підменю", "Підназва") - Створює основне меню
CommandItem("Назва","Команда") - Створюэ пункт меню який виконуэ консльну команду
SubmenuItem("Назва",Підменю,основне_меню) - Стврює підменю для CurseMenu
menu.append_item(Пункт_меню) - Команда шо додаэ в CurseMenu пункти
menu.show() - Показує меню в термніналі для підменю не потрібно бо зразу малює підменю
і при виході малює основне меню
"""

#
# Основне меню. Запускати програму з цього файла
#

# Класи для створення меню
from cursesmenu import CursesMenu
from cursesmenu.items import CommandItem, SubmenuItem
from os import getlogin

# Класи дій для підменю
# import soft
# import ssh
# import ssh_X
# import remove
# import xfce
from modules import InstallSoft as soft
from modules import RemoveProgram as remove
from modules import SSH as ssh
from modules import SshX as ssh_X
from modules import Xfce as xfce
# Створення основного меню
menu = CursesMenu("\033[31m Ubuntu universal script \033[31m ", "Hello "+str(getlogin()))
# Створення основних пунктів
update = CommandItem("Update paсkages", "sudo apt update")
upgrade = CommandItem("Upgrade paсkages", "sudo apt upgrade")
autoremove = CommandItem("Autoremove paсkages", "sudo apt autoremove")
remove_kernel = CommandItem("Remove other kernel`s", "bash bash/remove_kernel.sh")
pickings = CommandItem("Cleaning pickings removed paсkages",
                       "sudo dpkg -l | awk '/^rc/ {print $2}' | xargs sudo dpkg --purge")

# Відображення підменю
soft = SubmenuItem("Install soft", soft.menu, menu)
remove = SubmenuItem("Remove software", remove.menu, menu)
xfce = SubmenuItem("Xfce soft", xfce.menu, menu)
SSH = SubmenuItem("SSH Connect", ssh.menu, menu)
SSH_X = SubmenuItem("SSH connect with X-window support", ssh_X.menu, menu)

# Додавання пунктів до основного меню
menu.append_item(update)
menu.append_item(upgrade)
menu.append_item(autoremove)
menu.append_item(pickings)
menu.append_item(remove_kernel)
menu.append_item(soft)
menu.append_item(soft)
menu.append_item(remove)
menu.append_item(SSH)
menu.append_item(SSH_X)

# Показ меню
menu.show()



