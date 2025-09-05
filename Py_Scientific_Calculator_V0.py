import tkinter as tk

root=tk.Tk() #creates the aplication window
root.title("My calculator")
message=tk.Label(root,text="Hello World")	#Create a label with the text "Hello World" for the window root
message.pack() #Shoes the label in the app window
push_button=tk.Button(root,text="Boton", fg="blue", bg="red")
push_button.pack(expand=1)

root.mainloop() #makes the created window keeps open until its closed

app=tk.Tk()
target=tk.Label(app,text="Ya aprendi lo basico para crear apps")
target.pack()
actions=tk.Button(app,text="Bonon 2")
actions.pack()

app.mainloop()
