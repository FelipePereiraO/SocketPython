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
        # Send data 
        ProdutoNome = input("Digite o nome do Produto: ")
        ProdutoValor = input("Digite o valor inicial: ")
        print ("Nome %s" % ProdutoNome) 
        data = json.dumps({"nome": ProdutoNome, "valor": ProdutoValor})
        print ("Valor %s" % ProdutoNome) 

        print(data)
        sock.send(data.encode('utf-8'))

        
        # Look for the response 
        amount_received = 0 
        amount_expected = len(ProdutoNome) 
        while amount_received < amount_expected: 
            data = sock.recv(16) 
            amount_received += len(data) 
            print ("Recebida %s" % data) 
    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Encerrado!!") 
        sock.close() 

client()