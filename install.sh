#!/bin/bash
pman=apt-get

echo "install packages"
$pman install python3 python3-pip

echo "install python library\n"
echo "twitter(https://github.com/sixohsix/twitter)"
pip3 install --upgrade twitter
