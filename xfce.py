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
# Модуль налаштувань для XFCE
#

# Основне меню
menu = CursesMenu("XFCE soft")

# Пункти меню
all_s = CommandItem("All remove", "bash bash/xfce.sh")
notes = CommandItem("Remove XFCE4-Notes", "sudo apt autoremove xfce4-notes")
pidgin = CommandItem("Remove Pidgin", "sudo apt autoremove pidgin")
thunderbird = CommandItem("Remove Thunderbird", "sudo apt autoremove thunderird")
parole = CommandItem("Remove Parole", "sudo apt autoremove parole")
gnome_sudoku = CommandItem("Remove Sudoku", "sudo apt autoremove gnome-sudoku")
gnome_mines = CommandItem("Remove Mines", "sudo apt autoremove gnome-mines")
firefox = CommandItem("Remove firefox", "sudo apt autoremove firefox")

# Додавання пунктів до меню
menu.append_item(all_s)
menu.append_item(notes)
menu.append_item(pidgin)
menu.append_item(thunderbird)
menu.append_item(parole)
menu.append_item(gnome_sudoku)
menu.append_item(gnome_mines)
menu.append_item(firefox)
