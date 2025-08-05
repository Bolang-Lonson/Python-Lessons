from sys import path

path.append('/Users/annie/Documents/Dev/Python-Lessons/PE2/Module 1/packages/extrapack.zip')

from extra.iota import funI
import extra.ugly.omega as om
import extra.good.best.sigma as sig
from extra.good.best.tau import funT
print(funI())
print(om.funO())
print(sig.funS())
print(funT())

import extra.good.beta as bet

print(bet.funB())