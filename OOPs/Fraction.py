class Fraction:
    def __init__(self,num=0,den=1):
        if den ==0:
            den = 1
        self.num = num
        self.den = den

    def printFraction(self):
        if self.num == 0:
            print(0)
        elif self.den ==1:
            print(self.num)
        else:
            print(self.num, '/', self.den)


    def simplify(self):
        if self.num ==0:
            self.den =1
            return
        current = min(self.num,self.den)
        while current >1:
            if self.num % current ==0 and self.den %current ==0:
                break
            current = current -1
        self.num = self.num //current
        self.den = self.den //current









f1 = Fraction(0,5)
f1.simplify()
f1.printFraction()
