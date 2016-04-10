def match(command):
    if 'rm' in command.script:
        return True
    else:
        return False
