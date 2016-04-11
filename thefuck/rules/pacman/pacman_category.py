def match(command):
    if ('pacman' in command.script) or (')yaourt' in command.script) or ('not found' in command.stderr):
        return True
    else:
        return False
