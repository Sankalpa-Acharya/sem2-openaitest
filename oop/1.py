

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real,
                       self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real,
                       self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        return self * Complex(no.real, -no.imaginary) / float(no.mod())**2

    def mod(self):
        return Complex(pow(self.real**2 + self.imaginary**2, 0.5), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

c = Complex(2, 1)
d = Complex(5, 6)
print('Addition: ' + str(c + d))
print('Subtraction: ' + str(c - d))
print('Multiplication: ' + str(c * d))
print('Division: ' + str(c / d))