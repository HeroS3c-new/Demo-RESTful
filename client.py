import tkinter as tk
from tkinter import font
import requests

API_URL = 'http://localhost:5000'



def connection_error():
    root = tk.Tk()
    root.title('Errore')
    root.geometry('200x50')
    tk.Label(root, text='Server non attivo', font=font.Font(size=12)).pack()
    tk.Frame(root).pack()
    root.mainloop()
    
def get_corsi():
    corsi = []
    try:
        response = requests.get(f'{API_URL}/corsi')
        corsi = response.json()
    except:
        connection_error()
    return corsi

def populate_corsi_listbox(corsi_listbox):
    corsi_listbox.delete(0, tk.END)
    corsi = get_corsi()
    for corso in corsi:
        corsi_listbox.insert(tk.END, f"{corso['id']} - {corso['nome']} ({corso['dipartimento']})")

def create_corso(nome, dipartimento):
    try:
        nuovo_corso = {'nome': nome, 'dipartimento': dipartimento}
        response = requests.post(f'{API_URL}/corsi', json=nuovo_corso)
    except:
        connection_error()
    return response.json()

def delete_corso(corso_id, corsi_listbox):
    try:
        response = requests.delete(f'{API_URL}/corsi/{corso_id.get()}')
        populate_corsi_listbox(corsi_listbox)
    except:
        connection_error()
    return response.status_code

def on_create_corso_button_click(nome_entry, dipartimento_entry, corsi_listbox):
    nome = nome_entry.get()
    dipartimento = dipartimento_entry.get()
    create_corso(nome, dipartimento)
    populate_corsi_listbox(corsi_listbox)

def create_gui():
    root = tk.Tk()
    root.title('API REST - Università degli Studi di Perugia (Unipg)')
    root.geometry('800x600')

    corsi_label = tk.Label(root, text='Corsi:', font=font.Font(size=20))
    corsi_label.pack()

    corsi_listbox = tk.Listbox(root)
    corsi_listbox.pack(fill=tk.BOTH, expand=True)

    populate_corsi_listbox(corsi_listbox)

    create_corso_frame = tk.Frame(root)
    create_corso_frame.pack()

    nome_label = tk.Label(create_corso_frame, text='Nome:')
    nome_label.grid(row=0, column=0)

    nome_entry = tk.Entry(create_corso_frame)
    nome_entry.grid(row=0, column=1)

    dipartimento_label = tk.Label(create_corso_frame, text='Dipartimento:')
    dipartimento_label.grid(row=1, column=0)

    dipartimento_entry = tk.Entry(create_corso_frame)
    dipartimento_entry.grid(row=1, column=1)

    create_corso_button = tk.Button(create_corso_frame, text='Crea corso', command=lambda: on_create_corso_button_click(nome_entry, dipartimento_entry, corsi_listbox))
    create_corso_button.grid(row=2, column=0, columnspan=2)

    delete_corso_frame = tk.Frame(root)
    delete_corso_frame.pack()

    id_label = tk.Label(delete_corso_frame, text='ID:')
    id_label.grid(row=0, column=0)

    id_entry = tk.Entry(delete_corso_frame)
    id_entry.grid(row=0, column=1)

    delete_corso_button = tk.Button(delete_corso_frame, text='Elimina', command=lambda: delete_corso(id_entry, corsi_listbox))
    delete_corso_button.grid(row=1, column=0, columnspan=2)

    root.mainloop()

if __name__ == '__main__':
    try: 
        requests.get(f'{API_URL}/corsi')
        create_gui()
    except:
        connection_error()
