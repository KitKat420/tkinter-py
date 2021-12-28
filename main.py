import tkinter

WIDTH, HEIGHT = 500, 300
FONT = ("Arial", 24, "normal")

window = tkinter.Tk()
window.title("GUI Program")

window.minsize(width=WIDTH, height=HEIGHT)

# Label


my_label = tkinter.Label(text="Label", font=FONT)

# Ways to modify attributes of classes
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=1, row=1)

# Entry

entry = tkinter.Entry(width=10)
entry.grid(column=4, row=4)
# Button


def button_clicked():
    my_label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_clicked)
button.place(x=250, y=150)
button.grid(column=2, row=2)

button = tkinter.Button(text="New Button")
button.grid(column=3, row=1)
# like a while loop, mainloop keeps the tkinter window displayed


window.mainloop()
