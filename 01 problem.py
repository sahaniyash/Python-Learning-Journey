class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin= pin

p = Programmer("Yashkumar", 122000, 46977)
print(p.name, p.salary,p.pin,p.company)