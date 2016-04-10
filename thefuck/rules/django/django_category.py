def match(command):
    if 'manage.py' in command.script and 'migrate' in command.script:
        return True
    else:
        return False
