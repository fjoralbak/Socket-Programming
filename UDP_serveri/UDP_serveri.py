import socket
from socket import *
import datetime
import random

serverName=""
serverPort=14000
FORMAT="utf-8"

sock=socket(AF_INET,SOCK_DGRAM)
sock.bind((serverName,serverPort))
print("Serveri eshte duke pritur per lidhje...")

while True:
    message, clientAddress=sock.recvfrom(128)
    mesazhi=message.decode("utf-8").split(" ")

    def IP():
        sock.sendto(gethostbyname(gethostname()).encode("utf-8"),clientAddress)

    def NRPORTIT():
            sock.sendto(str("Porti: ").encode(FORMAT)+ str(clientAddress[1]).encode(FORMAT),clientAddress)

    def KOHA():
            date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            sock.sendto(str("Data dhe koha e tanishme: ").encode(FORMAT)+ str(date).encode(FORMAT),clientAddress)

    def LOJA():
            loja = [random.randint(1,35) for i in range(5)]
            loja.sort()
            sock.sendto(str("5 numrat nga 1-35 jane: ").encode(FORMAT) + str(loja).encode(FORMAT),clientAddress)

    def NUMERO(teksti):
        nrZanoreve = 0
        nrBashtinglloreve = 0
        zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
        for i in teksti:
            if i in zanoret:
                nrZanoreve+=1
            else:
                nrBashtinglloreve+=1
        sock.sendto(str("Numri i zanoreve ne tekstin qe keni shkruar eshte: ").encode(FORMAT)+str(nrZanoreve).encode(FORMAT)+str(" Numri i bashtonglloreve ne tekstin qe keni shkruar eshte: ").encode(FORMAT)+str(nrBashtinglloreve).encode(FORMAT),clientAddress)
    
    def ANASJELLTAS(teksti):
        reversed_string=""
        for i in teksti:
            reversed_string=i+reversed_string
        sock.sendto(str("Reversed string: ").encode(FORMAT)+str(reversed_string).encode(FORMAT),clientAddress)

    def PALINDROM(teksti):
        reversedString=(teksti[::-1])
        if teksti==reversedString:
            sock.sendto(str("Teksti eshte palindrom").encode(FORMAT))
        else:
            sock.sendto(str("Teksti nuk eshte palindrom").encode(FORMAT),clientAddress)

    def PANGRAM(teksti):
            alphabet='abcdefghijklmnopqrstuvxyz'
            for char in alphabet:
                if char not in teksti.lower():
                    sock.sendto(str("Teksti nuk eshte pangram").encode(FORMAT),clientAddress)
            sock.sendto(str("Teksti  eshte pangram").encode(FORMAT),clientAddress)
       
        
    def NUMBERS(teksti):
        even = []
        odd=[]
        sum = 0
        for n in teksti:
            if int(n) % 2 == 0:
                even.append(n)
            if int(n) % 2 != 0:
                odd.append(n)
        for x in range(1, int(teksti)):
            if int(teksti) % x == 0:
                sum += x
        isPerfect = sum == int(teksti)
        
        sock.sendto(str(" A  eshte numri perfekt? ").encode(FORMAT)+str(isPerfect).encode(FORMAT) +str(" \nNumrat qift: ").encode(FORMAT)+str(even).encode(FORMAT) +str(" \nNumrat tek: ").encode(FORMAT)+str(odd).encode(FORMAT),clientAddress)
    
    def GCF(numri1 , numri2):
        try:
            num1=int(numri1)
            num2=int(numri2)
        except:
            sock.sendto("Parametrat qe keni shtypur nuk jane numra!".encode(FORMAT),clientAddress)

        if num1 > num2:
            num1, num2= num2,num1
        for x in range(num1,0,-1):
            if num1 % x == 0 and num2 % x == 0:
                sock.sendto(str("The gratest factor beetwen two numbers: ").encode(FORMAT)+str(x).encode(FORMAT),clientAddress)
                break

    def KONVERTO():
        try:
            parametri=float(par2)
        except:
            sock.sendto("Parametri qe keni shtypur nuk eshte numer!".encode(FORMAT),clientAddress)

        if(par1=="CMNEINCH"):
            Inch = parametri/2.54
            sock.sendto((str(parametri)+" Centimeters = "+ str(Inch) +" Inchs").encode(FORMAT),clientAddress)
        elif(par1=="INCHNECM"):
            cm = parametri*2.54
            sock.sendto((str(parametri)+" Inches = "+ str(cm)+" Centimeters").encode(FORMAT),clientAddress)
        elif(par1=="KMNEMILE"):
            MILE = parametri/1.609
            sock.sendto((str(parametri)+" Km = "+ str(MILE)+" Miles").encode(FORMAT),clientAddress)
        elif(par1=="MILENEKM"):
            KM = parametri*1.609
            sock.sendto((str(parametri)+" Miles = "+ str(KM)+" Km").encode(FORMAT),clientAddress)

    if(len(mesazhi)==1):
        funksioni=mesazhi[0]
        funksioni=funksioni.upper()
        if(funksioni=="IP"):
            IP()
        elif(funksioni=="NRPORTIT"):
            NRPORTIT()
        elif(funksioni=="KOHA"):
            KOHA()
        elif(funksioni=="LOJA"):
            LOJA()
        else:
            sock.sendto(( "Keni shenuar emrin e metodes gabim!").encode('utf-8'),clientAddress)
    elif(len(mesazhi)==2):
         funksioni=mesazhi[0]
         funksioni=funksioni.upper()
         teksti=mesazhi[1]
         if(funksioni=="NUMERO"):
            NUMERO(teksti)
         elif(funksioni=="ANASJELLTAS"):
            ANASJELLTAS(teksti)
         elif(funksioni=="PALINDROM"):
            PALINDROM(teksti)
         elif(funksioni=="PANGRAM"):
            PANGRAM(teksti)
         elif(funksioni=="NUMBERS"):
            NUMBERS(teksti)
         else:
            sock.sendto(( "Keni shenuar emrin e metodes gabim!").encode('utf-8'),clientAddress)
    elif(len(mesazhi)==3):
        funksioni=mesazhi[0]
        funksioni=funksioni.upper()
        par1=mesazhi[1]
        par2=mesazhi[2]
        if(funksioni=="KONVERTO"):
           KONVERTO()
        elif(funksioni=="GCF"):
           GCF(par1,par2)


    
