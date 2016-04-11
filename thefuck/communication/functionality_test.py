from socket import *
import pickle
from .receiver import receive_from_server


SERVER_IP = localhost
SERVER_PORT = 9001
to_be_corrected = "This fucker is working"
def send_command(to_be_corrected):
    client_socket = socket(AF_INT, SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    client_socket.send(pickle.dumps(to_be_corrected))
    Receiver.receive_from_server(client_socket)


def receive_from_server(client_socket):
        # messageCount = 0
        # commandList = []

        # while True:
        #     if messageCount ==0:
        #         messageCount = clientSocket.recv(4)
        #   else:
        #       corrected = pickle.loads(clientSocket.recv(1024))
        #       commandList.append(corrected)
        #        if commandList.length == messageCount:
        #           returnCorrected(commandList)
        #           clientSocket.close()
        #           break

    corrected = pickle.loads(client_socket.recv(1024))
    client_socket.close()
    print (corrected)
    



