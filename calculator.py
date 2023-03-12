from tkinter import *
expression = ""
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
def equal():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""

	except:
		equation.set(" error ")
		expression = ""

def allclear():
	global expression
	expression = ""
	equation.set("")
	
def backspace():
   global expression
   expression = expression[:-1]
   equation.set(expression)

if __name__ == "__main__":
	master = Tk()
	master.configure(background="black")
	master.title("Simple Calculator")
	master.geometry("270x180")
	equation = StringVar()
	expression_field = Entry(master, textvariable=equation,font=('Roboto',12))
	expression_field.grid(columnspan=4, ipadx=38,padx=5,pady=5)
	button7 = Button(master, text='7', fg='white', bg='gray',command=lambda: press(7), height=1, width=7)
	button7.grid(row=2, column=0)

	button8 = Button(master, text='8', fg='white', bg='gray',command=lambda: press(8), height=1, width=7,font=('Roboto',10))
	button8.grid(row=2, column=1)

	button9 = Button(master, text='9', fg='white', bg='gray',command=lambda: press(9), height=1, width=7)
	button9.grid(row=2, column=2)

	button4 = Button(master, text='4', fg='white', bg='gray',command=lambda: press(4), height=1, width=7)
	button4.grid(row=3, column=0)

	button5 = Button(master, text='5', fg='white', bg='gray',command=lambda: press(5), height=1, width=7)
	button5.grid(row=3, column=1)

	button6 = Button(master, text='6', fg='white', bg='gray',command=lambda: press(6), height=1, width=7)
	button6.grid(row=3, column=2)

	button1 = Button(master, text='1', fg='white', bg='gray',command=lambda: press(1), height=1, width=7)
	button1.grid(row=4, column=0)

	button2 = Button(master, text='2', fg='white', bg='gray',command=lambda: press(2), height=1, width=7)
	button2.grid(row=4, column=1)

	button3 = Button(master, text='3', fg='white', bg='gray',command=lambda: press(3), height=1, width=7)
	button3.grid(row=4, column=2)

	button0 = Button(master, text='0', fg='white', bg='gray',command=lambda: press(0), height=1, width=7)
	button0.grid(row=5, column=0)

	plus = Button(master, text='+', fg='black', bg='orange',command=lambda: press("+"), height=1, width=7)
	plus.grid(row=2, column=3)

	minus = Button(master, text='-', fg='black', bg='orange',command=lambda: press("-"), height=1, width=7)
	minus.grid(row=3, column=3)

	multiply = Button(master, text='*', fg='black', bg='orange',command=lambda: press("*"), height=1, width=7)
	multiply.grid(row=4, column=3)

	divide = Button(master, text='/', fg='black', bg='orange',command=lambda: press("/"), height=1, width=7)
	divide.grid(row=5, column=3)

	equal = Button(master, text='=', fg='black', bg='white',command=equal, height=1, width=7)
	equal.grid(row=5, column=2)

	clear = Button(master, text='C', fg='black', bg='red',command=backspace, height=1, width=7)
	clear.grid(row=6, column=1)
	allclear = Button(master,text="AC",fg='black',bg='red',command=allclear, height=1,width=7)
	allclear.grid(row=6,column=0)
	Decimal= Button(master, text='.', fg='white', bg='gray',command=lambda: press('.'), height=1, width=7)
	Decimal.grid(row=5, column=1)
	master.mainloop()
	
