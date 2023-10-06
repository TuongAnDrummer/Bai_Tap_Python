import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import * 
from tkinter.ttk import *

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Checkbox Demo')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())

chonmonhoc = Label(root,text="Chọn môn học")
l1 = Checkbutton(root,
                text='A',
                # command=agreement_changed,
                variable=agreement,
                onvalue='A',
                offvalue='disagree')
l2 = Checkbutton(root,
                text='B',
                # command=agreement_changed,
                variable=agreement,
                onvalue='B',
                offvalue='disagree')

r1 = Checkbutton(root,
                text='C',
                # command=agreement_changed,
                variable=agreement,
                onvalue='C',
                offvalue='disagree')
r2 = Checkbutton(root,
                text='D',
                # command=agreement_changed,
                variable=agreement,
                onvalue='D',
                offvalue='disagree')
chonmonhoc.grid(row = 0, column = 0, sticky = W, pady = 2)
l1.grid(row = 0, column = 1, sticky = W, pady = 2)
l2.grid(row = 1, column = 1, sticky = W, pady = 2)
r1.grid(row = 0, column = 2, sticky = W, pady = 2)
r2.grid(row = 1, column = 2, sticky = W, pady = 2)
root.mainloop()


if self.value2.get() != "":
                    sheet.cell(row=current_row + 1, column=1).value = self.iD_field.get()
                    sheet.cell(row=current_row + 1, column=2).value = self.hoTen_field.get()
                    sheet.cell(row=current_row + 1, column=3).value = self.ngaySinh_field.get()
                    sheet.cell(row=current_row + 1, column=4).value = self.SDT_field.get()
                    sheet.cell(row=current_row + 1, column=5).value = self.email_field.get()
                    sheet.cell(row=current_row + 1, column=6).value = self.hocKy_field.get()
                    sheet.cell(row=current_row + 1, column=7).value = self.namHoc_field.get()
                    sheet.cell(row=current_row + 1, column=8).value = self.value2.get()
                if self.value3.get() != "":
                    sheet.cell(row=current_row + 1, column=1).value = self.iD_field.get()
                    sheet.cell(row=current_row + 1, column=2).value = self.hoTen_field.get()
                    sheet.cell(row=current_row + 1, column=3).value = self.ngaySinh_field.get()
                    sheet.cell(row=current_row + 1, column=4).value = self.SDT_field.get()
                    sheet.cell(row=current_row + 1, column=5).value = self.email_field.get()
                    sheet.cell(row=current_row + 1, column=6).value = self.hocKy_field.get()
                    sheet.cell(row=current_row + 1, column=7).value = self.namHoc_field.get()
                    sheet.cell(row=current_row + 1, column=8).value = self.value3.get()
                if self.value4.get() != "":
                    sheet.cell(row=current_row + 1, column=1).value = self.iD_field.get()
                    sheet.cell(row=current_row + 1, column=2).value = self.hoTen_field.get()
                    sheet.cell(row=current_row + 1, column=3).value = self.ngaySinh_field.get()
                    sheet.cell(row=current_row + 1, column=4).value = self.SDT_field.get()
                    sheet.cell(row=current_row + 1, column=5).value = self.email_field.get()
                    sheet.cell(row=current_row + 1, column=6).value = self.hocKy_field.get()
                    sheet.cell(row=current_row + 1, column=7).value = self.namHoc_field.get()
                    sheet.cell(row=current_row + 1, column=8).value = self.value4.get()    