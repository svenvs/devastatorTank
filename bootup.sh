#!/bin/bash
cd /home/pi/devastatorTank
git checkout main
git pull
/usr/bin/python3 main.py
