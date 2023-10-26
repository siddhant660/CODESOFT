from tkinter import *

def add_entry():
    name = name_entry.get()
    number = number_entry.get()
    address_text = address.get("1.0", "end-1c")
    if name and number and address_text:
        entry = f"Name: {name}, Phone No.: {number}, Address: {address_text}"
        select.insert(END, entry)
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        address.delete("1.0", END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def delete_entry():
    selected = select.curselection()
    if selected:
        select.delete(selected)

root = Tk()
root.geometry('400x500')

frame = Frame(root)
frame.pack(pady=10)

frame1 = Frame(root)
frame1.pack()

frame2 = Frame(root)
frame2.pack(pady=10)

Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
name_entry = Entry(frame, width=50)
name_entry.pack()

Label(frame1, text='Phone No.', font='arial 12 bold').pack(side=LEFT)
number_entry = Entry(frame1, width=50)
number_entry.pack()

Label(frame2, text='Address', font='arial 12 bold').pack(side=LEFT)
address = Text(frame2, width=37, height=10)
address.pack()

Button(root, text="Add", font="arial 12 bold", command=add_entry).place(x=100, y=270)
Button(root, text="Delete", font="arial 12 bold", command=delete_entry).place(x=100, y=310)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200, y=260)

root.mainloop()
