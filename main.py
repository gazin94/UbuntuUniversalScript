"""
    Подяка:
Thanks pmbarrett314 from curses-menu 0.5
link: https://pypi.python.org/pypi/curses-menu/0.5.0
Need: Python 2.7, 3.3, 3.4, and 3.5

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
import platform

from modules import InstallSoft as soft
from modules import RemoveProgram as remove
from modules import SSH as ssh
from modules import SshX as ssh_X
from modules import Xfce as xfce

# Створення основного меню
menu = CursesMenu("Ubuntu universal script", platform.version())
# Створення основних пунктів
_menu_items = [
    CommandItem("Update paсkages", "sudo apt update"),
    CommandItem("Upgrade paсkages", "sudo apt upgrade"),
    CommandItem("Autoremove paсkages", "sudo apt autoremove"),
    CommandItem("Remove other kernel`s", "bash bash/remove_kernel.sh"),
    CommandItem("Cleaning pickings removed paсkages",
                "sudo dpkg -l | awk '/^rc/ {print $2}' | xargs sudo dpkg --purge"),

    # Відображення підменю

    SubmenuItem("Install soft", soft.menu, menu),
    SubmenuItem("Remove software", remove.menu, menu),
    SubmenuItem("Xfce soft", xfce.menu, menu),
    SubmenuItem("SSH Connect", ssh.menu, menu),
    SubmenuItem("SSH connect with X-window support", ssh_X.menu, menu)
]

# Додавання пунктів до основного меню
for item in _menu_items:
    menu.append_item(item)

# Показ меню
menu.show()
