from definition import *
from module import *
class concept(module):
	def __init__(self,name):
		super(concept,self).__init__(name)
		self.parts["Definition"] = definition()
