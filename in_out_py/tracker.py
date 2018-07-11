#!/usr/bin/env python
import os
from datetime import datetime, timedelta
import time
import subprocess
import re
import argparse

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.")

class DeviceTracker():

    def __init__(self, mac=None, times=10, t_int=3):
        '''mac(str): mac address you want to track
        times(int): times you would like it to check connectivity before determining presence
        t_int(int): time interval in seconds between each check
        '''
        
        self.mac = mac 
        self.freq = times
        self.t_int = t_int
        self.onoff = None
        self.reading = None
        self.rawoutput = None
        self.presence = []

    def getReading(self):
        '''get all mac addresses found'''
        self.rawoutput = subprocess.check_output(['arp-scan', '-l'])
        self.rawoutput = self.rawoutput.decode('utf-8')
        m = re.compile('[a-z0-9]{2}' + ':[a-z0-9]{2}'*5)
        self.reading = m.findall(self.rawoutput)
        return self.reading

    def getOnOff(self):
        '''try to get the device connectivity'''
        if self.mac in self.getReading():
            self.onoff = True
        else:
            self.onoff = False
        return self.onoff

    def getPresence(self):
        '''get the connectivity of the device for the amount of times specified in freq'''
        self.presence = []
        for i in range(self.freq):
            self.presence.append(self.getOnOff())
            time.sleep(self.t_int)
        return self.presence

    def actualPresence(self):
        '''if the device was found connected on at least on try within freq count it as connected'''
        if sum(self.getPresence()) > 0:
            return True
        else:
            return False

    def writeResult(self):
        '''writes result of presence to file'''
        t = datetime.now().strftime('%Y%m%d %H%M%S')
        if not os.path.exists('devices/' + self.mac + '.txt'):
            f = open('devices/' + self.mac + '.txt', 'w')
            f.close()
        if self.actualPresence():
            with open('devices/' + self.mac + '.txt', 'a+') as f:
                f.write('{},{},{}'.format(t, self.mac, 'connected'))
                print('{},{},{}\n'.format(t, self.mac, 'connected'))
        else:
            with open('devices/' + self.mac + '.txt', 'a+') as f:
                f.write('{},{},{}'.format(t , self.mac, 'not connected'))
                print('{},{},{}\n'.format(t, self.mac, 'not connected'))

    def startLoop(self, until=(0,5)):
        '''start loop to write connectivity of device to file till specified time
        until(tuple): (hours,minutes)
        '''
        if until:
            end_at = datetime.now() + timedelta(hours=until[0], minutes=until[1])
            while datetime.now() < end_at:
                self.writeResult()
        else:
            while True:
                self.writeResult()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='track presence of device with given mac address')
    parser.add_argument('-d', '--mac', help='(str) mac address of device')
    parser.add_argument('-H', '--hours', help='(int) hours duration', default=0)
    parser.add_argument('-m', '--mins', help='(int) minutes duration', default=5)
    args = parser.parse_args()

    me = DeviceTracker(mac=args.mac)
    me.startLoop(until=(args.hours, args.mins))
    print 'stopped'
        
