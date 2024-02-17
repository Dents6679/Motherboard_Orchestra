import socket
import PySimpleGUI as sg
import threading




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
        print(f"Current Clients:\n {[str(client) for client in clients]}")

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
        print("Waiting...")
        # Event loop
        event, values = window.read()


        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Submit':  # Allow server to send data to clients by setting flag to True
            send_client_data = True

        if event == 'Load Song':
            filepath = values["-IN-"]
            print(filepath)

        ## Server-Client loop.

        if send_client_data:  # Send data to all clients
            if not clients:  # If no clients are connected, do not send data
                print("No clients connected. Cannot send data.")
                send_client_data = False  # Reset flag to False
                continue

            print("Sending message to all clients...")
            for client in clients: # Send data to all clients.
                info = "Welcome to the server! With this server you'll be able to do something awesome.@BREAK"
                client.send(bytes(info, "utf-8"))
                client.close()

            clients = []  # Clear clients list after sending data
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
layout = [[sg.Text("Music input", expand_x=True, font=("Helvetica", 20))],
          [sg.Text("0 clients connected.", key='-CLIENTS-')],
          [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")], [sg.Button("Load Song"), sg.Button("Submit")]]

window = sg.Window('Server GUI', layout)

# Driver Code
start_server()

