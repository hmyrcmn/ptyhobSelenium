class Mat():
    def __init__(self, num1, num2):
        self.s1 = num1
        self.s2 = num2
        
    def add(self):
        return self.s1 + self.s2
    
    def sub(self):
        return self.s1 - self.s2


class Istatistik(Mat):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        
    def varyansCalculate(self):
        return Mat.add(self) ** Mat.sub(self)


varyans = Istatistik(5, 3)
print(varyans.varyansCalculate())
