# Simple ContactBook - Простая книга контактов
import tkinter as tk
import sqlite3

window = tk.Tk()


def insert_contact_to_db(contact):
    try:
        conn = sqlite3.connect('contacts.sqlite')
        cursor = conn.cursor()
        query_insert_contact = """INSERT INTO contacts (name, tel)
                                VALUES (?,?)
        """
        cursor.execute(query_insert_contact, (contact.name, contact.tel))
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Ошибка при подключении к sqlite', error)
    finally:
        if(conn):
            conn.close()
            print('Соединение с SQLite закрыто')


def get_all_contacts_from_db():
    contacts = []
    try:
        conn = sqlite3.connect('contacts.sqlite')
        cursor = conn.cursor()
        query_get_all_contacts = """SELECT name, tel FROM contacts"""
        cursor.execute(query_get_all_contacts)
        records = cursor.fetchall()
        for record in records:
            contacts.append(Contact(record[0], record[1]))
        cursor.close()
    except sqlite3.Error as error:
        print('Ошибка при подключении к sqlite', error)
    finally:
        if(conn):
            conn.close()
            print('Соединение с SQLite закрыто')
        return contacts


def init_database():
    try:
        sqlite_connection = sqlite3.connect('contacts.sqlite')
        cursor = sqlite_connection.cursor()
        print('База данных создана и успешно подключена')

        query_select_version = "select sqlite_version();"
        query_create_table = 'CREATE TABLE IF NOT EXISTS contacts' \
                             ' (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, tel INTEGER UNIQUE);'
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
        self.name = str(name)
        self.tel = tel
        self.address = address
        self.email = email


def show_new_contact():
    print('show_new_contact')
    e_name = tk.Entry(window, name='name')
    e_name.grid(row=0, column=2)
    e_tel = tk.Entry(window, name='tel')
    e_tel.grid(row=0, column=3)
    btn_save_new_contact = tk.Button(window, text='сохранить', name='to_save')
    btn_save_new_contact.config(command=save_new_contact)
    btn_save_new_contact.grid(row=0, column=4)
    return (e_name, e_tel, btn_save_new_contact)


def unshow_new_contact():
    elements = [window.nametowidget('tel'), window.nametowidget('name'), window.nametowidget('to_save')]
    for element in elements:
        element.grid_remove()
    print('unshow_new_contact')


def save_new_contact():
    name = window.nametowidget('name').get()
    tel = window.nametowidget('tel').get()
    print(name)
    contact = Contact(name, tel)
    insert_contact_to_db(contact)
    refresh_listbox()
    unshow_new_contact()


def refresh_listbox():
    listbox = window.nametowidget('lstbx_contacts')
    listbox.delete(0, 'end')
    contacts = get_all_contacts_from_db()
    for contact in contacts:
        listbox.insert(tk.END, contact.name)


def start_window():
    init_database()

    window.title("Contact Book")
    button_add = tk.Button(window, text="Новый контакт")
    button_add.grid(row=0, column=1)
    button_add.bind("button_add", show_new_contact)
    button_add.config(command=show_new_contact)
    contacts = []
    for i in range(5):
        contact = Contact(i, str(i) * 8)
        contacts.append(contact)
    gorgona_contact = Contact('Ж', 8908888741)
    contacts.append(gorgona_contact)
    listbox = tk.Listbox(window, name='lstbx_contacts')
    scrollbar = tk.Scrollbar(listbox, orient='vertical')
    for contact in contacts:
        insert_contact_to_db(contact)
    refresh_listbox()
    listbox.grid(row=0, column=0, rowspan=5)
    show_new_contact()
    unshow_new_contact()

    window.geometry("600x400")
    window.mainloop()


if __name__ == '__main__':
    start_window()