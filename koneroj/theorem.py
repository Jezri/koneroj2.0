from result import *
from proof import *
from module import*
class theorem (module):
	def __init__(self, name):
                module.__init__(self,name)
                self.parts["Result"] = result () 
		self.parts["Proof"] = proof ()
