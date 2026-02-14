import Module
Module.name()

import Module
Module.nahid()

# change Module.py file and run this file again to see the changes.
import Module as Mod
Mod.name()


# use from keyword to import specific function from the module.
from Module import nahid
Module.nahid()

import Module
x = Module.person1
print(x)