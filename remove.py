# Імпорт класа  методів отримання
from cursesmenu.items import CommandItem
from cursesmenu import CursesMenu

menu = CursesMenu("Remove software")
all_s = CommandItem("All software", "bash bash/remove.sh")
ssh = CommandItem("ssh", "sudo apt autoremove ssh")
gparted = CommandItem("Gparted", "sudo apt autoremove gparted")
VLC = CommandItem("VLC", "sudo apt autoremove vlc")
screenfetch = CommandItem("screenfetch", "sudo apt autoremove screenfetch")
flux = CommandItem("f.lux", "sudo apt autoremove flux")
gimp = CommandItem("gimp", "sudo apt autoremove gimp")
kdenlive = CommandItem("Kdenlive", "sudo apt autoremove kdenlive")
wine = CommandItem("Wine", "sudo apt autoremove wine")
rhythmbox = CommandItem("Rhythmbox", "sudo apt autoremove rhythmbox")

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
