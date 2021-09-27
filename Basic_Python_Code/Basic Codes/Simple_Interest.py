class SI:
    def get_data(self, P, T, R):
        self.P = P
        self.R = R
        self.T = T

    def cal_SI(self):
        SI = ((self.P * self.T * self.R)/100)
        return SI


s = SI()
P = float(input("Enter Principle amount : "))
T = float(input("Enter Duration :"))
R = float(input("Enter rate of interest : "))
s.get_data(P, T, R)

print("Simple Interest is : ", s.cal_SI())
