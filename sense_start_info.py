#sense_start_info.py
#Built by Michael Lockette, Lockette Down Security LLC
# SenseHat startup info for tightVNC display
# and wlan IP Address displayed across LED pad for user use upon bootup.

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from sense_hat import SenseHat
import netifaces as ni
import time
import subprocess
from subprocess import PIPE
import re


sense = SenseHat()
'''
I personally feel I can read the message across the LED pad with a low
 low light setting.  That is what the line below changes.
'''
sense.low_light = True

green = (0,255,0)

'''
Fetch the wlan0 ip address.  object 'ip' will hold the pi's wlan0 ip address
 for further use.
'''
ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[2][0]['addr']
print (ip)

#Next find the process id for Xthightvnc and record the 'port id'
cmd = "ps ax"
p = subprocess.Popen(cmd, shell=True, stdout=PIPE)
i = 0

while True or i > 7000:
    out = p.stdout.read()
    sout = out.decode(encoding='UTF-8')
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

'''
Lastly create loop for continous printing of the information collected.
 This portion is not quite a finished product,
 just like any project... its truely never done...
 The while loop only iterates once through the code.
 then waits for an input to occur.
'''
while True:
    sense.show_message(vncport, text_colour=green)
    sense.show_message("Wlan ip is: ", text_colour=green)
    sense.show_message(ip, text_colour=green)
    if input():
        break
    
