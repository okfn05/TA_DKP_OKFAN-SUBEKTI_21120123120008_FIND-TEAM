import tkinter as tk
from tkinter import simpledialog, messagebox

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
        messagebox.showinfo("Sukses", f"Anggota {name} berhasil ditambahkan ke tim.")

    def find_members(self, required_skills):
        potential_members = []
        for member in self.members:
            if all(skill in member.skillset for skill in required_skills):
                potential_members.append(member)
        return potential_members

def admin_login():
    username = simpledialog.askstring("Login Admin", "Masukkan username admin:")
    password = simpledialog.askstring("Login Admin", "Masukkan password admin:", show='*')
    return username == "admin" and password == "admin123"

def admin_menu(team):
    def add_member():
        name = simpledialog.askstring("Tambah Anggota Tim", "Masukkan nama anggota tim:")
        skillset = simpledialog.askstring("Tambah Anggota Tim", "Masukkan keterampilan anggota tim (pisahkan dengan koma):").split(',')
        team.add_member(name, skillset)
    
    admin_window = tk.Toplevel()
    admin_window.title("Menu Admin")
    
    tk.Button(admin_window, text="Tambah Anggota Tim", command=add_member).pack(pady=10)
    tk.Button(admin_window, text="Kembali ke Menu Utama", command=admin_window.destroy).pack(pady=10)

def user_menu(team):
    def find_members():
        required_skills = simpledialog.askstring("Cari Anggota Tim", "Masukkan keterampilan yang Anda cari (pisahkan dengan koma):").split(',')
        potential_members = team.find_members(required_skills)
        if potential_members:
            message = "Anggota tim yang cocok ditemukan:\n"
            for member in potential_members:
                message += f"- {member.name}\n"
            messagebox.showinfo("Hasil Pencarian", message)
        else:
            messagebox.showinfo("Hasil Pencarian", "Tidak ada anggota tim yang cocok ditemukan.")
    
    user_window = tk.Toplevel()
    user_window.title("Menu User")
    
    tk.Button(user_window, text="Cari Anggota Tim", command=find_members).pack(pady=10)
    tk.Button(user_window, text="Keluar", command=user_window.destroy).pack(pady=10)

def main():
    team = Team()
    
    root = tk.Tk()
    root.title("FIND TEAM")
    
    def login_as_admin():
        if admin_login():
            admin_menu(team)
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")
    
    def login_as_user():
        user_menu(team)
    
    tk.Button(root, text="Login Admin", command=login_as_admin).pack(pady=10)
    tk.Button(root, text="Login User", command=login_as_user).pack(pady=10)
    tk.Button(root, text="Keluar", command=root.quit).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
