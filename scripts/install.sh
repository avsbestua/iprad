#!/bin/bash

curl -o iprad.zip -L https://github.com/avsbestua/iprad/archive/refs/heads/main.zip
unzip iprad.zip

cd iprad

pip3 install -e .

echo "Install finished. Press enter to exit"
read