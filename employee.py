class employee:
    def _init__(self):
        self.firstname="Priyanshi "
        self.lastname="Chopra "
        self.salary=30000.00
    def get(self,fn,ln,sal):
        self.firstname=fn
        self.lastname=ln
        if(sal>0):
            self.salary=sal
        else:
            print("Invalid salary ")
            self.salary=input() 
    def show(self):
        print("First name ",self.firstname)
        print("last name ",self.lastname)
        print("salary ",self.salary)
emp=employee()
emp.show()
emp.get('xyz','abc',-30000)
emp.show()
        
        
