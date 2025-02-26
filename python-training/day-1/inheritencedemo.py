
from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def deposit(self):
        pass
        
    def withdraw(self):
        print("withdraw")
    def checkBalance(self):
        print("checking Balance")



