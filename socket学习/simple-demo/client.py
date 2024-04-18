import socket

server_address = ("127.0.0.1", 8888)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
    msg = input("请输入发送给服务端的消息(exit退出客户端):>>> ")
    if msg == "exit":
        break
    client_socket.sendall(msg.encode())
    # 接受服务端回复的消息
    reply = client_socket.recv(1024)
    print("收到服务端响应：{}".format(reply.decode()))
client_socket.close()