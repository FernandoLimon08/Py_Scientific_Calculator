import tkinter as tk

root=tk.Tk() #creates the aplication window
root.title("My calculator")
message=tk.Label(root,text="Hello World")	#Creates a label with the text "Hello World" for the window root
message.pack() #Shows the label in the app window
push_button=tk.Button(root,text="Boton", fg="blue", bg="red") #Creates a red button with the label "Boton" in a blue font
push_button.pack(expand=1) #Shows the button in the app window

root.mainloop() #makes the created window keeps open until its closed

app=tk.Tk() #creates a second window that apears after the root window is closed
target=tk.Label(app,text="Ya aprendi lo basico para crear apps") #Creates a label with a simple text
target.pack() #Shows the label in the app window
actions=tk.Button(app,text="Boton 2") #Creates a button with the label "boton 2"
actions.pack() #shows the button in the app window

app.mainloop() 
