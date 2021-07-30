# Simple ContactBook - Простая книга контактов
import tkinter as tk


class Contact:
    def __init__(self, name, tel, address='none', email='none'):
        print(f'Contact of {name} initializated')
        self.name = name
        self.tel = tel
        self.address = address
        self.email = email


def start_window():
    window = tk.Tk()
    window.title("Contact Book")

    button_add = tk.Button(window, text="Добавить")
    button_add.pack()

    frame = tk.Frame(borderwidth=5, relief=tk.GROOVE)
    label = tk.Label(master=frame, text="Hello", bg='red')
    label.pack()
    frame.pack()


    contacts = []
    for i in range(5):
        contact = Contact(i,i+i)
        contacts.append(contact)
    cars = ['vaz', 'mercedes', 'bmw', 'opel']
    listbox = tk.Listbox(window)
    for contact in contacts:
        listbox.insert(tk.END, contact.name)
    listbox.pack()

    window.geometry("400x400")
    window.mainloop()


if __name__ == '__main__':
    start_window()