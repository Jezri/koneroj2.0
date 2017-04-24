from concept import*
from writable_module import*
class writable_concept(concept,writable_module):
    def __init__(self,name):
        writable_module.__init__(self,name)
        concept.__init__(self,name)

