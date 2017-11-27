# device_log
Track presence of device on network using MAC address.

Just a program I made to keep track of device presence on a network. I personally use it to keep track of when I was home or away. You will need to have python 3 installed and run on Linux. Install arp-scan, then set up a cron job to run the bash script every few minutes. It will have a log.txt file with timestamps and device presence at that time.

Steps:

1. sudo apt-get install arp-scan
2. go into chk_mac.py and change necessary file paths and mac address of the device you wish to keep track of
3. setup cron job to run check_mac.sh
4. reboot
