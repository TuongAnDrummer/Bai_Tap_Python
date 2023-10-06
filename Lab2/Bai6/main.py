from DsHinhHoc import DsHinhHoc
from HinhHoc import HinhHoc
from HinhTron import HinhTron
from HinhVuong import HinhVuong
from HinhChuNhat import HinhChuNhat

dshh = DsHinhHoc()
dshh.themHinh(HinhChuNhat(5,6))
dshh.themHinh(HinhChuNhat(4,8))
dshh.themHinh(HinhTron(6))
dshh.themHinh(HinhTron(3))
dshh.themHinh(HinhTron(5))
dshh.themHinh(HinhVuong(5))


dshh.Xuat()

#Dien Tich Lon Nhat
# print(f"Dien tich lon nhat : {dshh.TimHinhCoDienTichLonNhat()}")

#Dien Tich Nho Nhat
# print(f"Dien tich nho nhat : {dshh.TimHinhCoDienTichNhoNhat()}")

# Tìm hình tròn có diện tích nho nhất
# print(dshh.TimHinhTronNhoNhat())

# Sap Xep Giam Dan Theo DIen Tich
# print(dshh.sapXepGiamTheoDienTich())

# Tính tổng diện tích các hình
# print(f"Tong dien tich cac hinh : {dshh.TinhTongDienTichCacHinh()}")

#Dem so luong hinh
# print(f"Tong cac hinh  {dshh.DemSoLuongHinh(HinhTron)}")

#Tinh tong dien tich
# print(f"Tong dien tich cac hinh {dshh.tinhTongDienTichCacHinh()}")