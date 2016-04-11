from .sender import send_command
import os

SERVER_IP = "162.246.157.118"

def send_to_server(to_be_corrected):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return Sender.send_command(to_be_corrected)
    else
        return None


