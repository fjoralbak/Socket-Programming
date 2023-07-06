import socket
from socket import *

serverName="localhost"
serverPort=14000

sock=socket(AF_INET,SOCK_DGRAM)
print("Serveri eshte duke pritur kerkesen tuaj...")

while True:
    kerkesa=input("Shkruani emrin e metodes qe doni te provoni")
    if kerkesa== "":
        print("Ju lutem shkruani emrin e metodes ")
    else:
        sock.sendto(kerkesa.encode("utf-8"),(serverName,serverPort))
        ReturnedText = sock.recv(128).decode("UTF-8")
        print("\nRezultati sipas kerkeses suaj: "+ReturnedText)
        print("______________________________________________________________________________")
    