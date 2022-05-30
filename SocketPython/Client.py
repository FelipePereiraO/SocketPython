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
        TipoCliente = input("Digite o tipo de usuario que você quer entrar? \n Digite: \n 1 - Cliente\n 2 - Vendedor")

        if(TipoCliente == '2'):
               ProdutoNome = input("Digite o nome do Produto: ")
               ProdutoValor = input("Digite o valor inicial: ")
               print ("Nome %s" % ProdutoNome) 
               print ("Valor %s" % ProdutoNome) 
               data = json.dumps({"nome": ProdutoNome, "valor": ProdutoValor})
               sock.send(data.encode('utf-8'))
               
        sock.send(TipoCliente.encode('utf-8'))

        # Look for the response 
        amount_received = 0 
        amount_expected = len(TipoCliente) 

    except socket.error as e: 
        print ("Socket error: %s" %str(e)) 
    except Exception as e: 
        print ("Other exception: %s" %str(e)) 
    finally: 
        print ("Encerrado!!") 
        sock.close() 

client()