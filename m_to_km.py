from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=25, pady=25)

entry = Entry()
entry.grid(column=2, row=0)
entry.config(width=10)


miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)
miles_label.config()

result_label = Label(text="is equal to")
result_label.grid(column=0, row=2)
km_value_label = Label(text="0")
km_value_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)


def converter(km=1.609344):
    km_value_label.config(text=f"{round(int(entry.get()) * km)}")


convert_button = Button(text="Calculate", command=converter)
convert_button.grid(column=2, row=3)

window.mainloop()
