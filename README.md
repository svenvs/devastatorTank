# devastatorTank

## connect to pi
- Look up your device using LanScan
- `ssh pi@xxx.xxx.x.xxx`
- enter password

## how to run
- Go to directory `devastatorTank`
- Ensure required packages are installed: `pip3 install -r requirements.txt`
- Run command `sudo python3 main.py`

## start on boot
link for boot:
https://raspberrypi-guide.github.io/programming/run-script-on-boot

bash -c '/usr/bin/python3 /home/pi/devastatorTank/main.py > /home/pi/mylog.log 2>&1' &

## Handy links
- [A guide for headless configuration of Raspberry Pi](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)
