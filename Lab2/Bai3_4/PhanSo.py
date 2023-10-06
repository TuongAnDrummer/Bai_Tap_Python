import math
class PhanSo:
    def __init__(self, tu: int, mau: int) -> None:
        self.__tu = tu
        self.__mau = mau

    @property
    def tuSo(self):
        return self.__tu

    @property
    def mauSo(self):
        return self.__mau

    def rutGon(self):
        greatest_common_factor = math.gcd(self.__tu, self.__mau)
        self.__tu //= greatest_common_factor
        self.__mau //= greatest_common_factor
        return self

    def __add__(self, other):
        return PhanSo(self.__tu * other.__mau + other.__tu * self.__mau, self.__mau * other.__mau)

    def __sub__(self, other):
        return PhanSo(self.__tu * other.__mau - other.__tu * self.__mau, self.__mau * other.__mau)

    def __mul__(self, other):
        return PhanSo(self.__tu * other.__tu, self.__mau * other.__mau)

    def __truediv__(self, other):
        return PhanSo(self.__tu * other.__mau, self.__mau * other.__tu)

    # >
    def  __gt__(self,other):
        return (self.__tu * other.__mau) > (self.__mau * other.__tu)
        # return (self.__tu/self.__mau) > (other.__tu/other.__mau)
    # <
    def  __lt__(self,other):
        return (self.__tu * other.__mau) < (self.__mau * other.__tu)
        # return (self.__tu/self.__mau) < (other.__tu/other.__mau)
    # ==
    def __eq__(self, other):
        return (self.__tu * other.__mau) == (self.__mau * other.__tu)
        # return (self.__tu/self.__mau) == (other.__tu/other.__mau)
        
    def __repr__(self):
        return f"{self.tuSo}/{self.mauSo}"
# a = PhanSo(2, 3)
# b = PhanSo(3, 5)
# c = PhanSo(2,6)

# print(c.rutGon())

# print(f"{a} + {b} = {a + b}")
# print(f"{a} - {b} = {a - b}")
# print(f"{a} * {b} = {a * b}")
# print(f"{a} / {b} = {a / b}")

