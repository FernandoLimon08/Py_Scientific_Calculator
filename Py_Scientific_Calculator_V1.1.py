from math import sqrt
import tkinter as tk

squares=tk.Tk()
squares.title("Scientific Calculator")
height=300
width=300
screen_width=int(squares.winfo_screenwidth())
screen_heigth=int(squares.winfo_screenheight())
centerx=int((screen_width-width)/2)
centery=int((screen_heigth-height)/2)
squares.geometry(f"{width}x{height}+{centerx}+{centery}")
geom=squares.geometry()
screen_number=tk.StringVar()
screen_value=tk.StringVar()
rows=list(range(0,6))
columns=list(range(0,4))
for row in rows:
	squares.grid_rowconfigure(row, weight=1)
for column in columns:
	squares.grid_columnconfigure(column, weight=1)

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

buttons=["one","two","three","four","five","six","seven","eight","nine","cero","dot","summ","rest","mult","div","square","clearAll"]
operator=["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","**2",""]
i=0
for number in buttons:
	exec(f"""
def print_{number}():
	#print(f"{operator[i]}")
	print(f"Se preciono el boton {number}")
	append_digit(f"{operator[i]}")
	""")
	i+=1

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
	print("Se preciono el boton Equal")
	expretion=screen_number.get()
	print(expretion)
	result=eval(expretion)
	screen_number.set(result)

screen=tk.Label(squares,textvariable=screen_number)
screen.grid(row=0,columnspan=4,sticky=tk.NSEW)

one=tk.Button(squares,text="1",command=print_one)
one.grid(row=4,column=0,sticky=tk.NSEW)

two=tk.Button(squares,text="2",command=print_two)
two.grid(row=4,column=1,sticky=tk.NSEW)

three=tk.Button(squares,text="3",command=print_three)
three.grid(row=4,column=2,sticky=tk.NSEW)

four=tk.Button(squares,text="4",command=print_four)
four.grid(row=3,column=0,sticky=tk.NSEW)

five=tk.Button(squares,text="5",command=print_five)
five.grid(row=3,column=1,sticky=tk.NSEW)

six=tk.Button(squares,text="6",command=print_six)
six.grid(row=3,column=2,sticky=tk.NSEW)

seven=tk.Button(squares,text="7",command=print_seven)
seven.grid(row=2,column=0,sticky=tk.NSEW)

eight=tk.Button(squares,text="8",command=print_eight)
eight.grid(row=2,column=1,sticky=tk.NSEW)

nine=tk.Button(squares,text="9",command=print_nine)
nine.grid(row=2,column=2,sticky=tk.NSEW)

cero=tk.Button(squares,text="0",command=print_cero)
cero.grid(row=5,column=0,sticky=tk.NSEW)

dot=tk.Button(squares,text=".",command=print_dot)
dot.grid(row=5,column=1,sticky=tk.NSEW)

equal=tk.Button(squares,text="=",command=print_equal)
equal.grid(row=5,column=2,columnspan=2,sticky=tk.NSEW)

summ=tk.Button(squares,text="+",command=print_summ)
summ.grid(row=4,column=3,sticky=tk.NSEW)

rest=tk.Button(squares,text="-",command=print_rest)
rest.grid(row=3,column=3,sticky=tk.NSEW)

mult=tk.Button(squares,text="x",command=print_mult)
mult.grid(row=2,column=3,sticky=tk.NSEW)

div=tk.Button(squares,text="/",command=print_div)
div.grid(row=1,column=3,sticky=tk.NSEW)

square=tk.Button(squares,text="^2",command=print_square)
square.grid(row=1,column=2,sticky=tk.NSEW)

clear_entry=tk.Button(squares,text="CE",command=print_clearEntry)
clear_entry.grid(row=1,column=0,sticky=tk.NSEW)

clear_all=tk.Button(squares,text="C",command=print_clearAll)
clear_all.grid(row=1,column=1,sticky=tk.NSEW)


squares.mainloop()
