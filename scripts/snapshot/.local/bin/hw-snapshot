#!/bin/bash

dir_name=hardware_snapshot$(date +%Y_%m_%d-%H_%M_%S)

mkdir -p $dir_name

sudo dmidecode >$dir_name/dmidecode.txt
sudo lshw >$dir_name/lshw.txt
sudo lspci -vv >$dir_name/lspci.txt
lsusb >$dir_name/lsusb.txt
lsblk -a >$dir_name/lsblk.txt

sudo smartctl -a /dev/nvme0n1 >$dir_name/nvme_smart.txt

inxi -Fxxxz >$dir_name/inxi.txt

uname -a >$dir_name/kernel.txt

echo "Done."
