from socket import *
import pickle

class SexyObject:
    some_str = None

    def __init__(self, somestr):
        self.some_str = somestr

    def getstr(self):
        return self.some_str

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
    print(corrected.getstr())


SERVER_IP = 'localhost'
SERVER_PORT = 9002
to_be_corrected = SexyObject("This fucker is working")

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
client_socket.send(pickle.dumps(to_be_corrected),2)
receive_from_server(client_socket)






