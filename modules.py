"""
   Поясенння:
CurseMenu("Назва меню/підменю", "Підназва") - Створює основне меню
CommandItem("Назва","Команда") - Створюэ пункт меню який виконуэ консльну команду
menu.append_item(Пункт_меню) - Команда шо додаэ в CurseMenu пункти
"""

# Імпорт модуля методів
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu


class RemoveProgram:
    """
    #
    # Видалення програм
    #
    """

    # Основне меню
    menu = CursesMenu("Remove software", "YOU DELETE SOFT!!!")

    # Пункти меню
    _menu_items = [
        CommandItem("All software", "bash bash/remove.sh"),
        CommandItem("ssh", "sudo apt autoremove ssh"),
        CommandItem("Gparted", "sudo apt autoremove gparted"),
        CommandItem("VLC", "sudo apt autoremove vlc"),
        CommandItem("screenfetch", "sudo apt autoremove screenfetch"),
        CommandItem("f.lux", "sudo apt autoremove flux"),
        CommandItem("gimp", "sudo apt autoremove gimp"),
        CommandItem("Kdenlive", "sudo apt autoremove kdenlive"),
        CommandItem("Wine", "sudo apt autoremove wine"),
        CommandItem("Rhythmbox", "sudo apt autoremove rhythmbox")
    ]
    # Додавання пунктів до меню
    for item in _menu_items:
        menu.append_item(item)


class InstallSoft:
    """
    #
    # Модуль встановлення програм
    #
    """

    # Основне меню
    menu = CursesMenu("Install software", "DEPENDENCES!!!")

    # Пункти меню
    _menu_items = [
        CommandItem("All software", "bash bash/install.sh"),
        CommandItem("ssh", "sudo apt install ssh"),
        CommandItem("Gparted", "sudo apt install gparted"),
        CommandItem("VLC", "sudo apt install vlc"),
        CommandItem("screenfetch", "sudo apt install screenfetch"),
        CommandItem("f.lux", "bash bash/f.lux.sh"),
        CommandItem("gimp", "sudo apt install gimp"),
        CommandItem("Kdenlive", "sudo apt install kdenlive"),
        CommandItem("Wine", "sudo apt install wine"),
        CommandItem("Rhythmbox", "sudo apt install rhythmbox")
    ]

    # Додавання пунктів до меню
    for item in _menu_items:
        menu.append_item(item)


class SSH:
    """
   #
   # SSH підключення
   #
    """

    # Основне меню
    menu = CursesMenu("SSH Connect")

    # Пунктии меню
    _menu_items = [
        CommandItem("DIR 615-E4", "ssh root@192.168.15.25"),
        CommandItem("Home ms-7519(ivan)", "ssh ivan@192.168.15.102"),
        CommandItem("Acer-aspire V5-131(ivan)", "ssh ivan@192.168.15.103"),
        CommandItem("Lenovo B560(diana)", "ssh ivan@192.168.15.105"),
        CommandItem("Server(home)", "ssh ivan@192.168.15.106")
    ]

    # Додавання пунктів до меню
    for item in _menu_items:
        menu.append_item(item)


class SshX:
    """
    #
    # Модуль підключення SSH з підтримкою запуска програм з графічним інтерфейсом
    #
    """

    menu = CursesMenu("SSH connect with X-window support")

    # Пункти
    _menu_items = [
        CommandItem("Home ms-7519(ivan)", "ssh -X ivan@192.168.15.102"),
        CommandItem("Acer-aspire V5-131(ivan)", "ssh -X ivan@192.168.15.103"),
        CommandItem("Lenovo B560(diana)", "ssh -X ivan@192.168.15.105"),
        CommandItem("Server(home)", "ssh -X ivan@192.168.15.106")
    ]

    #  Додаваня пунктів до меню
    for item in _menu_items:
        menu.append_item(item)


class Xfce:
    """
    #
    # Модуль налаштувань для XFCE
    #
    """

    # Основне меню
    menu = CursesMenu("XFCE soft")

    # Пункти меню
    _menu_items = [
        CommandItem("All remove", "bash bash/xfce.sh"),
        CommandItem("Remove XFCE4-Notes", "sudo apt autoremove xfce4-notes"),
        CommandItem("Remove Pidgin", "sudo apt autoremove pidgin"),
        CommandItem("Remove Thunderbird", "sudo apt autoremove thunderird"),
        CommandItem("Remove Parole", "sudo apt autoremove parole"),
        CommandItem("Remove Sudoku", "sudo apt autoremove gnome-sudoku"),
        CommandItem("Remove Mines", "sudo apt autoremove gnome-mines"),
        CommandItem("Remove firefox", "sudo apt autoremove firefox")
    ]

    # Додавання пунктів до меню
    for item in _menu_items:
        menu.append_item(item)
