from socket import *
import pickle
from . import logs
from .receiver import receive_from_server


SERVER_IP = 162.246.157.118
SERVER_PORT = 9001

def send_command(to_be_corrected):
    client_socket = socket(AF_INT, SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    logs.debug("Sending command")
    client_socket.send(pickle.dumps(to_be_corrected))
    return Receiver.receive_from_server(client_socket)


