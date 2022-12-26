class Sample():
    def __init__(self, num):
        self.num = num

    def multipier10x(self):
        return self.num*10


cal = Sample(num = 5)

print(cal.multipier10x())

#python myfile.py