from .sender import send_command
from . import logs
import os

SERVER_IP = "162.246.157.118"

def send_to_server(to_be_corrected):
    logs.debug("Pinging server")
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        logs.debug("Server alive")
        return Sender.send_command(to_be_corrected)
    else
        logs.debug("No response from server")
        return None


