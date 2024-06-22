# Destructors are called when an object gets destroyed. In Python, destructors are not needed
#  as much as in C++ because Python has a garbage collector that handles memory management 
#  automatically. 
# The _del_() method is a known as a destructor method in Python. 
# It is called when all references to the object have been deleted i.e when an object
#  is garbage collected.

#  def __del__(self):   destructor definition
#     Body

# Note : A reference to objects is also deleted when the object goes out of reference or when the program ends. 
# Example 1 : Here is the simple example of destructor. By using del keyword we deleted the all references of 
# object ‘obj’, therefore destructor invoked automatically.

# Python program to illustrate destructor
class Employee1:
    def __init__(self):
        print("Employee Created.")

    def __del__(self):
        print("Destructor called, Employee deleted.")

obj1 = Employee1()
del obj1 #Calling destructor

# Note : The destructor was called after the program ended or when all the references 
# to object are deleted i.e when the reference count becomes zero, not when object went 
# out of scope.
# Example 2: This example gives the explanation of above-mentioned note. Here, notice 
# that the destructor is called after the ‘Program End…’ printed.

# Python program to illustrate destructor
class Employee2:
    def __init__(self):
        print("Employee Created.")
    def __del__(self):
        print("Destructor called.")

def create_obj1():
    print("Making Object...")
    obj = Employee2()
    print("Function end...")
    return obj

print("Calling create_obj1 function")
obj = create_obj1()
print("Some imp statements")
print("program end...")

# Python program to illustrate destructor
class A:
    def __init__(self, bb):
        self.b = bb

class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")

def fun():
    b = B()

fun()