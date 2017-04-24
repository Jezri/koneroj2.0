from module_name import *
class module(object):
    def __init__(self,name):
        self.name = module_name(name) 
        self.parts = {}
        self.concepts = []
        self.theorems = []
        self.techniques = []
    def assemble(self):	
        for part in self.parts:
            self.concepts += self.parts[part].concepts
            self.theorems += self.parts[part].theorems
            self.techniques += self.parts[part].techniques
    def write_concepts(self):
        temp = """ """
        if self.concepts != []:
            temp +=r""" \subsection*{Concepts}
                        \begin{enumerate}"""
            for concept in self.concepts:
                temp+= concept.parts["Definition"].write_item()
            temp += """\end{enumerate}"""
        return temp
    def write_techniques(self):
        temp = """ """
        if self.techniques != []:
            temp +=r""" \subsection*{Techniques}
                        \begin{enumerate}"""
            for technique in self.techniques:
                temp+= technique.parts["Procedure"].write_item()
            temp += """\end{enumerate}"""
        return temp
    
    def write_theorems(self):
        temp = """ """
        if self.theorems != []:
            temp +=r""" \subsection*{Theorems}
                        \begin{enumerate}"""
            for theorem in self.theorem:
                temp+= thoerem.parts["Result"].write_item()
            temp += """\end{enumerate}"""
        return temp
      
    def write_module(self):
        temp = ''
        for part in self.parts:
            temp += r'\subsection*{'+ self.parts[part].name.desplay + r'}' + self.parts[part].desplay
        return temp
