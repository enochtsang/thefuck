def match(command):
    if 'mvn' in command.script:
        return True
    else:
        return False
