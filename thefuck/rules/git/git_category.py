def match(command):
    if 'git' in command.script:
        return True
    else:
        return False
