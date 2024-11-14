import socket as so
import os

SRV_ADDR = "" #se vuoto utilizza tutte le interfacce, altrimenti quella di appartenenza ip
SRV_PORT = 4444

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("Sto attendendo una connessione...")
connection, address = s.accept()
print("Ho stabilto una connessione con:", address)
percorso_partenza = os.getcwd()
while True:
    prompt = percorso_partenza + "$"
    connection.sendall(prompt.encode("utf-8"))
    data = connection.recv(1024)
    if not data: break
    comando = data.decode("utf-8")
    result =""
    if(comando.startswith('cd')):
        result = "Mi dispiace non ancora disponibile"
    elif (comando.startswith('rm')):
        result = "Ci hai provato"
    else:
        result = "Non trovato"
    connection.sendall(result.encode("utf-8"))

    #connection.sendall(b"Ho ricevuto il messaggio! \n")
    print(data.decode('utf-8'))
connection.close()