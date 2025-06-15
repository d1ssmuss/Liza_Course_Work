# Окно регистрации и входа
# Добавить шифрование cryptography


import subprocess
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os
import sys

# Генерируйте ключ один раз и сохраните в файл. Потом загружайте его.
KEY_FILE = "secret.key"
USER_FILE = "users.txt"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def save_user(username, encrypted_password):
    with open(USER_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username}:{encrypted_password}\n")

def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    u, p = line.strip().split(":", 1)
                    users[u] = p
    return users

def launch_main_py():
    """
    Запускает файл main.py и закрывает текущее окно.
    """
    subprocess.Popen(['python', "main.py"])
    time.sleep(0.7)
    root.destroy()

def register():
    username = username_entry.get().strip()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    users = load_users()
    if username in users:
        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует.")
        return

    encrypted_password = encrypt_password(password)
    save_user(username, encrypted_password)
    messagebox.showinfo("Успех", "Регистрация прошла успешно!")
    username_entry.delete(0, END)
    password_entry.delete(0, END)

def login():
    username = username_entry_login.get().strip()
    password = password_entry_login.get()
    if not username or not password:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    users = load_users()
    encrypted_password = users.get(username)
    if encrypted_password is None:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")
        return

    try:
        decrypted_password = decrypt_password(encrypted_password)
    except:
        messagebox.showerror("Ошибка", "Ошибка при дешифровке пароля.")
        return

    if decrypted_password == password:
        messagebox.showinfo("Успех", "Вход выполнен успешно!")
        username_entry_login.delete(0, END)
        password_entry_login.delete(0, END)
        launch_main_py()  # Запуск main.py при успехе
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")

root = Tk()
root.title("Регистрация и вход")
root.geometry('%dx%d+%d+%d' % (800, 800, 550, 150))


notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)

# Регистрация
ttk.Label(frame1, text="Регистрация", font=("Tahoma", 20)).pack(pady=10)

ttk.Label(frame1, text="Логин:", font=("Tahoma", 18)).pack(pady=5)
username_entry = ttk.Entry(frame1)
username_entry.pack(pady=5)

ttk.Label(frame1, text="Пароль:", font=("Tahoma", 18)).pack(pady=5)
password_entry = ttk.Entry(frame1, show='*')
password_entry.pack(pady=5)

ttk.Button(frame1, text="Зарегистрироваться", command=register).pack(pady=20)

# Вход
ttk.Label(frame2, text="Вход", font=("Tahoma", 20)).pack(pady=10)

ttk.Label(frame2, text="Логин:", font=("Tahoma", 18)).pack(pady=5)
username_entry_login = ttk.Entry(frame2)
username_entry_login.pack(pady=5)

ttk.Label(frame2, text="Пароль:", font=("Tahoma", 18)).pack(pady=5)
password_entry_login = ttk.Entry(frame2, show='*')
password_entry_login.pack(pady=5)

ttk.Button(frame2, text="Войти", command=login).pack(pady=20)

notebook.add(frame1, text="Регистрация")
notebook.add(frame2, text="Вход")

# notebook.select(1) для переключения на вкладку "Вход" сразу

root.mainloop()
