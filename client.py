import socket
import PySimpleGUI as sg
import os

from twisted.internet.fdesc import fcntl

layout = [[sg.Text("Client", expand_x=True, font=("Helvetica", 20))],
          [sg.Text("Enter a server IP: "), sg.Input(key="IP_IN", default_text=socket.gethostname())],
          [sg.Button("Connect to Server", key="CONN"), [sg.Text("Status: Not connected to server.", key='CONN_STATUS')]]

          ]

window = sg.Window('Client', layout)


full_msg = ''
msg_len = 0

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "CONN":
        print("Connecting to server...")
        window["CONN_STATUS"].update("Status: Connecting to server...")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((values["IP_IN"], 6969))

            window["CONN_STATUS"].update("Status: Connected to server.")
            print("Connected to server.")

        except ConnectionRefusedError:
            window["CONN_STATUS"].update("Status: Connection refused. Try again.")
            print("Connection refused. Try again.")
            continue

        print("Got here.")
        # Blocking Issue is here
        msg = s.recv(8)

        if msg:  # If there is data to be received
            print(f"message: {msg}")
            msg_len += 1

        if full_msg[-6::] == "@BREAK":
            print(f"Message received from server in {msg_len} packets.")
            msg_len = 0  # Reset message length
            print(full_msg[:-6])
            full_msg = ''
            msg = ''



#
# print("Client started...")
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #  These need to be changed into a local IP rather than the hostname for local testing
#
# s.connect((socket.gethostname(), 6969))
#
# full_msg = ''
# msg_len = 0
# while True:
#
#     msg = s.recv(8)
#
#     # if len(msg) <= 0:
#
#     if msg: # If there is data to be received
#         msg_len += 1
#
#     full_msg += msg.decode("utf-8")
#
#     if full_msg[-6::] == "@BREAK":
#         print(f"Message received from server in {msg_len} packets.")
#         msg_len = 0 # Reset message length
#         print(full_msg[:-6])
#         full_msg = ''
#         msg = ''
