
class Student():
    def __init__(self,rollno,name,subject,marks):
        self.rollno=rollno
        self.name=name
        self.subject=subject
        self.marks=marks

    def displayData(self):
        print(f"The name and subject is {self.name} {self.subject}")
    
    def __str__(self):
        return f"The name and subject is {self.name} {self.subject}"
    

sayna= Student("999","sanya","PHY","88")
atul= Student("997","atul","CHEM","89")

print(sayna)
print(atul.displayData())