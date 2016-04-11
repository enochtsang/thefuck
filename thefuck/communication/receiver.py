from socket import *
from thefuck import logs
import pickle


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
    logs.debug("Received response from server")
    client_socket.close()
    return corrected
