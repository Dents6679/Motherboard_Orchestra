import socket


print("Client started...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  These need to be changed into a local IP rather than the hostname for local testing

s.connect((socket.gethostname(), 6969))

full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        continue
    full_msg += msg.decode("utf-8")
    if msg[:6] == "@BREAK":
        print(msg[:-6:])
