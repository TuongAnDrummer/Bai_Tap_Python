import math
from HinhHoc import HinhHoc
class HinhTron(HinhHoc):
    def __init__(self, bankinh) -> None:
        
        self.bankinh = bankinh
    
    def TinhDienTich(self):
        return math.pi * self.bankinh**2

    def __str__(self) -> str:
        return (f"Hinh tron Ban Kinh: {self.bankinh}")
