#!/bin/bash
git -C /home/pi/devastatorTank checkout main
git -C /home/pi/devastatorTank pull
/usr/bin/python3 /home/pi/devastatorTank/main.py
