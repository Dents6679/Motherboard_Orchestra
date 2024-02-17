import socket
import PySimpleGUI as sg
import threading

import encoder
from encoder import *




# Function to handle client connections

def handle_clients(s):
    global send_client_data
    global clients
    global window
    while True:
        client_socket, address = s.accept()
        clients.append(client_socket)
        window['-CLIENTS-'].update(str(len(clients)) + " clients connected.")
        print(f"Connection from {address} has been established")



# Start server to establish connections. Retain connections and send data to clients.
def start_server():
    global send_client_data
    global clients
    global layout
    global window
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 6969))
    s.listen(5)
    print("Server started...")



    # Start a thread to handle client connections
    client_handler_thread = threading.Thread(target=handle_clients, args=[s])
    client_handler_thread.start()


    while True:

        # Event loop
        event, values = window.read()


        if event == sg.WINDOW_CLOSED:
            break

        if event == '-SUBMIT-':  # Allow server to send data to clients by setting flag to True
            if len(clients) == 0:
                window["-OUTPUT-"].update("No clients connected. Cannot send data.")
                continue

            if max_overlapping_notes > len(clients):
                window["-OUTPUT-"].update(f"{max_overlapping_notes} clients are required for this song.")
                continue

            window["-OUTPUT-"].update(f"Sending data to clients...")
            send_client_data = True



        if event == 'Load Song':
            song_file_path = values["-IN-"]

            if song_file_path[-4::] != ".mid":
                window["-OUTPUT-"].update("Incorrect file type. Please select a .mid file.")
                continue

            max_overlapping_notes = find_max_overlapping_notes(song_file_path)
            window["-SUBMIT-"].update(disabled=False)
            window["-OUTPUT-"].update(f"{song_file_path.split('/')[-1]} has been loaded.")





        if event == '-SHOW-':
            print(f"Current Clients:\n {[str(client) for client in clients]}")



        # Server-Client loop.
        if send_client_data:  # Send data to all clients
            if not clients:  # If no clients are connected, do not send data
                print("No clients connected. Cannot send data.")
                send_client_data = False  # Reset flag to False
                continue

            print("Sending message to all clients...")
            for client in clients: # Send data to all clients.
                try:
                    info = "Welcome to the server! With this server you'll be able to do something awesome.@BREAK"
                    client.send(bytes(info, "utf-8"))
                except ConnectionResetError:
                    print("Client disconnected.")
                    clients.remove(client)
                    client.close()
                    window['-CLIENTS-'].update(str(len(clients)) + " clients connected.")
                    continue



            # clients = []  # Clear clients list after sending data
            send_client_data = False  # Reset flag to False after sending data

    # Close server socket and GUI window
    print("Closing server...")
    s.close()
    window.close()


# Flags
send_client_data = False

# Global variables
clients = []

# GUI layout
layout = [[sg.Text("Composer", expand_x=True, font=("Helvetica", 20))],
          [sg.Text("0 clients connected.", key='-CLIENTS-'), sg.Button("Refresh", key="-SHOW-")],
          [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],
          [sg.Button("Load Song"), sg.Button("Submit", key="-SUBMIT-", disabled=True)],
          [sg.Text("Please input a .mid file to play.", key="-OUTPUT-")],]

window = sg.Window('Composer', layout)

# Driver Code
start_server()










