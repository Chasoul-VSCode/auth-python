import sqlite3
from hashlib import sha256

# Fungsi untuk membuat database dan tabel
def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# Fungsi untuk mendaftar pengguna baru
def register(username, password):
    hashed_password = sha256(password.encode()).hexdigest()
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("Registrasi berhasil!")
    except sqlite3.IntegrityError:
        print("Username sudah terdaftar.")
    finally:
        conn.close()

# Fungsi untuk login pengguna
def login(username, password):
    hashed_password = sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = c.fetchone()
    conn.close()
    
    if user:
        print("Login berhasil!")
    else:
        print("Username atau password salah.")

# Fungsi utama untuk menu
def main():
    create_db()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih opsi (1/2/3): ")
        
        if choice == '1':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            register(username, password)
        elif choice == '2':
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            login(username, password)
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
