from socket import *
from thefuck import logs
from ..thefucktypes import CorrectedCommand
from ..thefucktypes import Command
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

    corrected_strings = pickle.loads(client_socket.recv(1024))
    client_socket.close()
    
    if corrected_strings == None:
        yield None
    logs.debug("Received response from server")
    corrected_commands = []
    for packaged_command_string in corrected_strings:
        script = packaged_command_string[0]

        side_effect = packaged_command_string[1] 
        priority = packaged_command_string[2]
        if side_effect != None:
            side_effect = (Command(packaged_command_string[1], 
                                   packaged_command_string[2], 
                                   packaged_command_string[3]),
                           packaged_command_string[4])
            priority = packaged_command_string[5]
        
        logs.debug("script is " + str(script))
        logs.debug("side_effect is " + str(side_effect))
        logs.debug("priority is " + str(priority))

        yield CorrectedCommand(script, side_effect, priority)
