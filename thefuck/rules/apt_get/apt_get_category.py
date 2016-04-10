from thefuck.rules.apt_get.apt_get import get_package

def match(command):
    if ('not found' in command.stderr and get_package(command.script)) or ('apt' in command.script) or ('apt-get' in command.script) or ('apt-cache' in command.script):
        return True
    else:
        return False
