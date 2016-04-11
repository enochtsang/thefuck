from socket import *
import pickle
from thefuck import logs
from . import receiver

SERVER_IP = "162.246.157.118"
SERVER_PORT = 9001

def send_command(to_be_corrected):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    logs.debug("Sending command")
    script = to_be_corrected.script
    stdout = to_be_corrected.stdout
    stderr = to_be_corrected.stderr
    client_socket.send(pickle.dumps((script, stdout, stderr)))
    return receiver.receive_from_server(client_socket)
