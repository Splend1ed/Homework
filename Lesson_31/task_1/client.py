import socket

address = ("127.0.0.1", 8003)
bite_chunk = 1024

file = open('client_test.txt', 'wb')


client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.sendto(input('Enter file name to search:').encode('utf-8'), address)
data_from_server, address = client_sock.recvfrom(bite_chunk)
with open('Result.txt', 'w+') as res:
    res.write(data_from_server.decode('utf-8'))


