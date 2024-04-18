import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 8888)
server_socket.bind(server_address)

server_socket.listen(1)
client_socket, client_address = server_socket.accept()

print("客户端 {} 已经连接 .".format(client_address))

while True:
    # 接收客户端消息
    msg = client_socket.recv(1024)
    if not msg:
        break
    reply = "服务端响应信息：{}".format(msg.decode())
    print(reply)
    client_socket.sendall(reply.encode())
client_socket.close()
server_socket.close()