# device_log
Track presence of device on network using MAC address.

Keep track of device presence on a network. Use it to keep track of when I was home or away. You will need to have python 3 installed and run on Linux. Install arp-scan, then set up a cron job to run the bash script every few minutes. It will have a log.txt file with timestamps and device presence at that time.

Steps:

1. sudo apt-get install arp-scan
2. run tracker.py in in_out_py with option -h for more information 
