from .sender import send_command


def send_to_server(to_be_corrected):
    Sender.send_command(to_be_corrected)

def receive_corrected(corrected):
    return corrected

