# Класи для створення меню
from cursesmenu import CursesMenu
from cursesmenu.items import CommandItem, SubmenuItem
# Класи дій для підменю
import soft
import ssh
import ssh_X
import xfce

# Створення основного меню
menu = CursesMenu("Ubuntu universal script")
# Підменю
submenu = CursesMenu("lol")
# Пункти підменю
soft = SubmenuItem("Install soft", submenu, menu)
# Створення основних пунктів
update = CommandItem("Update pakages", "sudo apt update")
upgrade = CommandItem("Upgrade pakages", "sudo apt upgrade")
autoremove = CommandItem("Autoremove pakages", "sudo apt autoremove")
remove_kernel=CommandItem("Remove other kernel`s", "bash bash/remove_kernel.sh")
# Відображення підменю
ls = CommandItem("ls", "ls && sleep 10")
submenu.append_item(ls)


SSH = SubmenuItem("SSH Connect", ssh.ssh_menu, menu)
SSH_X = SubmenuItem("SSH connect with X-window support", ssh_X.ssh_x, menu)
# Додавання пунктів до основного меню
menu.append_item(update)
menu.append_item(upgrade)
menu.append_item(autoremove)
menu.append_item(remove_kernel)
menu.append_item(soft)
menu.append_item(SSH)
menu.append_item(SSH_X)
# Показ меню
menu.show()
