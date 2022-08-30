import socket
import random
hostName = socket.gethostname()
HostAddress = socket.gethostbyname(hostName);
print("My computername is: "+hostName," \n and my adress is "+HostAddress)

#print("EH")

listlen = random.randint(0,70)
print (listlen)
boys = [listlen]
print (len(boys))