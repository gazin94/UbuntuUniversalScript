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
    __all_s = CommandItem("All software", "bash bash/remove.sh")
    __ssh = CommandItem("ssh", "sudo apt autoremove ssh")
    __gparted = CommandItem("Gparted", "sudo apt autoremove gparted")
    __VLC = CommandItem("VLC", "sudo apt autoremove vlc")
    __screenfetch = CommandItem("screenfetch", "sudo apt autoremove screenfetch")
    __flux = CommandItem("f.lux", "sudo apt autoremove flux")
    __gimp = CommandItem("gimp", "sudo apt autoremove gimp")
    __kdenlive = CommandItem("Kdenlive", "sudo apt autoremove kdenlive")
    __wine = CommandItem("Wine", "sudo apt autoremove wine")
    __rhythmbox = CommandItem("Rhythmbox", "sudo apt autoremove rhythmbox")

    # Додавання пунктів до меню
    menu.append_item(__all_s)
    menu.append_item(__ssh)
    menu.append_item(__gparted)
    menu.append_item(__VLC)
    menu.append_item(__screenfetch)
    menu.append_item(__flux)
    menu.append_item(__gimp)
    menu.append_item(__kdenlive)
    menu.append_item(__wine)
    menu.append_item(__rhythmbox)


class InstallSoft:
    """
    #
    # Модуль встановлення програм
    #
    """

    # Основне меню
    menu = CursesMenu("Install software", "DEPENDENCES!!!")

    # Пункти меню
    __all_s = CommandItem("All software", "bash bash/install.sh")
    __ssh = CommandItem("ssh", "sudo apt install ssh")
    __gparted = CommandItem("Gparted", "sudo apt install gparted")
    __VLC = CommandItem("VLC", "sudo apt install vlc")
    __screenfetch = CommandItem("screenfetch", "sudo apt install screenfetch")
    __flux = CommandItem("f.lux", "bash bash/f.lux.sh")
    __gimp = CommandItem("gimp", "sudo apt install gimp")
    __kdenlive = CommandItem("Kdenlive", "sudo apt install kdenlive")
    __wine = CommandItem("Wine", "sudo apt install wine")
    __rhythmbox = CommandItem("Rhythmbox", "sudo apt install rhythmbox")

    # Додавання пунктів до меню
    menu.append_item(__all_s)
    menu.append_item(__ssh)
    menu.append_item(__gparted)
    menu.append_item(__VLC)
    menu.append_item(__screenfetch)
    menu.append_item(__flux)
    menu.append_item(__gimp)
    menu.append_item(__kdenlive)
    menu.append_item(__wine)
    menu.append_item(__rhythmbox)


class SSH:
    """
   #
   # SSH підключення
   #
    """

    # Основне меню
    menu = CursesMenu("SSH Connect")

    # Пунктии меню
    __router = CommandItem("DIR 615-E4", "ssh root@192.168.15.25")
    __Home = CommandItem("Home ms-7519(ivan)", "ssh ivan@192.168.15.102")
    __Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh ivan@192.168.15.103")
    __Lenovo = CommandItem("Lenovo B560(diana)", "ssh ivan@192.168.15.105")
    __Server = CommandItem("Server(home)", "ssh ivan@192.168.15.106")

    # Додавання пунктів до меню
    menu.append_item(__router)
    menu.append_item(__Home)
    menu.append_item(__Acer)
    menu.append_item(__Lenovo)
    menu.append_item(__Server)


class SshX:

    """
    #
    # Модуль підключення SSH з підтримкою запуска програм з графічним інтерфейсом
    #
    """

    menu = CursesMenu("SSH connect with X-window support")

    # Пункти
    __Home = CommandItem("Home ms-7519(ivan)", "ssh -X ivan@192.168.15.102")
    __Acer = CommandItem("Acer-aspire V5-131(ivan)", "ssh -X ivan@192.168.15.103")
    __Lenovo = CommandItem("Lenovo B560(diana)", "ssh -X ivan@192.168.15.105")
    __Server = CommandItem("Server(home)", "ssh -X ivan@192.168.15.106")

    #  Додаваня пунктів до меню
    menu.append_item(__Home)
    menu.append_item(__Acer)
    menu.append_item(__Lenovo)
    menu.append_item(__Server)


class Xfce:

    """
    #
    # Модуль налаштувань для XFCE
    #
    """

    # Основне меню
    menu = CursesMenu("XFCE soft")

    # Пункти меню
    __all_s = CommandItem("All remove", "bash bash/xfce.sh")
    __notes = CommandItem("Remove XFCE4-Notes", "sudo apt autoremove xfce4-notes")
    __pidgin = CommandItem("Remove Pidgin", "sudo apt autoremove pidgin")
    __thunderbird = CommandItem("Remove Thunderbird", "sudo apt autoremove thunderird")
    __parole = CommandItem("Remove Parole", "sudo apt autoremove parole")
    __gnome_sudoku = CommandItem("Remove Sudoku", "sudo apt autoremove gnome-sudoku")
    __gnome_mines = CommandItem("Remove Mines", "sudo apt autoremove gnome-mines")
    __firefox = CommandItem("Remove firefox", "sudo apt autoremove firefox")

    # Додавання пунктів до меню
    menu.append_item(__all_s)
    menu.append_item(__notes)
    menu.append_item(__pidgin)
    menu.append_item(__thunderbird)
    menu.append_item(__parole)
    menu.append_item(__gnome_sudoku)
    menu.append_item(__gnome_mines)
    menu.append_item(__firefox)
