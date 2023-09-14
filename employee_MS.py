
class Employee:
    def __init__(self,name):
        self.name = str(name)
        self.wage = 0

    def calculatePayment(self):
        pass
   
class Temporary(Employee):
    def __init__(self,name,hourlywage,hour):
        self.name = str(name)
        self.hourlywage = hourlywage
        self.hour = hour
   
    def calculatePayment(self):
        wage= self.hourlywage * self.hour
        return wage
   
class FulltimeEmployee(Employee):
    def __init__(self, name, monthlywage):
        super().__init__(name)
        self.monthlywage = monthlywage
   
    def calculatePayment(self):
        return self.monthlywage

emilia_employee =  FulltimeEmployee ('Emilia',20.000)
serena_temporary= Temporary ('Serena',1500, 10)

print (emilia_employee.calculatePayment())
print (serena_temporary.calculatePayment())