from socket import *
import pickle
from .serverFacade import receive_corrected


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
    return_corrected(corrected)

def return_corrected(corrected_list):
    ServerFacade.receive_corrected(corrected_list)