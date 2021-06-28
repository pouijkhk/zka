import tkinter
from tkinter import *
wndo = Tk()
wndo.geometry("600x600")
wndo.config(bg="#3637F5")
entrey = Entry(wndo, text="", font=("Arial", 25))
entrey.pack()
lk = StringVar()
lk2 = StringVar()
def ca():
	try:
		io = int(entrey.get())
		man = io * 2.25 / 100
		ler = io - man
		lk.set(man)
		lk2.set(ler)
	except ValueError:
		lk.set("أدخل قيمة صحيحة")
		lk2.set("أدخل قيمة صحيحة")

b1 = Button(wndo, text="أحسب قيمة الزكاة", font=("Arial", 25), command=ca)
b1.pack()

lo = Label(wndo, textvariable=lk, font=("Arial", 25), bg="#C4FFD2")
lo.pack()

lo2 = Label(wndo, textvariable=lk2, font=("Arial", 25), bg="#C4FFD2")
lo2.pack()

wndo.mainloop()