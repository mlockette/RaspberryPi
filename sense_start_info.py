#sense_start_info.py
#sensehat startup info display.

from sense_hat import SenseHat
import netifaces as ni
import time
import subprocess
from subprocess import PIPE
import re


sense = SenseHat()
sense.low_light = True
#sense.set_rotation(180)
green = (0,255,0)

ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[2][0]['addr']
print (ip)
#print (type(ip))
#sense.show_message("Wlan ip is: ", text_colour=green)
#sense.show_message(ip, text_colour=green)
#subprocess.call(["ps", "ax"])
cmd = "ps ax"
p = subprocess.Popen(cmd, shell=True, stdout=PIPE)
i = 0

while True or i > 7000:
    out = p.stdout.read()
    #print(out)
    sout = out.decode(encoding='UTF-8')
    #print(sout)
    
    #print(type(out))
    if out == '' and p.poll() != None:
        break
    if 'Xtightvnc' in sout:
        print("found vnc ps")
        #print(type(sout))
        #print(sout)
        port = re.search(r'Xtightvnc :*(\d*)', sout) 
        break
vncport = port.group(0)
print(vncport)
#print(type(port))


while True:
    sense.show_message(vncport, text_colour=green)
    sense.show_message("Wlan ip is: ", text_colour=green)
    sense.show_message(ip, text_colour=green)
    if input():
        break
    
