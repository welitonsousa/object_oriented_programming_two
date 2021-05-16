import socket
ip = 'localhost'
porta = 8000
endereco = ((ip, porta))
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(endereco)
while(True):
    mensagem = input('Digite aqui: ')
    if mensagem == 'sair':
        cliente_socket.close()
        break

    cliente_socket.send(mensagem.encode())
    mensagem_servidor = cliente_socket.recv(1024).decode()
    
    print('servidor: ' + mensagem_servidor)

