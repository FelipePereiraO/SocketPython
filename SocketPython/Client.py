from math import prod
import socket, json

from Produto import Produto


def client(host = 'localhost', port=8082): 
    # Create a TCP/IP socket 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
    server_address = (host, port) 
    print ("Conectando %s a porta %s" % server_address) 
    sock.connect(server_address) 
    # Send data 
    try: 
        info = True
        while info:
            user = input("Digite \n lista - Para ver lista de produtos \n sair - Para Sair")
            # Send data 
            if user == "lista":
                sock.send(user.encode('utf-8'))
                info = False
            elif user == "sair":
                exit()
            else:
                info = True
        # Look for the response 
        data = sock.recv(2000)
        lista = data.decode('UTF-8').split('-')
        print ("Recebida %s" % data.decode('UTF-8')) 
        count = 0
        for item in lista:
            count += 1
            print(count,' - ', item)
        produto = input("Digite a posição do produto que queira da um lance: ")
        ps = "posicao- "+produto
        sock.send(ps.encode('utf-8'))

        amount_received = 0 
        amount_expected = len(user) 
        while amount_received < amount_expected: 
            
            amount_received += len(data) 
            print ("Recebida %s" % data.decode('UTF-8')) 

    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Encerrado!!") 
        sock.close() 

client()