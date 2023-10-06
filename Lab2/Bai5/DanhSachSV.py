from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien import SinhVien
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from datetime import datetime
class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    def themSV(self,sv: SinhVien):
        self.dssv.append(sv)

    def Xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def timVTSvTheoMssv(self, mssv:str):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1
    def timSvTheoLoai(self,loai:str):
        if loai == "chinhquy":
            return [sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy)]
        return [sv for sv in self.dssv if isinstance(sv,SinhVienPhiChinhQuy)]
    
    # 1. Tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def timSvCoDiemRL(self):
        kq = [sv for sv in self.dssv if isinstance(sv,SinhVienChinhQuy)]
        for i in kq:
            if i.diemRL >= 80:
                print(i)
    # 2. Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
    def timSvTheoTrinhDo(self):
        kq = [sv for sv in self.dssv if isinstance(sv,SinhVienPhiChinhQuy)]
        for i in kq:
            if i.trinhDo == "Cao đẳng" and i.ngaySinh < datetime.strptime("15/8/1999","%d/%m/%Y"):
                print(i)