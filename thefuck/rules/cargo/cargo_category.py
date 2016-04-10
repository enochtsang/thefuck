def match(command):
    if 'cargo' in command.script:
        return True
    else:
        return False
