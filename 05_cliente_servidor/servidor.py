import socket
ip = 'localhost'
porta = 8000
endereco = ((ip, porta))
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor_socket.bind(endereco)
servidor_socket.listen(1)
print('aguardando conexao...')
conexao, cliente = servidor_socket.accept()
print('conectado')
print('aguardando mensagem...')
while(True):
    
    mensagem_recebida = conexao.recv(1024).decode()
    
    
    print('cliente: ' + mensagem_recebida)

    mensagem = input('Digite aqui: ')
    if mensagem == 'sair':
        servidor_socket.close()
        break
    
    conexao.send(mensagem.encode())
    


