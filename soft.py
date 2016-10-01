"""
   Поясенння:
CurseMenu("Назва меню/підменю", "Підназва") - Створює основне меню
CommandItem("Назва","Команда") - Створюэ пункт меню який виконуэ консльну команду
menu.append_item(Пункт_меню) - Команда шо додаэ в CurseMenu пункти
"""

#
# Модуль встановлення програм
#

# Імпорт модуля методів
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu

# Основне меню
menu = CursesMenu("Install software")

# Пункти меню
all_s = CommandItem("All software", "bash bash/install.sh")
ssh = CommandItem("ssh", "sudo apt install ssh")
gparted = CommandItem("Gparted", "sudo apt install gparted")
VLC = CommandItem("VLC", "sudo apt install vlc")
screenfetch = CommandItem("screenfetch", "sudo apt install screenfetch")
flux = CommandItem("f.lux", "bash bash/f.lux.sh")
gimp = CommandItem("gimp", "sudo apt install gimp")
kdenlive = CommandItem("Kdenlive", "sudo apt install kdenlive")
wine = CommandItem("Wine", "sudo apt install wine")
rhythmbox = CommandItem("Rhythmbox", "sudo apt install rhythmbox")

# Додавання пунктів до меню
menu.append_item(all_s)
menu.append_item(ssh)
menu.append_item(gparted)
menu.append_item(VLC)
menu.append_item(screenfetch)
menu.append_item(flux)
menu.append_item(gimp)
menu.append_item(kdenlive)
menu.append_item(wine)
menu.append_item(rhythmbox)
