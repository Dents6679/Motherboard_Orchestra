import socket
import PySimpleGUI as sg
import threading




# Function to handle client connections

def handle_clients(s, clients):
    global send_client_data
    while True:
        client_socket, address = s.accept()
        clients.append(client_socket)
        print(f"Connection from {address} has been established")
        print(clients)
        if send_client_data:
            for client in clients:
                info = "Welcome to the server."
                client.send(bytes(info, "utf-8"))
                client.close()

            print("Data sent to clients. Closing connections...")
            send_client_data = False

# Start server to establish connections. Retain connections and send data to clients.
def start_server():
    global send_client_data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 6969))
    s.listen(5)
    print("Server started...")
    clients = []

    # GUI setup
    layout = [[sg.Button('Send Message')]]
    window = sg.Window('Server GUI', layout)

    # Start a thread to handle client connections
    client_handler_thread = threading.Thread(target=handle_clients, args=(s, clients))
    client_handler_thread.start()

    while True:
        # Event loop
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        # Send message to all clients
        if event == 'Send Message':
            print(f"current data_toggle: {send_client_data}")
            send_client_data = True
            print("Sending message to all clients...")

    # Close server socket and GUI window
    print("Closing server...")
    s.close()
    window.close()

send_client_data = False
start_server()

