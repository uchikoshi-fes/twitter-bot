#!/bin/bash
pman=apt-get

echo "install packages"
$pman install python3 python3-pip

echo "install python library"
pip3 install --upgrade twitter
