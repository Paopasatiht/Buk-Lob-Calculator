#calculation.py

from tkinter import *
from tkinter import ttk
import sympy as sp
from tkinter import messagebox

#import tkinter.ttk as t

GUI = Tk()
GUI.title('โปรแกรมคำนวน Beam')
GUI.geometry('500x500')

############################

def math_addition():
	GUI2 = Toplevel()
	GUI2.title('หน้าต่างคณิตศาสตร์')
	GUI2.geometry('500x400')

	def Add():
		messagebox.showinfo('การบวก','ตัวอย่าง: 1 + 1 = 2')

	B = ttk.Button(GUI2,text='ตัวอย่างการบวกเลข',command=Add).pack(ipadx=20,ipady=10)

	GUI2.mainloop()



############################

menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit',command=GUI.quit)
menubar.add_cascade(label='File',menu=filemenu)

mathmenu = Menu(menubar, tearoff=0)
mathmenu.add_command(label='การบวก',command=math_addition)
mathmenu.add_command(label='การลบ')
mathmenu.add_command(label='การคูณ')
mathmenu.add_command(label='การหาร')
mathmenu.add_command(label='สูตร 1+2 เรื่อย ๆ ถึง n')

menubar.add_cascade(label='คณิตศาสตร์',menu=mathmenu)

###########Tab##############
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)

Tab.pack(fill=BOTH, expand=1)

Tab.add(T1,text='Beam')
Tab.add(T2,text='Number')
Tab.add(T3,text='Electicity')
###########Tab#################

#นี่คือรูปที่ใช้แสดงผล
image_beam = PhotoImage(file='beam.png')
image_board = PhotoImage(file='board.png')

logo = ttk.Label(T1,text='Beam',image=image_beam)
logo.pack()

logo2 = ttk.Label(T2,text='Column',image=image_board)
logo2.pack()

#############################

F1 = Frame(T1)
F1.pack()

F2 = Frame(T2)
F2.pack()

F3 = Frame(T3)
F3.pack()

#############################

value1 = StringVar()
value2 = StringVar()
value3 = StringVar()

FONT1 = ('Angsana New',15)

L = ttk.Label(F1,text='(1) ความกว้าง')
L.grid(row=0,column=0)
E1 = ttk.Entry(F1,textvariable=value1)
E1.grid(row=0,column=1,pady=10)

######

L = ttk.Label(F1,text='(2) ความสูง')
L.grid(row=1,column=0)
E2 = ttk.Entry(F1,textvariable=value2)
E2.grid(row=1,column=1,pady=10)

########

L = ttk.Label(F1,text='(3) ความยาว')
L.grid(row=2,column=0)
E3 = ttk.Entry(F1,textvariable=value3)
E3.grid(row=2,column=1,pady=10)


def Calc():
	v1 = float(value1.get()) #.get() ดึงค่ามา
	v2 = float(value2.get())
	v3 = float(value3.get())
	cal = v1 * v2 * v3
	textshow = 'คานคอนกรีตชิ้นนี้มีปริมาตร: {:,.2f} ลบ.ม.'.format(cal)
	v_result.set(textshow) # .set() สั่งให้เปลี่ยนข้อความเป็น textshow

B1 = ttk.Button(T1,text='Calculate',command=Calc)
B1.pack(pady=10,ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('----------Result----------')

Result = ttk.Label(T1,textvariable=v_result,foreground='green')
Result.pack()
##############################################################

value4 = StringVar()

L = ttk.Label(F2,text='1 + 2 +... จนถึง')
L.grid(row=0,column=0)
E4 = ttk.Entry(F2,textvariable=value4)
E4.grid(row=0,column=1,pady=10)

def Zigma():
	v4 = float(value4.get())
	cal = v4 * (v4+1)
	totalcal = cal / 2
	textshow = f'ค่ารวมตั้งแต่ 1 บวกไปเรื่อย ๆ จนถึง: {v4}  ก็คือ: {totalcal:,.2f}'
	v_result2.set(textshow)

B2 = ttk.Button(T2,text='Calculate',command=Zigma)
B2.pack(pady=10,ipadx=20,ipady=10)

v_result2 = StringVar()
v_result2.set('----------Result----------')

Result2 = ttk.Label(T2,textvariable=v_result2,foreground='green')
Result2.pack()
##########################################################


GUI.mainloop()
