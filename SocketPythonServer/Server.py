import socket, json

def server(host = 'localhost', port=8082):
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    i = 0
    list = []
    while True: 

        print ("Aguardando para receber mensagem do cliente")
        
        client, address = sock.accept() 
        
        data = client.recv(data_payload)
        String = ''
        if data:
            print(data.decode('utf-8'))
            if data.decode("UTF-8") == "lista":
                print("Bem vindo cliente")
                print(list[0])
                dados = ' - '.join(list)
                print(dados)   
                client.send(dados.encode('utf-8'))

            elif 'posicao-' in data.decode("UTF-8"):
                print("Você quer dar lance no produto tal" +data.decode('utf-8'))
            else:
                dados_dict = json.loads(data.decode('UTF-8'))
            
                print(dados_dict)
                
                print("Produto cadastrado com sucesso!")
                list.append(data.decode('UTF-8'))
                print ("Data: %s" %data.decode('UTF-8'))
                client.send(data)
                print ("Enviou: %s bytes back to %s" % (data, address))
                # end connection
                client.close()
                i+=1
                if i>=3: break

server()