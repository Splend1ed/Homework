import socket


address = ('127.0.0.1', 8000)
bite_chunk = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server_socket.bind(address)
server_socket.listen(1)


def cesar_coding(message: str, step: int):
    ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    for letter in message.upper():
        index = ru.find(letter)
        index_with_step = index + step
        if letter in ru:
            result += ru[index_with_step]
        else:
            client_socket.send('You must write only in Russian!'.encode('utf-8'))
    return result


while True:
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}')
    while True:
        data_from_client = client_socket.recv(bite_chunk).decode('utf-8')
        try:
            conv_to_tuple = eval(data_from_client)
            coding_data = cesar_coding(conv_to_tuple[0], int(conv_to_tuple[1]))
            client_socket.send(f'Coding data - {coding_data.title()}'.encode('utf-8'))
        except (TypeError, IndexError):
            client_socket.send('You must send tuple with message and step to coding in ru language:\n'
                               'Example: ("Амогус", 3)'.encode('utf-8'))
