def match(command):
    if 'tsuru' in command.script:
        return True
    else:
        return False
