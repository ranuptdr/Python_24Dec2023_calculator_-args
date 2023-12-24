# 1.  class defination 
class A():
    #1. prpperty
    #1. construsctor
    def __init__(self):
        print("Hello from A Constructor")
    #1.  method
    pass

class B(A):
    #1. prpperty
    #1. construsctor
    def __init__(self):
        #co.method
        super().__init__()
        print("Hello from B Constructor")
    #1. method
    pass

#2.  create a class object
#classobject = ClassName()
ceo = B()



#1. function defination is a one time process
def ranu(*args): # formal argument name can be anything
    print(args)
    pass
#2. function calling is a many time process 
ranu(1,2,3,4,5,6,7,8,9)
