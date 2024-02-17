import socket
import PySimpleGUI as sg


# Start server to establish connections. Retain connections and send data to clients.
def start_server():

    send_client_data = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 6969))
    s.listen(5)
    print("Server started...")
    clients = []

    # GUI setup
    layout = [[sg.Button('Send Message')]]
    window = sg.Window('Server GUI', layout)

    while True:

        # Event loop
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        # Send message to all clients
        if event == 'Send Message':
            print("Sending message to all clients...")

        print("Got here.")
        client_socket, address = s.accept()
        clients.append(client_socket)
        print(f"Connection from {address} has been established")
        print(clients)
        if send_client_data:
            for client in clients:
                info = "Welcome to the serverAAAA."
                client.send(bytes(info, "utf-8"))
                client.close()
            send_client_data = False

    print("Got there...")
    window.close()





start_server()
