from HinhChuNhat import HinhChuNhat
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        self.canh = canh


    def TinhDienTich(self):
        return self.canh**2

    def __str__(self) -> str:
        return (f"Hinh Vuong canh la: {self.canh}")
