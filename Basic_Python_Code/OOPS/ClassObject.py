class Fact:
    fact = 1

    def fact(self, no):
        if no == 1:
            return self.fact
        else:
            while no > 1:
                self.fact = self.fact * no
                no = no - 1
            return self.fact


number = int(input("Enter number to find fact = "))
obj = Fact()

f = obj.fact(5)
print("factorial = ", f)
