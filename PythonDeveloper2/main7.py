import tkinter as tk


def pecati_ime():
    imePrezime_input = ime_prezime_entry.get()
    email_input = email_entry.get()

    print(int(imePrezime_input) + int(email_input))


screen = tk.Tk()
ime_prezime_label = tk.Label(screen, text="Vnesi broj:")
email_label = tk.Label(screen, text="Vnesi broj:")
password_label = tk.Label(screen, text="Password:")

ime_prezime_entry = tk.Entry(screen)
email_entry = tk.Entry(screen)

ime_prezime_label.grid(column=0, row=0, padx=5, pady=5, sticky='e')
ime_prezime_entry.grid(column=1, row=0, padx=5, pady=5)

email_label.grid(column=0, row=1, padx=5, pady=5, sticky='e')
email_entry.grid(column=1, row=1, padx=5, pady=5)

button = tk.Button(text="Pecati", command=pecati_ime)
button.grid(column=1, row=3)
screen.mainloop()