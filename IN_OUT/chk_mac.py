import os
import datetime
import time

for i in range(0,10):
    os.system('sudo arp-scan -l > reading.txt')

    with open('/home/pi/Desktop/IN_OUT/reading.txt', 'r') as f:
        reading = f.read()

    with open('/home/pi/Desktop/IN_OUT/ON_OFF.txt','a') as g:
        if '84:98:66:7f:95:87' in reading:
            g.write('on,')
        else:
            g.write('off,')
    time.sleep(3)

with open('/home/pi/Desktop/IN_OUT/ON_OFF.txt','r') as j:
    test = j.read().split(',')

with open('/home/pi/Desktop/IN_OUT/log.txt', 'a') as h:
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
    with open('/home/pi/Desktop/IN_OUT/ON_OFF.txt','w') as k:
        k.write(','.join(test))
    
        
    
