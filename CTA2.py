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
    # Implementasi logika autentikasi pengguna
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

        exit_button = tk.Button(self.root, text="Keluar", command=self.root.destroy)
        exit_button.pack()

    def admin_login_menu(self):
        # Implementasi login admin
        pass

    def admin_login(self):
        # Implementasi login admin
        pass

    def admin_menu(self):
        # Implementasi menu admin
        pass

    def add_member_menu(self):
        # Implementasi menu tambah anggota tim
        pass

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

        search_member_button = tk.Button(self.root, text="Cari Anggota Tim", command=self.search_member_menu)
        search_member_button.pack()

        back_button = tk.Button(self.root, text="Kembali", command=self.main_menu)
        back_button.pack()

    def search_member_menu(self):
        self.clear_screen()
        label = tk.Label(self.root, text="Cari Anggota Tim", font=("Helvetica", 16))
        label.pack(pady=10)

        self.skills_label = tk.Label(self.root, text="Keterampilan yang dicari (pisahkan dengan koma):")
        self.skills_label.pack()
        self.skills_entry = tk.Entry(self.root)
        self.skills_entry.pack()

        search_button = tk.Button(self.root, text="Cari", command=self.search_member)
        search_button.pack()

    def search_member(self):
        required_skills = self.skills_entry.get().split(',')
        potential_members = self.team.find_members(required_skills)
        if potential_members:
            messagebox.showinfo("Info", "Anggota tim yang cocok ditemukan:\n{}".format("\n".join(member.name for member in potential_members)))
        else:
            messagebox.showinfo("Info", "Tidak ada anggota tim yang cocok ditemukan.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    root.title("FIND TEAM")
    root.geometry("400x300")

    app = GUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()
