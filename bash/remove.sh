#!/bin/bash
#Install script
clear
echo "Remove main programs"
sudo apt update
sudo apt autoremove gparted
sudo apt autoremove wine
sudo apt autoremove screenfetch
sudo apt autoremove vlc
sudo apt autoremove rhythmbox
sudo apt autoremove gimp
sudo apt autoremove kdenlive
sudo apt autoremove ssh
sudo apt-get autoremove fluxgui