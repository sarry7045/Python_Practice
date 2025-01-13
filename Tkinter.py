# import tkinter
from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.mainloop()
window.title("My First GUI")
window.minsize(width=500, height=300)

# my_label = tkinter.Label(text = "I Am a Label", font=("Arial", 24, "bold"))
my_label = Label(text = "I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    print("Hello Button Click")
button = Button(text= "Click me", command=button_clicked)
button.pack() 
button.place(x=0, y=0) 
button.grid(column=1, row=2) 

input = Entry(width=10)
input.pack()
input.get()

canvas = Canvas(width=200, height=250)
my_image = PhotoImage(file="Wallpaper.jpg")
canvas.create_image(120, 120, image = "Wallpaper.jpg")
canvas.pack()