import tkinter as tk
import random
from tkinter import PhotoImage
from tkinter import messagebox

#-----------------------generate password----------------#
def generate_password():
    a = ['a', 'b', 'c', 'd', 'e']
    b = ['1', '2', '3', '4', '5']
    c = ['/', '@', '.', ',', '$']
    lists = a + b + c
    random.shuffle(lists)
    password = ''.join(lists[:8])
    return password

def generate_password_2():
    generated_password = generate_password()
    entry3.delete(0, tk.END)
    entry3.insert(0, generated_password)


def find():
    website = entry1.get()
    found = False

    if website:
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    stored_website, stored_email, stored_password = line.strip().split(" | ")
                    if stored_website.lower() == website.lower():
                        messagebox.showinfo("Najdeno", f"Website: {stored_website}\nEmail: {stored_email}\nPassword: {stored_password}")
                        found = True
                        break
            if not found:
                messagebox.showinfo("Ne e pronajdeno ", f"Nema detali za '{website}'")
        except FileNotFoundError:
            messagebox.showwarning("Filot ne e pronajden", "Data filot ne pronajden.")
    else:
        messagebox.showwarning("Input error", "Vnesi go imeto na websitot")




#----------------------save entries------------------#

def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    if website and email and password:
        with open('data.txt', 'a') as file:
            file.write(f"{website} | {email} | {password}\n")

        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
    else:
        tk.messagebox.showwarning("Input error","Please fill in all fields.")




#------------------------------------UI------------------------------------------#
screen = tk.Tk()
canvas = tk.Canvas(width=200, height=200,background='white')
main_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=main_image)
canvas.grid(column=2, row=0)


screen.geometry("500x500")

label1 = tk.Label(text = "Website: ")
label1.grid(row=1, column=0)
entry1 = tk.Entry(width=35)
entry1.grid(row=1, column=2)

label2=tk.Label(text = "Email/Username: ")
label2.grid(row=2, column=0)
entry2=tk.Entry(width=35)
entry2.grid(row=2, column=2)

label3=tk.Label(text = "Password: ")
label3.grid(row=3, column=0)
entry3=tk.Entry(width=20)
entry3.grid(row=3, column=2)


button1=tk.Button(text="Generate Password",width=16,command= generate_password_2 )
button1.grid(row=3, column=3)

button2 = tk.Button(text="Add", width=16, command = save)
button2.grid(column=1, row=4, columnspan=2)

button3=tk.Button(text="Find", width=16, command=find)
button3.grid(column=3, row=2)


screen.mainloop()