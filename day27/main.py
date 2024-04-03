from tkinter import *

window = Tk()
window.title("Mi to Km Converter")
window.minsize(250,100)
window.config(padx=20, pady=20)

def convert():
    km = round(float(mi.get()) * 1.60934, 2)
    value_label['text'] = km

# input box
mi = Entry(width=10)
mi.grid(column=1, row=0)

# mi label
mi_label = Label(text="Miles")
mi_label.grid(column=2, row=0)

# is equal to label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# converted value label
value_label = Label(text=0)
value_label.grid(column=1, row=1)

# km label
km_label = Label(text="Km")
km_label.grid(column=2,row=1)

# button
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

window.mainloop()
