import socket

SERVER="localhost"
PORT=14000
FORMAT="utf-8"

clinetPortManually = input("Deshironi te jepni portin manualisht? ")
if clinetPortManually == 'P' or clinetPortManually == 'p':
    port = input("Porti: ")
    if(int(port) > 0 and int(port) <= 65535):
        print("Porti eshte nderruar me sukses!")
        PORT = int(port)
        changeServerName = input("Deshironi te vendosni emrin e serverit?")
        if(changeServerName == 'p' or changeServerName == 'P'):
            sName = input("Jepni emrin e serverit: ")
            SERVER = sName
    else:
        print("Keni zgjedhur portin gabim!")


    print("Metodat kryesore jane: ")
    print("")
    print("IP-Kthen IP adresen tuaj...")
    print("NRPORTIT-Kthen Portin tuaj...")
    print("NUMERO-Kthen numrin e zanoreve dhe bashtinglloreve ne fjaline qe ju e shkruani...")
    print("ANASJELLTAS-Kthen reverse textin...")
    print("PALINDROM-Kthen teksti qe keni shkruar eshte palindrim...")
    print("KOHA-Kthen kohen aktuale...")
    print("LOJA-Kthen 5 numra random nga 1-35...")
    print("GCF-Gjënë faktorin më te madh te përbashkët në mes dy numra...")
    print("KONVERTO- konverton: \n\t\t\tCMNEINCH\n\t\t\tINCHNECM\n\t\t\tKMNEMILES\n\t\t\tMILESNEKM")
    print("")
    print("Ndersa metodat shtese jane: ")
    print("")
    print("PANGRAM- Kthen nese teksti permban te gjitha shkronjat e alfabetit anglez")
    print("NUMBERS- kthen nese nje numer eshte perfekt a jo, dhe nga ai numer ndan nunmrat qift dhe tek...")
    print("")



x='P'
while x=='P':
    clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        clientSocket.connect((SERVER,PORT))
        mesazhi=input("Try a method: ")
        clientSocket.send(mesazhi.upper().encode(FORMAT))
    except:
        print("The server is disconnected!")
        clientSocket.close()
        break

    if(mesazhi==""):
        print("You should try a method")
    else:
        try:
         mesazhiImodifikuar=clientSocket.recv(128)
         print(mesazhiImodifikuar.decode(FORMAT))
         print("------------------------------------------------------")
         print("")
         mesazhi=input("\nPress P if you want to try another method, or J if you want to disconnect: ")
         mesazhi=mesazhi.upper()
         if(mesazhi!="P"):
           print("We hope you come back again\n")
           x='J'
         else:
           x=mesazhi
        except: 
         print("Serveri eshte çkyçur!")
         

   
    










