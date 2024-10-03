class myClass:
    
    __privateVar = 27
        
    def __privaeMeth(self):
        print("I'm inside class myClass and PrivMeth method")
        
        
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)
        
        
foo = myClass()
foo.hello()
foo.__privaeMeth()