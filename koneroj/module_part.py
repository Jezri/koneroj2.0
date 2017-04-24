from module_name import * 
class module_part(object):
	def __init__(self,name):
		self.name = module_name(name)
		self.desplay = ''
		self.concepts = []
		self.techniques = []
                self.theorems =[]
      
	def write_item(self, label):
		return (r'\begin{item}['+label+']'+ self.desplay + '\end{item}')
  
	def write_section(self):
		temp = ''   
		if self.desplay != '': 
			temp += r'\subsection*{' + self.name.desplay + r'}'
			temp +=  '\n' +self.desplay
			return temp
       
	def add_thoerem(self,thoerm):
		self.desplay += r'\footnotemark'
		self.thoerms += [dependency]
  
	def add_concept(self,concept):
		self.concepts += [concept]

	def add_technique(self,technique):
		self.desplay += r'\footnotemark'
		self.techniques += [technique]
          
