from string import*
def name():
    return "Some name"
print name()
def code(name):
    temp = name()
    temp = temp.lower
    return  temp.replace(' ','_')
def desplay(name):
    return name()
print desplay(name)
def code_name():
    return code(name())
def desplay_name():
    return desplay(name)
print desplay_name()
