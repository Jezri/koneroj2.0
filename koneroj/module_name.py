from string import*
class module_name(object):
    def __init__(self, name):
         self.desplay = name
    def get_code(self):
        temp = self.desplay.lower()
        temp = temp.replace(' ','_')
        return temp
    code = property(get_code)

