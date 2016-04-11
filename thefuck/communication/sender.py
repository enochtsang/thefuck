from socket import *
import pickle
from thefuck import logs
from . import receiver


SERVER_IP = "localhost"
SERVER_PORT = 3033

def send_command(to_be_corrected):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    logs.debug("Sending command")
    client_socket.send(pickle.dumps(to_be_corrected))
    return receiver.receive_from_server(client_socket)
