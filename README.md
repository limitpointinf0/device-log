# device_log
Track presence of device on network using MAC address.

Steps:

1. sudo apt-get install arp-scan
2. go into chk_mac.py and change necessary file paths and mac address of the device you wish to keep track of
3. setup cron job to run check_mac.sh
4. reboot
