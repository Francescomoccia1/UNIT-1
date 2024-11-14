import http.client

host = input("Inserisci host/IP del sistema target: ")
port = input("Inserisci la porta del sistema target (default: 80)")
path = input("Inserisci il percorso (default'/'): ")
if(port == ""): port = 80
if(path == ""): path = '/'

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS','/')
    response = connection.getresponse()
    print("I metodi abilitati sono: ", response.getheaders())
    connection.close()
except ConnectionError:
    print("Connessione fallita", ConnectionError.strerror)