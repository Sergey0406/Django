class TheCalc_1:
    def __init__(self):
        self.func5()

    def func1(self):
        return self.a + self.b

    def func2(self):
        return self.a - self.b

    def func3(self):
        return self.a * self.b

    def func4(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b

    def func5(self):
        self.a = int(input("a = "))
        self.b = int(input("b = "))

while True:
    x = input("+, -, *, /: ")
    print("Numbers:")
    Calc_1 = TheCalc_1()
    if x == 'n':
        break
    if x == "+":
        print(Calc_1.func1())
    if x == "-":
        print(Calc_1.func2())
    if x == "*":
        print(Calc_1.func3())
    if x == "/":
        print(Calc_1.func4())