class Employee:

    def __init__(self, numa, numb):
        self.num1 = numa
        self.num2 = numb
        

    def total(self):
        totals = self.num1 + self.num2
        if totals < 10:
            return "The total is : ", totals , " and it is less than 10"
        else:
            return self.num1 * self.num2

class Developer(Employee):
    def __init__(self, numa, numb, numc):
        super().__init__(numa,numb)
        self.num3 = numc

    def addTotal(self):
        return self.num1 * self.num3


numa = int(input("Enter the first Number: "))
numb = int(input("Enter the second Number: "))
numc = int(input("Enter the third Number for Developer: "))

empl = Employee(numa,numb)
empD = Developer(numa,numb,numc)

print( empl.total())
print( empD.addTotal())

