import socket
hostName = socket.gethostname()
HostAddress = socket.gethostbyname(hostName);
print("My computername is: "+hostName," \n and my adress is "+HostAddress)

