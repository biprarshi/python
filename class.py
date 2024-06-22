class DemoClass:                               #camal case
    a=10
    def sumvalue(self):                        #argument object inside the class important(this)
        print(20+30)
        self.c=self.a*self.a
        print(self.c)
        
    def nameprint(se):  
        print("\nObject oriented programing")
        c=se.a*se.a
        print(c+1)
    
    def nameprintt(s):  
        print("\nObject oriented programing")
        s.c=s.a*s.a
        print(s.c+2)

    def __init__(sl ):                      # init keyword is used to define constructor
        print("\nWelcome to PYTHON OOPS Concept")

dmo=DemoClass()                             # variable(object) =Class name   #outside of the class
print(dmo.a)
dmo.sumvalue()
dmo.nameprint()
dmo.nameprintt()

dmo2=DemoClass() 
print(dmo2.a)
dmo2.sumvalue()
dmo2.nameprint()
dmo.nameprintt()