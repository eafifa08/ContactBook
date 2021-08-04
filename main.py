# Simple ContactBook - Простая книга контактов
import tkinter as tk
import sqlite3


def create_table():
    pass


def init_database():
    try:
        sqlite_connection = sqlite3.connect('contacts.sqlite')
        cursor = sqlite_connection.cursor()
        print('База данных создана и успешно подключена')

        query_select_version = "select sqlite_version();"
        query_create_table = 'CREATE TABLE IF NOT EXISTS contacts' \
                             ' (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);'
        cursor.execute(query_select_version)
        record = cursor.fetchall()
        print('Версия базы данных SQLite:', record)
        cursor.execute(query_create_table)
        cursor.close()
    except sqlite3.Error as error:
        print('Ошибка при подключении к sqlite', error)
    finally:
        if(sqlite_connection):
            sqlite_connection.close()
            print('Соединение с SQLite закрыто')


class Contact:
    def __init__(self, name, tel, address='none', email='none'):
        print(f'Contact of {name} initializated')
        self.name = name
        self.tel = tel
        self.address = address
        self.email = email


def start_window():
    init_database()
    window = tk.Tk()
    window.title("Contact Book")
    button_add = tk.Button(window, text="Новый контакт")
    button_add.pack()
    frame = tk.Frame(borderwidth=5, relief=tk.GROOVE)
    label = tk.Label(master=frame, text="Hello", bg='red')
    label.pack()
    frame.pack()
    contacts = []
    for i in range(5):
        contact = Contact(i, i+i)
        contacts.append(contact)
    gorgona_contact = Contact('Ж', 8908888741)
    contacts.append(gorgona_contact)
    listbox = tk.Listbox(window)
    for contact in contacts:
        listbox.insert(tk.END, contact.name)
    listbox.pack()

    window.geometry("400x400")
    window.mainloop()


if __name__ == '__main__':
    start_window()