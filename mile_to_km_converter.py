from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)


label1 = Label(text="Miles")
label1.grid(column=2, row=0)
km = 0


def action():
    mile = float(entry.get())
    global km
    km = round(mile*1.61)
    label3["text"] = km


entry = Entry(width=15)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
button = Button(text="Calculate", command=action)
button.grid(column=1, row=2)


label2 = Label(text="is equal to")
label2.grid(column=0, row=1)


label3 = Label(text=f" {km} ")
label3.grid(column=1, row=1)

label4 = Label(text=" Km ")
label4.grid(column=2, row=1)


window.mainloop()
