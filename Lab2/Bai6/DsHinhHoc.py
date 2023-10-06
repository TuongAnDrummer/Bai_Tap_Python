from HinhHoc import HinhHoc
from HinhTron import HinhTron
from HinhVuong import HinhVuong
from HinhChuNhat import HinhChuNhat

from enum import Enum
class LoaiHinh(Enum):
    TatCa = 1
    HinhTron = 2
    HinhVuong = 3
    HinhChuNhat = 4

    
    

class DsHinhHoc:
    def __init__(self,arr = None):
        if arr == None:
            self.dshh = []
        else:
            self.dshh = arr

    def themHinh(self,hh:HinhHoc):
        self.dshh.append(hh)

    def Xuat(self):
        for hh in self.dshh:
            print(hh)
            print(f"Dien Tich = {hh.TinhDienTich()}")

    def TinhTongDienTichCacHinh(self):
        sum = 0
        for hh in self.dshh:
            sum += hh.TinhDienTich()
        return sum
    
    def TimHinhCoDienTichLonNhat(self):
        max = self.dshh[0].TinhDienTich()
        for i in range(len(self.dshh)):
            if self.dshh[i].TinhDienTich() > max:
                max = self.dshh[i].TinhDienTich()
        return max   
    
    def TimHinhCoDienTichNhoNhat(self):
        min = self.dshh[0].TinhDienTich()
        for i in range(len(self.dshh)):
            if self.dshh[i].TinhDienTich() < min:
                min = self.dshh[i].TinhDienTich()
        return min     
    
    def TimHinhTronNhoNhat(self):
        arr = [i for i in self.dshh if isinstance(i,HinhTron)]
        min = arr[0].TinhDienTich()
        for i in range(len(arr)):
            if arr[i].TinhDienTich() < min:
                min = arr[i].TinhDienTich()
        return min
    
    def sapXepGiamTheoDienTich(self):
        self.dshh.sort(key=lambda x: x.TinhDienTich(), reverse=True)
        self.dshh.Xuat()

    # def DemSoLuongHinh(self,kieu: LoaiHinh) -> int:
    #     arr = [i for i in self.dshh if isinstance(i,kieu)]
    #     return len(arr)

    def tinhTongDienTichCacHinh(self):
        sum = 0
        for i in self.dshh:
            sum += i.TinhDienTich()
        return sum

         






