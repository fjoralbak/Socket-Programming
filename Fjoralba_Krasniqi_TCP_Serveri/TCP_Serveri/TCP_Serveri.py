import socket
from socket import *
from _thread import *
import datetime
import time
import random

serverName='localhost'
serverPort=14000
FORMAT="utf-8"


serverSocket=socket(AF_INET,SOCK_STREAM)
changePortName = input("Deshironi te vendosni manualisht portin apo emrin e serverit? ")
if(changePortName == 'p'  or changePortName == 'P'):
    port = input("Porti: ")
    if(int(port) > 0 and int(port) <= 65535):
        print("Porti eshte nderruar me sukses!")
        serverPort = int(port)
        changeServerName = input("Deshironi te vendosni emrin e serverit?")
        if(changeServerName == 'p' or changeServerName == 'P'):
            sName = input("Jepni emrin e serverit: ")
            serverName = sName
    else:
        print("Keni zgjedhur portin gabim!")


serverSocket.bind((serverName,serverPort))
print('Serveri eshte startuar ne '+ serverName +' ne portin ' + str(serverPort))
serverSocket.listen(5)
print('Server eshte duke punuar dhe eshte duke pritur per ndonje kerkese!')



def clientthread(clientS):

        try:
            mesazhi = clientS.recv(128)
            modifiedMessage = mesazhi.decode().split(" ")
        except:
            print("Klienti eshte çkyqur!")
            clientS.close()
            serverSocket.close()


        def IP():
            clientS.send(str("IP adresa juaj eshte: ").encode(FORMAT)+(gethostbyname(gethostname()).encode(FORMAT)))

        def NRPORTIT():
            clientS.send(str("Porti: ").encode(FORMAT)+ str(address[1]).encode(FORMAT))

        def KOHA():
            date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            clientS.send(("Data dhe koha e tanishme: ").encode(FORMAT)+ str(date).encode(FORMAT))

        def LOJA():
            loja = [random.randint(1,35) for i in range(5)]
            loja.sort()
            clientS.send(("5 numrat nga 1-35 jane: ").encode(FORMAT) + str(loja).encode(FORMAT))

        def NUMERO(teksti):
            nrZanoreve = 0
            nrBashtinglloreve = 0
            zanoret = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
            for i in teksti:
                if i in zanoret:
                    nrZanoreve+=1
                else:
                    nrBashtinglloreve+=1
            clientS.send(str("Numri i zanoreve ne tekstin qe keni shkruar eshte: ").encode(FORMAT)+str(nrZanoreve).encode(FORMAT)+str(" Numri i bashtonglloreve ne tekstin qe keni shkruar eshte: ").encode(FORMAT)+str(nrBashtinglloreve).encode(FORMAT))

        def ANASJELLTAS(teksti):
            reversed_string=""
            for i in teksti:
             reversed_string=i+reversed_string
            clientS.send(str("Reversed string: ").encode(FORMAT)+str(reversed_string).encode(FORMAT))

        def PALINDROM(teksti):
            reversedString=(teksti[::-1])
            if teksti==reversedString:
               clientS.send(str("Teksti eshte palindrom").encode(FORMAT))
            else:
                clientS.send(str("Teksti nuk eshte palindrom").encode(FORMAT))

        def PANGRAM(teksti):
            alphabet='abcdefghijklmnopqrstuvxyz'
            for char in alphabet:
                if char not in teksti.lower():
                    clientS.send(str("Teksti nuk eshte pangram").encode(FORMAT))
            clientS.send(str("Teksti  eshte pangram").encode(FORMAT))
       
        
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
            clientS.send(str(" A  eshte numri perfekt? ").encode(FORMAT)+str(isPerfect).encode(FORMAT) +str(" \nNumrat qift: ").encode(FORMAT)+str(even).encode(FORMAT) +str(" \nNumrat tek: ").encode(FORMAT)+str(odd).encode(FORMAT))
           

        def GCF(numri1 , numri2):
            try:
                num1=int(numri1)
                num2=int(numri2)
            except:
                clientS.send("Parametrat qe keni shtypur nuk jane numra!".encode(FORMAT))

            if num1 > num2:
                num1, num2= num2,num1
            for x in range(num1,0,-1):
                if num1 % x == 0 and num2 % x == 0:
                    clientS.send(str("The gratest factor beetwen two numbers: ").encode(FORMAT)+str(x).encode(FORMAT))
            

        def KONVERTO():
            try:
                parametri=float(param2)
            except:
                clientS.send("Parametri qe keni shtypur nuk eshte numer!".encode(FORMAT))

            if(param1=="CMNEINCH"):
                Inch = parametri/2.54
                clientS.send((str(parametri)+" Centimeters = "+ str(Inch)+" Inchs").encode(FORMAT))
            elif(param1=="INCHNECM"):
                cm = parametri*2.54
                clientS.send(str(parametri)+" Inches = "+ str(cm)+" Centimeters").encode(FORMAT)
            elif(param1=="KMNEMILE"):
                MILE = parametri/1.609
                clientS.send(str(parametri)+" Km = "+ str(MILE)+" Miles").encode(FORMAT)
            elif(param1=="MILENEKM"):
                KM = parametri*1.609
                clientS.send(str(parametri)+" Miles = "+ str(KM)+" Km").encode(FORMAT)
           
        
        functionsWithoutParameters = ["IP", "NRPORTIT","KOHA","LOJA","NUMERO","ANASJELLTAS","PALINDROM","GCF","KONVERTO","PANGRAM","NUMBERS"]
        functionsWithParameters = ["CMNEINCH","INCHNECM","KMNEMILE","MILENEKM"]

        if len(modifiedMessage) != 0:
            if(len(modifiedMessage) == 1):
                functionName = modifiedMessage[0]
                functionNameUpper = functionName.upper()
                if(functionNameUpper in functionsWithoutParameters): 
                    if (functionNameUpper == "IP"):
                        IP()
                    elif (functionNameUpper == "NRPORTIT"):
                        NRPORTIT()
                    elif (functionNameUpper == "KOHA"):
                        KOHA()
                    elif (functionNameUpper == "LOJA"):
                        LOJA() 
                    else:
                        clientS.send(("Paramterat e metodes jane gabim!").encode(FORMAT))
                else:
                    clientS.send(("Keni shenuar emrin e metodes gabim. Provoni prap!").encode(FORMAT))

            elif(len(modifiedMessage)==2):
               functionName = modifiedMessage[0]
               functionNameUpper=functionName.upper()
               teksti=modifiedMessage[1]
               if teksti != "":
                   if(functionName in functionsWithoutParameters): 
                        if(functionNameUpper=="NUMERO"):
                             NUMERO(teksti)
                        elif(functionNameUpper=="ANASJELLTAS"):
                             ANASJELLTAS(teksti)
                        elif (functionNameUpper=="PALINDROM"):
                             PALINDROM(teksti)
                        elif (functionNameUpper=="PANGRAM"):
                             PANGRAM(teksti)
                        elif (functionNameUpper == "NUMBERS"):
                            NUMBERS(teksti)
                   else:
                        clientS.send(("Keni shenuar emrin e metodes gabim, ose nuk keni shenuar parametrat perkates te metodes.").encode(FORMAT))
               else:
                    clientS.send("Ju lutemi shenoni parametrin e dyte!".encode(FORMAT))

            elif(len(modifiedMessage)==3):
                functionName=modifiedMessage[0]
                functionNameUpper=functionName.upper()
                param1=modifiedMessage[1]
                param2=modifiedMessage[2]

                if param2 != "" and param1 != "":
                    if(functionName in functionsWithoutParameters): 
                        if(functionNameUpper == "GCF"):
                            GCF(param1,param2)
                        elif(functionNameUpper == "KONVERTO"):
                            if(param1 in functionsWithParameters and param2 == ""):
                                clientS.send(("Ju duhet te shoni shkallet per konvertim!").encode(FORMAT))
                            elif(param1 in functionsWithParameters): 
                                if((param2>='a' and param2<='z') or (param2>='A' and param2<='Z')):
                                    clientS.send(("Per konvertim ju duhet te jepni numer e jo shkronje!").encode(FORMAT))
                                else:
                                    KONVERTO()
                            else:
                                clientS.send(("Keni shkruar gabim llojin per konvertim!").encode("ASCII"))
                        else:
                            clientS.send(("Keni shenuar emrin e metodes gabim, ose nuk keni shenuar parametrat perkates te metodes.").encode(FORMAT))
                else:
                        clientS.send("Ju lutemi shenoni parametrin e dyte ose te trete!".encode(FORMAT))
            else:
                clientS.send("Kontrolloni metoden per ndonje gabim eventual!".encode(FORMAT))
while True:
    clientS, address = serverSocket.accept()
    print('----------------------------------------')
    print("Serveri eshte i lidhur me: "+ gethostbyname(gethostname())+"   "+str(address[1]))
    start_new_thread(clientthread, (clientS,))
serverSocket.close()












