def match(command):
    if 'brew' in command.script:
        return True
    else:
        return False
