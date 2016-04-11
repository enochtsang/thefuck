
def match(command):
    toks = command.script_parts
    if (toks[0].endswith('.py')) or ('python' in command.script):
        return True
    else:
        return False
