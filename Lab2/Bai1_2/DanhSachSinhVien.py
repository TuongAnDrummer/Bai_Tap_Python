import datetime
from SinhVien import SinhVien

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)
    
    def xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timSvTheoMssv(self, mssv:int):
        return [ str(sv) for sv in self.dssv if sv.maSo == str(mssv)]
    
    def timVTSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == str(mssv):
                return i
        return -1
    def xoaSvTheoMssv(self,maso:int) -> bool:
        vt = self.timVTSvTheoMssv(maso)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    def timSvTheoTen(self, ten: str):
        return [ str(sv) for sv in self.dssv if sv.hoTen == ten]
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [ str(sv) for sv in self.dssv if sv.ngaySinh < ngay]
    def sapXepTangTheoHoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen)
        dssv.xuat()
    def sapXepGiamTheoHoTen(self):
        self.dssv.sort(key=lambda x: x.hoTen, reverse=True)
        dssv.xuat()

    
def DocFile(file_name):
    dssv = DanhSachSv()
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            maso, hoten, ngaysinh = line.strip().split('*')
            student = SinhVien(maso, hoten, ngaysinh)
            dssv.themSinhVien(student)
    # Đóng file
    file.close()
    return dssv

dssv = DocFile("Bai1_2\DanhSach.txt")
dssv.xuat()