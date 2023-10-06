from HinhHoc import HinhHoc
class HinhChuNhat(HinhHoc):
    def __init__(self, canh, rong):
        super().__init__(canh)
        self.rong = rong

        if self.canh < self.rong:
            self.canh,self.rong = self.rong,self.canh

    def TinhDienTich(self):
        return self.canh * self.rong

    def __str__(self) -> str:
        return (f"Hinh Chu Nhat ChieuDai: {self.canh},ChieuRong: {self.rong}")
