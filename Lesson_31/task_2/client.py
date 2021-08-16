import socket


address = ('127.0.0.1', 8000)
bite_chunk = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(address)

while True:
    message_to_codding = (input('Enter message to codding: '), input('Enter step to offset: '))
    conv_to_str = str(message_to_codding)
    client_socket.send(conv_to_str.encode('utf-8'))
    data_from_server = client_socket.recv(bite_chunk).decode('utf-8')
    print(data_from_server)
