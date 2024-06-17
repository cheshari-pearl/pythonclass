
class Account:
    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0


    def check_balance(self,pin):
        if pin == self.__pin:
           return self.__balance
        else:
            return "Wrong pin"
