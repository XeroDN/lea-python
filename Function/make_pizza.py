import storing_the_functionInModule
storing_the_functionInModule.make_pizza(12,'peporni')
storing_the_functionInModule.make_pizza(16,'mushroom','cheese','pepper')

# You can also import a specific function from a module. Here’s the general syntax for this approach:
# from module_name import function_name

# You can import as many functions as you want from a module by separating each function’s name with a comma:
# from module_name import function_0, function_1, function_2

from storing_the_functionInModule import make_pizza
make_pizza(15,'tomato')
make_pizza(20, "wheat", 'flour')

# Using as to Give a Function an Alias
from storing_the_functionInModule import make_pizza as mp
mp(11, 'peporaniiiii')
mp(44, 'mushroom','goos','good')

#from module_name import function_name as fn


#Using as to Give a Module an Alias
import storing_the_functionInModule as sfm
sfm.make_pizza(10, 'peporani')
sfm.make_pizza(20, 'mushroom')
#syntax  import module_name as mn


#Importing All Functions in a Module
from storing_the_functionInModule import * #The asterisk in the import statement tells Python to copy every function from the module into this program file
make_pizza(22, 'peporani')