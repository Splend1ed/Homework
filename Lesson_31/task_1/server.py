import socket


address = ("127.0.0.1", 8003)
bite_chunk = 1024

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(address)
while True:
    data, address = server_sock.recvfrom(bite_chunk)
    try:
        with open(f'{data.decode("utf-8")}.txt', 'r') as file:
            data_in_file = file.readlines()
            str_conv = ''.join(data_in_file)
            server_sock.sendto(str_conv.encode('utf-8'), address)
    except FileNotFoundError(f'File with this name not found: {data}'):
        continue
