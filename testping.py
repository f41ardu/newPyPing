import newping

ping = newping.Ping("localhost",1,1)

print(ping.ping())
print(ping.ping("11.4.1.1",1,1))