from writable_concept import*
from definition import*
differentiate = writable_concept("Differentiate")
differentiate.parts["Definition"] = definition()
differentiate.parts["Definition"].desplay = r"""The differentiate of a function $f$ with repect a variable which it acts upon $x$ is defined as 
$$ \lim_{h\rightarrow0}\frac{f(x+h)-f(x)}{h}$$ and is written as $ f \prime$ \\
It may also be thought of as the instantanious rate of change of $f$ with respect to $x$"""
differentiate.write_module_doc() 
