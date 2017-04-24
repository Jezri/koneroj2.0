from module_part import*
from result import *
from proof import *
		

class proof(module_part):
    def __init__(self):
        module_part.__init__(self,"Proof")
	
class definition(module_part):
   def __init__(self):
        module_part.__init__(self,"Definition")

class provable_statment(module_part):
	def __init__(self,name = ''):
		module_part. __init__(self,name,)
		self.result = result()
		self.proof = proof()
		self.definition = definition()	
		self.lemmas = []
		
	def add_lemma(self, lemma):
		self.lemmas += [lemma] 		
	def assemble(self):
		self.dependencies = self.result.dependencies + self.proof.dependencies+self.definition.dependencies	
		self.concepts = self.result.concepts + self.proof.concepts+self.definition.concepts
	
	def get_preamble(self):
		temp = ''
		temp = 	r"\documentclass{article}" 		+ "\n"
		temp += r"\usepackage{fancyhdr}" 		+ "\n"
		temp += r"\usepackage{mathtools}" 		+ "\n"
		temp +=	r"\pagestyle{fancy}" 			+ "\n"
		temp += r"\everymath{\desplaystyle}"		+ "\n" 	
		temp += r"\begin{document}"			+ "\n"
		temp += r"\fancyhead[L]{" + self.name.desplay + r"}" + "\n"
		return temp
	
	preamble = property(get_preamble)	
	
	
	def write_dependencies_results (self):
		temp = ''
		if self.dependencies != []:
			temp += r'\subsection*{Dependencies}'+'\n'
			temp += '\t'+r'\begin{enumerate}'+'\n'
			for dependencies in self.dependencies:
				temp +='\t\t'+ dependencies.result.write_item() +'\n'
			temp +='\t'+r'\end{enumerate}'
		return temp
	
	def write_concepts (self):
		temp = ''
		if self.concepts != []:
			temp += r'\subsection*{Concepts}'
			temp += '\t'+r'\begin{enumerate}'+'\n'
			for concepts in self.concepts:
				temp +='\t\t'+r'\begin{item}'+ concepts +r'\end{item}'+r'\\'+'\n'
			temp +='\t'+r'\end{enumerate}'
		return temp

	def write_document(self):
		self.assemble()
		f = open( self.name.code + r'.tex',"w")
		f.write(self.preamble)
		f.write(self.result.write_section())
		f.write(self.proof.write_section())
		f.write(self.definition.write_section())
		f.write(self.write_dependencies_results())
		f.write(self.write_concepts())
		f.write(r'\end{document}')
		f.close

class concepts(module_part):
	pass
class algorithm(module_part):
	pass

