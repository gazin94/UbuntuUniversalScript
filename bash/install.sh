#!/bin/bash
#Install script
clear
echo "Installing main programs"
sleep 10s
sudo apt update
sudo apt install gparted
sudo apt install vine
sudo apt install screenfetch
sudo apt install vlc
sudo apt install nautilus
sudo apt install nautilus-share
sudo apt install samba
sudo apt install ssh

#Installing f.lux
sudo add-apt-repository ppa:nathan-renniewaldock/flux
sudo apt-get update
sudo apt-get install fluxgui


