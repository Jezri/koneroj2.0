from writable_module import*
from theorem import*
class writable_theorem(writable_module,theorem):
    def __init__(self,name):
        writable_module.__init__(self,name)
        theorem.__init__(self,name)
