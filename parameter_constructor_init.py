class employee:
    empid = 0
    empname = ''
    empadress = ''
    empsalary = 0

    def __init__(self,empid,empname,empadress,empsalary):
        print("=====")
        self.empid = empid
        self.empname =empname
        self.empadress = empadress
        self.empsalary = empsalary
        
    
        
    def getdata(self):
        return str(self.empid) +";"+ self.empname + ";" + self.empadress + ";" + str(self.empsalary)

    def printdata(self):
        print(self.getdata())

emp1 =employee(111,'ahmed','cairo',5300)
emp1.printdata()        
     
emp2 =employee(333,'zinou','cairo',1900)
emp2.printdata()
