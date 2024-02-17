import socket


print("Client started...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  These need to be changed into a local IP rather than the hostname for local testing

s.connect((socket.gethostname(), 6969))

full_msg = ''
msg_len = 0
while True:

    msg = s.recv(8)

    # if len(msg) <= 0:

    if msg: # If there is data to be received
        msg_len += 1

    full_msg += msg.decode("utf-8")

    if full_msg[-6::] == "@BREAK":
        print(f"Message received from server in {msg_len} packets.")
        msg_len = 0 # Reset message length
        print(full_msg[:-6])
        full_msg = ''
        msg = ''
