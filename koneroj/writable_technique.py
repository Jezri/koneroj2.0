from writable_module import*
from technique import*
class writable_technique(writable_module,technique):
    def __init__(self,name):
        writable_module.__init__(self,name)
        technique.__init__(self,name)
