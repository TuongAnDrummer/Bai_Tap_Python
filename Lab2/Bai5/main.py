from sinh_vien_chinh_quy import SinhVienChinhQuy
from sinh_vien import SinhVien
from sv_phi_chinh_quy import SinhVienPhiChinhQuy
from datetime import datetime
from DanhSachSV import DanhSachSV

sv1 = SinhVienChinhQuy(1610195,"Nguyễn Đức Duy Ân",datetime.strptime("24/02/1998","%d/%m/%Y"),80)
sv2 = SinhVienChinhQuy(1610194,"Lê Thùy Lan Chi",datetime.strptime("02/03/1998","%d/%m/%Y"),90)
sv3 = SinhVienPhiChinhQuy(1510451,"Nguyễn Xuân Thắng",datetime.strptime("15/12/2000","%d/%m/%Y"),"Cao đẳng",2)
sv4 = SinhVienPhiChinhQuy(1610166,"Võ Thị Thu Ngân",datetime.strptime("03/12/1998","%d/%m/%Y"),"Cao đẳng",2)
sv5 = SinhVienPhiChinhQuy(1610089,"Nguyễn Thị Thùy Linh",datetime.strptime("03/03/1998","%d/%m/%Y"),"Trung Cấp",2.5)
sv6 = SinhVienChinhQuy(1610167,"Nguyễn Quốc Anh",datetime.strptime("08/10/1998","%d/%m/%Y"),60)
sv7 = SinhVienPhiChinhQuy(1610288,"Lê Nhật  Ánh",datetime.strptime("10/07/1998","%d/%m/%Y"),"Trung Cấp",2.5)
sv8 = SinhVienChinhQuy(1610290,"Trần Thị Thùy Trang",datetime.strptime("08/10/1998","%d/%m/%Y"),70)

dssv = DanhSachSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

# dssv.Xuat()

# vt = dssv.timVTSvTheoMssv(1610166)
# print(f"Sinh vien o vi tri thu {vt+1}")

# kq = dssv.timSvTheoLoai("chinhquy")
# print("danh sach sinh vien theo loai:")
# for sv in kq:
#     print(sv)

##1 Tìm sinh viên có điểm rèn luyện từ 80 trở lên
# kq1 = dssv.timSvCoDiemRL()
##2 Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
# kq1 = dssv.timSvTheoTrinhDo()