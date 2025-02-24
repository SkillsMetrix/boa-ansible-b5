
from inheritencedemo import RBI

class SBI(RBI):
    def openFD(self):
        print("opening FD in SBI")
    def deposit(self):
        print("amount is deposited in SBI")


sbi= SBI()

sbi.deposit()
sbi.openFD()