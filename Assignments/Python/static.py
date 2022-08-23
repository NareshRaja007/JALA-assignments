# Define a static variable and access that through a class.

class Python:
# Access through class    
 staticVariable = 10 
print(Python.staticVariable)

#Change within an class
Python.staticVariable = 15
print(Python.staticVariable) # Gives 15

#Access through an instance
instance = Python()
print(instance.staticVariable) # Gives 15

#Change within an instance
instance.staticVariable = 20
print(instance.staticVariable) # Gives 20
print(Python.staticVariable) #Gives 15