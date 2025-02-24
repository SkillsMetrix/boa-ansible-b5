
from inheritencedemo import RBI

class ICICI(RBI):
     def deposit(self):
        print("amount is deposited in ICICI")


icici= ICICI()
icici.deposit()