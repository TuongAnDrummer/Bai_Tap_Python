class SinhVien:
    truong="Đại học Đà Lạt"
    import datetime
    def __init__(self,maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
    
    @property
    def hoTen(self):
        return self._hoTen
    @hoTen.setter
    def hoTen(self,hoTen:str):
        self._hoTen = hoTen
    
    @property
    def maSo(self):
        return self._maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self._maSo = maso
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    
    @property
    def ngaySinh(self):
        return self._ngaySinh
    
    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
