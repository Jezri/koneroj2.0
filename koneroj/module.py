from module_name import *
from example import *
from explanation import *
from question import *
class module(object):
    def __init__(self,name):
        self.name = module_name(name) 
        self.parts = {}
        self.extras ={"Examples" : {} , "Explanations" : {}, "Questions": {}}
        self.concepts = []
        self.theorems = []
        self.techniques = []
    def __enter__(self):
        return self
    def __exit__(self, type, value ,traceback):
	pass
    def assemble(self): 
        for part in self.parts:
            self.concepts += self.parts[part].concepts
            self.theorems += self.parts[part].theorems
            self.techniques += self.parts[part].techniques
    def write_concepts(self):
        temp = """ """
        if self.concepts != []:
            temp +=r""" \section*{Concepts}"""
            for concept in self.concepts:
                                temp+= r""" 
\subsection*{""" 
                                temp += concept.name.desplay + r"""}
\subsubsection*{""" 
                                temp+=concept.parts["Definition"].name.desplay + """}"""+concept.parts["Definition"].desplay
        return temp
    def write_techniques(self):
        temp = """ """
        if self.techniques != []:
            temp +=r""" \section*{Techniques}"""
            for technique in self.techniques:
                                temp+= r""" 
    \subsection*{""" 
                                temp += technique.name.desplay + r"""}
\subsubsection*{""" 
                                temp+=technique.parts["Procedure"].name.desplay + """}"""+technique.parts["Procedure"].desplay
                                
        return temp
    def write_theorems(self):
        temp = """ """
        if self.theorems != []:
            temp +=r""" \subsection*{Theorems}
                        \begin{enumerate}"""
            for theorem in self.theorem:
                temp+= thoerem.parts["Result"].write_item(self.name.desplay)
            temp += """\end{enumerate}"""
        return temp
      
    def write_module(self):
        temp = ''
        for part in self.parts:
            temp += r'\section*{'+ self.parts[part].name.desplay + r'}' + self.parts[part].desplay
        return temp

    def write_extras(self):
        temp = ''
        for catagory in self.extras:
            if self.extras[catagory] !={}:
                temp+= r'\section*{'+catagory+ r'}'
                for extra in self.extras[catagory]:
		    temp += r'\subsection*{'+self.extras[catagory][extra].name.desplay + r'}' + self.extras[catagory][extra].desplay
        return temp
