def match(command):
    if 'cd' in command.script:
        return True
    else:
        return False
