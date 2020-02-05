# simple class to emulate ping to host
# https://stackoverflow.com/questions/35750041/check-if-ping-was-successful-using-subprocess-in-python
import subprocess
"""
    save example as testping.py
    
    import newping
    ping = newping.Ping("localhost",1,1)
    print(ping.ping())
    print(ping.ping("11.4.1.1",1,1))

    >>> %Run testping.py
    True
    False
"""
class Ping:
    def __init__(self, ipadress="127.0.0.1",t=1, c=1):
        self.address = ipadress
        self.timeout = str(t)
        self.count = str(c)
    
    def ping(self,ipadress="127.0.0.1",t=1, c=1):
        self.address = ipadress
        self.timeout = str(t)
        self.count = str(c)
        try:
            subprocess.check_output(["ping", "-c", self.count, "-w", self.timeout, self.address])
            return True                      
        except subprocess.CalledProcessError:
            return False
