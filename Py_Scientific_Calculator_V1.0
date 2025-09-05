import tkinter as tk

result_printed=False
squares=tk.Tk()
squares.title("Scientific Calculator")
height=130
width=50
screen_width=int(squares.winfo_screenwidth())
screen_heigth=int(squares.winfo_screenheight())
centerx=int((screen_width-width)/2)
centery=int((screen_heigth-height)/2)
squares.geometry(f"{width}x{height}+{centerx}+{centery}")
screen_number=tk.StringVar()
screen_value=tk.StringVar()

def reset():
	global result_printed
	if result_printed==True:
		screen_number.set("")
		result_printed=False
		return True

def append_digit(value):
	reset()
	screen_value=screen_number.get()
	screen_value+=value
	screen_number.set(screen_value)

def print_one():
	print("Se preciono el boton One")
	append_digit("1")

def print_two():
	print("Se preciono el boton Two")
	append_digit("2")

def print_three():
	print("Se preciono el boton Three")
	append_digit("3")

def print_four():
	print("Se preciono el boton Four")
	append_digit("4")

def print_five():
	print("Se preciono el boton Five")
	append_digit("5")

def print_six():
	print("Se preciono el boton Six")
	append_digit("6")

def print_seven():
	print("Se preciono el boton Seven")
	append_digit("7")

def print_eight():
	print("Se preciono el boton Eigth")
	append_digit("8")

def print_nine():
	print("Se preciono el boton Nine")
	append_digit("9")

def print_cero():
	print("Se preciono el boton Cero")
	append_digit("0")

def print_dot():
	print("Se preciono el boton Dot")
	append_digit(".")

def print_summ():
	print("Se preciono el boton Summ")
	append_digit("+")

def print_rest():
	print("Se preciono el boton Rest")
	append_digit("-")

def print_mult():
	print("Se preciono el boton Mult")
	append_digit("*")

def print_div():
	print("Se preciono el boton Div")
	append_digit("/")

def print_square():
	print("Se preciono el boton Square")
	append_digit("**2")

def print_clearAll():
	print("Se preciono el boton Clear All")
	screen_number.set("")

def print_clearEntry():
	empty=reset()
	print("Se preciono el boton Clear Entry")
	if empty!=True:
		screen_value=screen_number.get()
		if screen_value!="":
			screen_value=screen_number.get()
			screen_value=screen_value.removesuffix(screen_value[-1])
			screen_number.set(screen_value)

def print_equal():
	global result_printed
	operation=""
	print("Se preciono el boton Equal")
	expretion=screen_number.get()
	print(expretion)
	result=eval(expretion)
	screen_number.set(result)
	result_printed=True

screen=tk.Label(squares,textvariable=screen_number)
screen.grid(row=0,columnspan=4,ipadx=4)

one=tk.Button(squares,text="1",command=print_one)
one.grid(row=4,column=0,ipadx=4)

two=tk.Button(squares,text="2",command=print_two)
two.grid(row=4,column=1,ipadx=4)

three=tk.Button(squares,text="3",command=print_three)
three.grid(row=4,column=2,ipadx=4)

four=tk.Button(squares,text="4",command=print_four)
four.grid(row=3,column=0,ipadx=4)

five=tk.Button(squares,text="5",command=print_five)
five.grid(row=3,column=1,ipadx=4)

six=tk.Button(squares,text="6",command=print_six)
six.grid(row=3,column=2,ipadx=4)

seven=tk.Button(squares,text="7",command=print_seven)
seven.grid(row=2,column=0,ipadx=4)

eight=tk.Button(squares,text="8",command=print_eight)
eight.grid(row=2,column=1,ipadx=4)

nine=tk.Button(squares,text="9",command=print_nine)
nine.grid(row=2,column=2,ipadx=4)

cero=tk.Button(squares,text="0",command=print_cero)
cero.grid(row=5,column=0,ipadx=4)

dot=tk.Button(squares,text=".",command=print_dot)
dot.grid(row=5,column=1,ipadx=4)

equal=tk.Button(squares,text="=",command=print_equal)
equal.grid(row=5,column=2,columnspan=2,sticky=tk.EW,ipadx=4)

summ=tk.Button(squares,text="+",command=print_summ)
summ.grid(row=4,column=3,ipadx=4)

rest=tk.Button(squares,text="-",command=print_rest)
rest.grid(row=3,column=3,ipadx=4)

clear_all=tk.Button(squares,text="C",command=print_clearAll)
clear_all.grid(row=2,column=3,ipadx=4)


squares.mainloop()
