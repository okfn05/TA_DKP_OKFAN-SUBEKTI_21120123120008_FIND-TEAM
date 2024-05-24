import tkinter as tk
from tkinter import messagebox

class TeamMember:
    def __init__(self, name, skillset):
        self.name = name
        self.skillset = skillset

class Team:
    def __init__(self):
        self.members = []

    def add_member(self, name, skillset):
        member = TeamMember(name, skillset)
        self.members.append(member)
        messagebox.showinfo("Info", "Anggota {} berhasil ditambahkan ke tim.".format(name))

    def find_members(self, required_skills):
        potential_members = []
        for member in self.members:
            if all(skill in member.skillset for skill in required_skills):
                potential_members.append(member)
        return potential_members

def admin_login(username, password):
    return username == "admin" and password == "admin123"

def user_login(username, password):
    return True

class GUI:
    def __init__(self, root):
        self.root = root
        self.team = Team()

        self.main_menu()

    def main_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Menu Utama", font=("Helvetica", 16))
        label.pack(pady=10)

        admin_button = tk.Button(self.root, text="Login Admin", command=self.admin_login_menu)
        admin_button.pack()

        user_button = tk.Button(self.root, text="Login User", command=self.user_login_menu)
        user_button.pack()

        register_button = tk.Button(self.root, text="Daftar Akun", command=self.register_menu)
        register_button.pack()

        exit_button = tk.Button(self.root, text="Keluar", command=self.root.destroy)
        exit_button.pack()

    def register_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Daftar Akun", font=("Helvetica", 16))
        label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        register_button = tk.Button(self.root, text="Daftar", command=self.register_account)
        register_button.pack()

        back_button = tk.Button(self.root, text="Kembali", command=self.main_menu)
        back_button.pack()

    def register_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Implementasi logika pendaftaran akun
        # Misalnya, validasi, penambahan ke database, dll.
        messagebox.showinfo("Info", "Akun dengan username {} berhasil didaftarkan.".format(username))

    def admin_login_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Login Admin", font=("Helvetica", 16))
        label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self.root, text="Login", command=self.admin_login)
        login_button.pack()

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if admin_login(username, password):
            self.admin_menu()
        else:
            messagebox.showerror("Error", "Login gagal. Username atau password salah.")

    def admin_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Menu Admin", font=("Helvetica", 16))
        label.pack(pady=10)

        add_member_button = tk.Button(self.root, text="Tambah Anggota Tim", command=self.add_member_menu)
        add_member_button.pack()

        logout_button = tk.Button(self.root, text="Logout", command=self.main_menu)
        logout_button.pack()

    def add_member_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Tambah Anggota Tim", font=("Helvetica", 16))
        label.pack(pady=10)

        self.name_label = tk.Label(self.root, text="Nama:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.skillset_label = tk.Label(self.root, text="Kemampuan yang dimiliki (pisahkan dengan koma):")
        self.skillset_label.pack()
        self.skillset_entry = tk.Entry(self.root)
        self.skillset_entry.pack()

        add_button = tk.Button(self.root, text="Tambah", command=self.add_member)
        add_button.pack()

        back_button = tk.Button(self.root, text="Kembali", command=self.admin_menu)
        back_button.pack()

    def add_member(self):
        name = self.name_entry.get()
        skillset = self.skillset_entry.get().split(',')
        skillset = [skill.strip() for skill in skillset]
        self.team.add_member(name, skillset)

    def user_login_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Login User", font=("Helvetica", 16))
        label.pack(pady=10)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        login_button = tk.Button(self.root, text="Login", command=self.user_login)
        login_button.pack()

    def user_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if user_login(username, password):
            self.user_menu()
        else:
            messagebox.showerror("Error", "Login gagal. Username atau password salah.")

    def user_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Menu User", font=("Helvetica", 16))
        label.pack(pady=10)

        search_button = tk.Button(self.root, text="Cari Anggota Tim", command=self.search_member_menu)
        search_button.pack()

        logout_button = tk.Button(self.root, text="Logout", command=self.main_menu)
        logout_button.pack()

    def search_member_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Cari Anggota Tim", font=("Helvetica", 16))
        label.pack(pady=10)

        self.skillset_label = tk.Label(self.root, text="Kemampuan yang diinginkan (pisahkan dengan koma):")
        self.skillset_label.pack()
        self.skillset_entry = tk.Entry(self.root)
        self.skillset_entry.pack()

        search_button = tk.Button(self.root, text="Cari", command=self.search_member)
