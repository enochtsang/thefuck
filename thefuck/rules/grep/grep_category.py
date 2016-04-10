def match(command):
    if 'grep' in command.script or 'egrep' in command.script:
        return True
    else:
        return False
