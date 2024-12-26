import tkinter as tk
def pecati():
    a = entry1.get()
    znak = entry2.get()
    b = entry3.get()
    zadaca = a + " " + znak + " " + b
    presmetana_zadaca = eval(zadaca)
    label4.config(text=str(presmetana_zadaca))

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)


screen = tk.Tk()
screen.geometry("500x500")

label1 = tk.Label(text = "Prv broj: ")
label1.grid(row=0, column=0)
entry1 = tk.Entry()
entry1.grid(row=0, column=1)

label2=tk.Label(text = "Znak: ")
label2.grid(row=1, column=0)
entry2=tk.Entry()
entry2.grid(row=1, column=1)

label3=tk.Label(text = "Vtor broj: ")
label3.grid(row=2, column=0)
entry3=tk.Entry()
entry3.grid(row=2, column=1)


button1=tk.Button(text="Click", command = pecati)
button1.grid(row=3, column=0)
label4 = tk.Label(text="0")
label4.grid(row=3,column=1)


screen.mainloop()