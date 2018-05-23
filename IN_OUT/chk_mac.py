import os
import datetime
import time

dir_reading = '/home/pi/Desktop/IN_OUT/reading.txt'
dir_on_off = '/home/pi/Desktop/IN_OUT/ON_OFF.txt'
dir_log = '/home/pi/Desktop/IN_OUT/log.txt'
mac_addr = 'xx:xx:xx:xx:xx:xx'

for i in range(0,10):
    os.system('sudo arp-scan -l > reading.txt')

    with open(dir_reading, 'r') as f:
        reading = f.read()

    with open(dir_on_off,'a') as g:
        if mac_addr in reading:
            g.write('on,')
        else:
            g.write('off,')
    time.sleep(3)

with open(dir_on_off,'r') as j:
    test = j.read().split(',')

with open(dir_log, 'a') as h:
    if ('on' in test[-11:]):
        h.write(str(datetime.datetime.now()) + ': in' + '\n')
        print('checked in')
    elif ('on' not in test[-11:]):
        h.write(str(datetime.datetime.now()) + ': out or wifi off' + '\n')
        print('checked out')
    else:
        print('no change')

if len(test) > 11:
    test = test[-11:]
    with open(dir_on_off,'w') as k:
        k.write(','.join(test))
    
        
    
