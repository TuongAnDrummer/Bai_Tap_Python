from PhanSo import PhanSo
class DanhSachPhanSo:
    def __init__(self) -> None:
        self.dsps = []

#1. Đếm số phân số âm trong mảng
    def Is_Negative(self,ps) -> bool:
        if ps.tuSo < 0 or ps.mauSo < 0 :
            return True
        return False

    def Count_Negative(self,arr):
        count = 0
        for i in arr:
            if(self.Is_Negative(i)):
                count += 1
        return count
    
#2. Tìm phân số dương nhỏ nhất
    def Min_Fraction(self,arr):
        min_frac = arr[0]
        for i in range(1, len(arr)):
            if (self.Is_Negative(arr[i])==0):
                if arr[i]< min_frac:
                    min_frac = arr[i]
        return min_frac

#3. Tìm tất cả vị trí của phân số x trong mảng
    def Find_Position(self,arr,n):
        positions = []
        for i in range(len(arr)):
            if arr[i] == n:
                positions.append(i)
        return positions

#Tổng tất cả các phân số âm trong mảng
    def Sum_Negative_Frac(self,arr):
        sum = PhanSo(0,1)
        for i in arr:
            if self.Is_Negative(i):
                sum +=i
        return sum

# 5. Xóa phân số x trong mảng
    def Del_Frac(self,arr1,arr):
        kq = self.Find_Position(arr1,arr)
        for i in kq:
            del arr[i]
        return arr

# 6. Xóa tất cả phân số có tử là x
    def Del_Numerator(self,arr,n):
        for i in arr:
            if i.tuSo == n:
                del arr[i.tuSo]
        return arr
            
# 7. Sắp xếp phân số theo chiều tăng, giảm; tăng theo mẫu, tử, giảm theo mẫu tử.
    def SortUp(self,arr):
        arr.sort(key=lambda x: (x.tuSo)/(x.mauSo))
        return arr
    def SortDown(self,arr):
        arr.sort(key=lambda x: (x.tuSo)/(x.mauSo), reverse = True)
        return arr
#Tang theo tu mau
    def SortUp_Numerator(self,arr):
        arr.sort(key=lambda x: x.tuSo)
        return arr
    def SortUp_Denominator(self,arr):
        arr.sort(key=lambda x: x.mauSo)
        return arr
#Giam theo tu mau
    def SortDown_Numeratorr(self,arr):
        arr.sort(key=lambda x: x.tuSo, reverse = True)
        return arr
    def SortDown_Denominator(self,arr):
        arr.sort(key=lambda x: x.mauSo, reverse = True)
        return arr

#==========================================
arr_PhanSo = [PhanSo(1,2),PhanSo(-1,3),PhanSo(2,3),PhanSo(1,5),PhanSo(1,5),PhanSo(1,4),PhanSo(-1,2),PhanSo(1,8)]
dsps = DanhSachPhanSo()

print(dsps.Min_Fraction(arr_PhanSo))


