#import tkinter as tk
#def pecati_ime():
 #   text_od_entry = entry.get()
  #  print(text_od_entry)
#screen = tk.Tk()

#entry = tk.Entry()
#entry.grid(column=0, row=0,)
#entry1=tk.Entry()

#button = tk.Button(text="click", command=pecati_ime)
#button.grid(column=1, row=0)
#screen.mainloop()

import tkinter as tk

def pecati_ime():
    imePrezime_input = ime_prezime_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    print(imePrezime_input,email_input,password_input,)

screen = tk.Tk()
ime_prezime_label = tk.Label(screen, text="Full Name:")
email_label = tk.Label(screen, text="Email:")
password_label = tk.Label(screen, text="Password:")


ime_prezime_entry = tk.Entry()
email_entry = tk.Entry()
password_entry = tk.Entry()

ime_prezime_entry.grid(column=0,row=0)
email_entry.grid(column=0,row=1)
password_entry.grid(column=0,row=2)

button = tk.Button(text="Test",command=pecati_ime)
button.grid(column=0,row=3)
screen.mainloop()