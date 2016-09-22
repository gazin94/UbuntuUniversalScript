#!/bin/bash
#Install script
clear
echo "Installing programs"
sudo apt update
sudo apt install gparted
sudo apt install wine
sudo apt install screenfetch
sudo apt install vlc
sudo apt install rhythmbox
sudo apt install gimp
sudo apt install kdenlive
sudo apt install ssh

#Installing f.lux
sudo add-apt-repository ppa:nathan-renniewaldock/flux
sudo apt-get update
sudo apt-get install fluxgui


