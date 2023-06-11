class FizzBizz :
    def Iz_negitive(self, number) :
        return "-" in str(number)
    
        
    def Iz_divisible_by_3(self, number):
        number -= 3
        try :
            5/number
        except ZeroDivisionError :
            return True
        try :
            5/int(not self.Iz_negitive(number))
        except ZeroDivisionError :
            return False
        return self.Iz_divisible_by_3(number)
    
    def IzFizz(self, n) :
        return self.Iz_divisible_by_3(n)

    def IzBuzz(self, n) :
        n = str(n)
        return (n[len(n)-1] == "5" or n[len(n)-1] == "0")
            
    def FizzBuzz(self, current_number) :
        current_number += 1
        print(self.IzFizz(current_number)*"Fizz" + self.IzBuzz(current_number)*"Buzz" or current_number)
        try :
            5/(current_number-self.max_number)
        except ZeroDivisionError :
            return
        self.FizzBuzz(current_number)
        
    def __init__(self, max_number) -> None:
        self.max_number = max_number
        self.FizzBuzz(0)

FizzBizz(100)
#or the easy way
#[print((n % 3 == 0)*"Fizz" + (n % 5 == 0)*"Buzz" or n) for n in range(0, 101)]
