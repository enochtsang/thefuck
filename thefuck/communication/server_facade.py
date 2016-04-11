from . import sender
from thefuck import logs
import os

SERVER_IP = "localhost"

def send_to_server(to_be_corrected):
    return sender.send_command(to_be_corrected)

