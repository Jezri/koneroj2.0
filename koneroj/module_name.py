from string import*
def name():
    return "Some name"
def code(name):
    return name().lower().replace(' ','_') 
def desplay(name):
    return name()
def code_name():
    return code(name)
def desplay_name():
    return desplay(name)
