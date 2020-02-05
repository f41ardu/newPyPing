# newPyPing

Simple phyton ping library

Use subprocess and built in shell commands. 
Supported so far -c : counts and -t : timeout 

Usage: 

import newping

ping = newping.Ping("localhost",1,1)

print(ping.ping())
print(ping.ping("11.4.1.1",1,1))

>>> %Run testping.py
True
False
