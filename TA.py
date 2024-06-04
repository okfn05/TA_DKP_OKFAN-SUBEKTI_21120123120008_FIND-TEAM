import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

class FindTeamApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Find Team App')
        self.root.geometry("400x300")
        self.members = []
        self.proposed_members = [] 

        # Bagian ilustrasi dan judul
        self.illustration_frame = tk.Frame(self.root, bg='#129ac7', width=50, height=300)
        self.illustration_frame.pack(side='left', fill='both', expand=True)

        # Gambar (tidak termasuk dalam perubahan)
        self.welcome_text = tk.Label(self.illustration_frame, text='Welcome!', fg='white', bg='#129ac7', font=('League Spartan', 30, 'bold'))
        self.welcome_text.pack(pady=(50, 10)) 

        self.illustration_image = Image.open('Gambar 1.png')  # Ganti dengan path ke gambar ilustrasi Anda
        resized_image = self.illustration_image.resize((522, 357), Image.LANCZOS)
        self.illustration_image = ImageTk.PhotoImage(resized_image)
        self.image_label = tk.Label(self.illustration_frame, image=self.illustration_image, bg='#129ac7')
        self.image_label.image = self.illustration_image  
        self.image_label.pack()

        self.image_text = tk.Label(self.illustration_frame, text='FIND TEAM', fg='white', bg='#129ac7', font=('Lilita One', 60))
        self.image_text.pack(pady=(0, 10))
        self.image_subtext = tk.Label(self.illustration_frame, text='Connect, Collaborate, and Conquer', fg='white', bg='#129ac7', font=('League Spartan', 30))
        self.image_subtext.pack()

        # Bagian Sign In
        self.sign_in_frame = tk.Frame(self.root, bg= '#129ac7')
        self.sign_in_frame.pack(side='right', fill='both', expand=True)
        self.sign_in_label = tk.Label(self.sign_in_frame, text='Sign In', fg= 'white', bg= '#129ac7', font=('League Spartan', 45, 'bold'))
        self.sign_in_label.pack(pady=(100, 20))

        # Tombol Admin
        self.admin_button = tk.Button(self.sign_in_frame, text='Admin', font=('League Spartan', 17, 'bold'), 
                                      command=self.show_admin_login_fields, width=11, height= 1, relief=tk.FLAT, fg='#129ac7', bg= 'white')
        self.admin_button.pack(pady=5)

        # Tombol User
        self.user_button = tk.Button(self.sign_in_frame, text='User', font=('League Spartan', 17, 'bold'), 
                                      command=self.show_user_login_fields, width=11, height= 1, relief=tk.FLAT, fg='#129ac7', bg= 'white')
        self.user_button.pack(pady=5)

        # Tombol Keluar
        self.exit_button = tk.Button(self.sign_in_frame, text='Exit', font=('League Spartan', 17, 'bold'), 
                                      command=self.exit_program, width=11, height= 1, relief=tk.FLAT, fg='#129ac7', bg= 'white')
        self.exit_button.pack(pady=5)

         # Membuat frame untuk Don't have account dan Sign Up
        self.account_frame = tk.Frame(self.sign_in_frame, bg='#129ac7')
        self.account_frame.pack(side='bottom', pady=(0, 10))

        # Label untuk "Don't have account?"
        self.no_account_label = tk.Label(self.account_frame, text="Don't have account?", fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.no_account_label.grid(row=0, column=0, padx=(0,5))

        # Tombol untuk "Sign Up"
        self.sign_up_button = tk.Button(self.account_frame, text='Sign Up', font=('League Spartan', 20, 'bold'), 
                                        command=self.sign_up, relief=tk.FLAT, bg='#129ac7', fg='white', cursor='hand2')
        self.sign_up_button.grid(row=0, column=1)

        # Dictionary untuk menyimpan akun yang didaftarkan
        self.registered_accounts = {}

##Adminnnnnnnnnnnnnnnnnnnnnnnnnnn#######################################################################
########################################################################################################
    def show_admin_login_fields(self):
        # Membuat jendela baru untuk login admin
        self.admin_login_window = tk.Toplevel(self.root)
        self.admin_login_window.title('Admin Login')
        self.admin_login_window.geometry("400x300")
        self.admin_login_window.configure(bg='#129ac7')

        self.admin_label = tk.Label(self.admin_login_window, text='Log in as Admin', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.admin_label.pack(pady=(10, 0))

        # Label untuk "Email"
        self.email_label = tk.Label(self.admin_login_window, text='Email:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.email_label.pack(pady=(10, 0))
        self.email_entry = tk.Entry(self.admin_login_window, font=('League Spartan', 15))
        self.email_entry.pack(pady=(0, 10))

        # Label untuk "Password"
        self.password_label = tk.Label(self.admin_login_window, text='Password:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.password_label.pack(pady=(10, 0))
        self.password_entry = tk.Entry(self.admin_login_window, show='*', font=('League Spartan', 15))
        self.password_entry.pack(pady=(0, 10))

        # Tombol login
        self.login_button = tk.Button(self.admin_login_window, text='Login', command=self.login_admin, fg='#129ac7', bg='white', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        self.login_button.pack(pady=(10, 10))

          # Tombol kembali
        self.back_button = tk.Button(self.admin_login_window, text='Back', command=self.close_admin_login_window, fg='#129ac7', bg='white', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        self.back_button.pack(pady=(0, 10))

        # Frame untuk background
        self.frame = tk.Frame(self.admin_login_window, bg='#129ac7')
        self.frame.pack(pady=(10, 10))
    def close_admin_login_window(self):
        self.admin_login_window.destroy()

    def login_admin(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if email in self.registered_accounts:
            user_type = self.registered_accounts[email].get('User Type', '')
            if user_type == 'Admin': 
                admin_credentials = self.registered_accounts.get(email, {}).get('Password')
                if admin_credentials and admin_credentials == password:
                    self.show_admin_dashboard()
                else:
                    messagebox.showerror("Error", "Invalid email or password")
            else:
                messagebox.showerror("Error", "Invalid email or password")
        else:
            messagebox.showerror("Error", "Invalid email or password")

    def show_admin_dashboard(self):
        if hasattr(self, "admin_login_window"):
            self.admin_login_window.destroy()

        self.admin_dashboard_window = tk.Toplevel(self.root)
        self.admin_dashboard_window.title('Admin Dashboard')
        self.admin_dashboard_window.geometry("400x300")
        self.admin_dashboard_window.configure(bg='#129ac7')

        self.admin_dashboard_label = tk.Label(self.admin_dashboard_window, text='Menu Utama', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.admin_dashboard_label.pack(pady=(10, 0))

        # tampilan admin
        add_member_button = tk.Button(self.admin_dashboard_window, text="Add Member", command=self.add_member, fg='#129ac7', bg='white', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        add_member_button.pack(pady=10)

        delete_member_button = tk.Button(self.admin_dashboard_window, text="Delete Member", command=self.delete_member, fg='#129ac7', bg='white', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        delete_member_button.pack(pady=10)

        approve_permission_button = tk.Button(self.admin_dashboard_window, text="Approve Permission", command=self.approve_permission, fg='#129ac7', bg='white', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        approve_permission_button.pack(pady=10)

        # tombol kembali
        back_button = tk.Button(self.admin_dashboard_window, text="Back", command=self.close_admin_dashboard, fg='#129ac7', bg='white', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        back_button.pack(pady=10)

    def close_admin_dashboard(self):
        self.admin_dashboard_window.destroy()


    def add_member(self):
        # Membuat jendela baru untuk menambahkan anggota
        self.add_member_window = tk.Toplevel(self.root)
        self.add_member_window.title('Add Member')
        self.add_member_window.geometry("400x300")
        self.add_member_window.configure(bg='#129ac7')

        self.member_label = tk.Label(self.add_member_window, text='Add Member', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.member_label.pack(pady=(10, 0))

        # Label untuk "Nama"
        self.name_label = tk.Label(self.add_member_window, text='Name:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.name_label.pack(pady=(10, 0))
        self.name_entry = tk.Entry(self.add_member_window, font=('League Spartan', 15))
        self.name_entry.pack(pady=(0, 10))

        # Label untuk "Skill"
        self.skill_label = tk.Label(self.add_member_window, text='Skill:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.skill_label.pack(pady=(10, 0))
        self.skill_entry = tk.Entry(self.add_member_window, font=('League Spartan', 15))
        self.skill_entry.pack(pady=(0, 10))

        # Label untuk "Kontak"
        self.contact_label = tk.Label(self.add_member_window, text='Contact:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.contact_label.pack(pady=(10, 0))
        self.contact_entry = tk.Entry(self.add_member_window, font=('League Spartan', 15))
        self.contact_entry.pack(pady=(0, 10))

        # Tombol tambah anggota
        self.add_member_button = tk.Button(self.add_member_window, text='Add Member', command=self.save_member, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        self.add_member_button.pack(pady=(10, 10))

    def save_member(self):
        name = self.name_entry.get()
        skill = self.skill_entry.get()
        contact = self.contact_entry.get()

        if not name or not skill or not contact:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Menyimpan data anggota baru
        new_member = {"Name": name, "Skill": skill, "Contact": contact}
        # Menambahkan data anggota baru ke dalam list data anggota
        self.members.append(new_member)
        messagebox.showinfo("Success", "Member added successfully")
        self.add_member_window.destroy()

    def delete_member(self):
        # Membuat jendela baru untuk menghapus anggota
        self.delete_member_window = tk.Toplevel(self.root)
        self.delete_member_window.title('Delete Member')
        self.delete_member_window.geometry("400x300")
        self.delete_member_window.configure(bg='#129ac7')

        self.member_label = tk.Label(self.delete_member_window, text='Delete Member', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.member_label.pack(pady=(10, 0))

        # Label untuk "Nama"
        self.name_label = tk.Label(self.delete_member_window, text='Name:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.name_label.pack(pady=(10, 0))
        self.name_entry = tk.Entry(self.delete_member_window, font=('League Spartan', 15))
        self.name_entry.pack(pady=(0, 10))

        # Tombol hapus anggota
        self.delete_member_button = tk.Button(self.delete_member_window, text='Delete Member', command=self.remove_member, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        self.delete_member_button.pack(pady=(10, 10))

    def remove_member(self):
        name = self.name_entry.get()

        if not name:
            messagebox.showerror("Error", "Please fill in the name field")
            return

        # Mencari anggota berdasarkan nama
        for member in self.members:
            if member['Name'] == name:
                # Menghapus anggota dari daftar members
                self.members.remove(member)
                messagebox.showinfo("Success", "Member deleted successfully")
                self.delete_member_window.destroy()
                # Memperbarui tampilan tabel pengguna setelah menghapus anggota
                self.show_user_dashboard(email=None)  # Menyertakan email=None sebagai nilai default
                return

        messagebox.showerror("Error", "Member not found")
        self.delete_member_window.destroy()



    def approve_permission(self):
        # Membuat jendela baru untuk mengelola anggota yang diajukan
        self.manage_proposed_window = tk.Toplevel(self.root)
        self.manage_proposed_window.title('Manage Proposed Members')
        self.manage_proposed_window.geometry("400x400")
        self.manage_proposed_window.configure(bg='#129ac7')

        self.proposed_member_label = tk.Label(self.manage_proposed_window, text='Proposed Members', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.proposed_member_label.pack(pady=(10, 0))

        # Menampilkan daftar anggota yang diajukan
        for idx, member in enumerate(self.proposed_members, start=1):
            tk.Label(self.manage_proposed_window, text=f"Name: {member['Name']}", fg='white', bg='#129ac7', font=('League Spartan', 15)).pack(pady=(10, 0))
            tk.Label(self.manage_proposed_window, text=f"Skill: {member['Skill']}", fg='white', bg='#129ac7', font=('League Spartan', 15)).pack(pady=(10, 0))
            tk.Label(self.manage_proposed_window, text=f"Contact: {member['Contact']}", fg='white', bg='#129ac7', font=('League Spartan', 15)).pack(pady=(10, 0))
            # Tombol untuk menyetujui anggota
            approve_button = tk.Button(self.manage_proposed_window, text=f'Approve {member["Name"]}', command=lambda mem=member: self.approve_member(mem), fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
            approve_button.pack(pady=(10, 0))
            # Tombol untuk menolak anggota
            reject_button = tk.Button(self.manage_proposed_window, text=f'Reject {member["Name"]}', command=lambda mem=member: self.reject_member(mem), fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
            reject_button.pack(pady=(10, 0))

    def approve_member(self, member):
        # Menghapus anggota dari daftar anggota yang diajukan
        self.proposed_members.remove(member)
        # Menambahkan anggota ke dalam daftar anggota yang disetujui
        self.members.append(member)
        # Menutup jendela "Manage Proposed Members"
        self.manage_proposed_window.destroy()
        # Memberi informasi bahwa anggota telah disetujui
        messagebox.showinfo("Success", f"{member['Name']} has been approved.")

    def reject_member(self, member):
        # Menghapus anggota dari daftar anggota yang diajukan
        self.proposed_members.remove(member)
        # Menutup jendela "Manage Proposed Members"
        self.manage_proposed_window.destroy()
        # Memberi informasi bahwa anggota telah ditolak
        messagebox.showinfo("Success", f"{member['Name']} has been rejected.")


    def close_admin_dashboard(self):
        self.admin_dashboard_window.destroy()
    def close_admin_login_window(self):
        self.admin_login_window.destroy()


##Userrrrrrrrrrrrrrr#######################################################################
###########################################################################################
    def show_user_login_fields(self):
        # Membuat jendela baru untuk login user
        self.user_login_window = tk.Toplevel(self.root)
        self.user_login_window.title('User Login')
        self.user_login_window.geometry("400x300")
        self.user_login_window.configure(bg='#129ac7')

        self.user_label = tk.Label(self.user_login_window, text='Log in as User', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.user_label.pack(pady=(10, 0))

        # Label untuk "Email"
        self.email_label = tk.Label(self.user_login_window, text='Email:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.email_label.pack(pady=(10, 0))
        self.email_entry = tk.Entry(self.user_login_window, font=('League Spartan', 15))
        self.email_entry.pack(pady=(0, 10))

        # Label untuk "Password"
        self.password_label = tk.Label(self.user_login_window, text='Password:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.password_label.pack(pady=(10, 0))
        self.password_entry = tk.Entry(self.user_login_window, show='*', font=('League Spartan', 15))
        self.password_entry.pack(pady=(0, 10))

         # Tombol login
        self.login_button = tk.Button(self.user_login_window, text='Login', command=self.login_user, fg='#129ac7', bg='White', font=('League Spartan', 15,'bold'), width= 15, height= 1)
        self.login_button.pack(pady=(10, 10))

               # Tombol kembali
        self.back_button = tk.Button(self.user_login_window, text='Back', command=self.close_user_login_window, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        self.back_button.pack(pady=(0, 10))

        # Frame untuk background
        self.frame = tk.Frame(self.user_login_window, bg='#129ac7')
        self.frame.pack(pady=(10, 10))
    def close_user_login_window(self):
        self.user_login_window.destroy()
    def login_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if email in self.registered_accounts:
            if self.registered_accounts[email]['Password'] == password:
                self.show_user_dashboard(email)
            else:
                messagebox.showerror("Error", "Invalid email or password")
        else:
            messagebox.showerror("Error", "Invalid email or password")

    def show_user_dashboard(self, email):
        self.user_login_window.destroy()

        self.user_dashboard_window = tk.Toplevel(self.root)
        self.user_dashboard_window.title('User Dashboard')
        self.user_dashboard_window.configure(bg='#129ac7')

        # tabel
        table_frame = tk.Frame(self.user_dashboard_window)
        table_frame.pack(pady=20)
        headers = ["Nama", "Skill", "Kontak yang dapat dihubungi"]
        self.tree = ttk.Treeview(table_frame, columns=headers, show="headings")
        self.tree.pack(fill="both", expand=True)
        for header in headers:
            self.tree.heading(header, text=header)
        for member in self.members:
            self.tree.insert("", "end", values=(member['Name'], member['Skill'], member['Contact']))
        for col in headers:
            self.tree.column(col, anchor="center")
            self.tree.heading(col, text=col, anchor="center")
            self.tree.configure(show="headings", height=len(self.members))

        # search
        search_entry = tk.Entry(self.user_dashboard_window, font=('League Spartan', 12))
        search_entry.pack(pady=(10, 5))
        search_button = tk.Button(self.user_dashboard_window, text="Search", command=lambda: self.search_data(search_entry.get()), fg='#129ac7', bg='White', font=('League Spartan', 10, 'bold'), width=10, height=1)
        search_button.pack(pady=(0, 10))

        # propose member
        propose_member_button = tk.Button(self.user_dashboard_window, text="Propose Member", command=self.propose_member, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width=15, height=1)
        propose_member_button.pack(pady=10)

        # tombol kembali
        back_button = tk.Button(self.user_dashboard_window, text="Back", command=self.close_user_dashboard, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width=15, height=1)
        back_button.pack(pady=10)

    def close_user_dashboard(self):
        self.user_dashboard_window.destroy()

    def search_data(self, keyword):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for member in self.members:
            if keyword.lower() in member['Name'].lower() or keyword.lower() in member['Skill'].lower() or keyword.lower() in member['Contact'].lower():
                self.tree.insert("", "end", values=(member['Name'], member['Skill'], member['Contact']))



    # Menambahkan fungsi untuk mengajukan anggota
    def submit_proposed_member(self):
        name = self.name_entry.get()
        skill = self.skill_entry.get()
        contact = self.contact_entry.get()

        if not name or not skill or not contact:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Menyimpan data anggota yang diajukan
        proposed_member = {"Name": name, "Skill": skill, "Contact": contact}
        # Menambahkan data anggota yang diajukan ke dalam list anggota yang diajukan
        self.proposed_members.append(proposed_member)
        messagebox.showinfo("Success", "Member proposed successfully")
        self.propose_member_window.destroy()
        # Kembali ke menu utama
        self.show_user_dashboard(email=None)

    def propose_member(self):
        # Membuat jendela baru untuk mengajukan anggota
        self.propose_member_window = tk.Toplevel(self.root)
        self.propose_member_window.title('Propose Member')
        self.propose_member_window.geometry("400x300")
        self.propose_member_window.configure(bg='#129ac7')

        self.member_label = tk.Label(self.propose_member_window, text='Propose Member', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.member_label.pack(pady=(10, 0))

        # Label untuk "Nama"
        self.name_label = tk.Label(self.propose_member_window, text='Name:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.name_label.pack(pady=(10, 0))
        self.name_entry = tk.Entry(self.propose_member_window, font=('League Spartan', 15))
        self.name_entry.pack(pady=(0, 10))

        # Label untuk "Skill"
        self.skill_label = tk.Label(self.propose_member_window, text='Skill:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.skill_label.pack(pady=(10, 0))
        self.skill_entry = tk.Entry(self.propose_member_window, font=('League Spartan', 15))
        self.skill_entry.pack(pady=(0, 10))

        # Label untuk "Kontak"
        self.contact_label = tk.Label(self.propose_member_window, text='Contact:', fg='white', bg='#129ac7', font=('League Spartan', 20))
        self.contact_label.pack(pady=(10, 0))
        self.contact_entry = tk.Entry(self.propose_member_window, font=('League Spartan', 15))
        self.contact_entry.pack(pady=(0, 10))

        # Tombol untuk mengajukan anggota
        self.propose_button = tk.Button(self.propose_member_window, text='Propose', command=self.submit_proposed_member, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        self.propose_button.pack(pady=(10, 10))

        # Tombol kembali
        self.back_button = tk.Button(self.propose_member_window, text='Back', command=self.close_propose_member_window, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        self.back_button.pack(pady=(0, 10))

    def close_propose_member_window(self):
        self.propose_member_window.destroy()

##Signnnnnnnnn Upppppppp#######################################################
###############################################################################

    def sign_up(self):
        # buat halaman baru
        self.sign_up_window = tk.Toplevel(self.root)
        self.sign_up_window.title('Sign Up')
        self.sign_up_window.geometry("400x300")
        self.sign_up_window.configure(bg='#129ac7')

        self.sign_up_label = tk.Label(self.sign_up_window, text='Register Account', fg='white', bg='#129ac7', font=('League Spartan', 40, 'bold'))
        self.sign_up_label.pack(pady=(10, 0))

        # memilih type akun
        user_type_label = tk.Label(self.sign_up_window, text='Select User Type:', font=('League Spartan', 20), fg='white', bg='#129ac7')
        user_type_label.pack(pady=20)
        self.user_type_var = tk.StringVar(self.sign_up_window)
        self.user_type_var.set('Choose one') 
        user_type_menu = tk.OptionMenu(self.sign_up_window, self.user_type_var, 'Admin', 'User')
        user_type_menu.pack(pady=10)

        # input nama
        Username_label = tk.Label(self.sign_up_window, text='Username:', font=('League Spartan', 20), fg='white', bg='#129ac7' )
        Username_label.pack(pady=10)
        self.Username_entry = tk.Entry(self.sign_up_window, width=20, font=('League Spartan', 15))
        self.Username_entry.pack(pady=10)

        # input email
        email_label = tk.Label(self.sign_up_window, text='Email:', font=('League Spartan', 20), fg='white', bg='#129ac7' )
        email_label.pack(pady=10)
        self.email_entry = tk.Entry(self.sign_up_window, width=20, font=('League Spartan', 15))
        self.email_entry.pack(pady=10)

        # input password
        password_label = tk.Label(self.sign_up_window, text='Password:', font=('League Spartan', 20), fg='white', bg='#129ac7')
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.sign_up_window, width=20, font=('League Spartan', 15), show='*')
        self.password_entry.pack(pady=10)

        # submit
        submit_button = tk.Button(self.sign_up_window, text='Register', command=self.submit_sign_up, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        submit_button.pack(pady=(0, 20))

        # kembali
        back_button = tk.Button(self.sign_up_window, text='Back', command=self.close_sign_up_window, fg='#129ac7', bg='White', font=('League Spartan', 15, 'bold'), width= 15, height= 1)
        back_button.pack(pady=(0, 20))

    def close_sign_up_window(self):
        self.sign_up_window.destroy()

    def submit_sign_up(self):
        user_type = self.user_type_var.get()
        username = self.Username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # mengecek input
        if user_type == 'Choose one':
            messagebox.showerror("Error", "Please select a user type")
            return

        if not email or not password or not username:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if '@' not in email or email.count('@') != 1:
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        self.registered_accounts[email] = {'User Type': user_type, 'Username': username, 'Password': password}
        messagebox.showinfo("Success", "Account successfully registered!")

        # menutup halaman
        self.sign_up_window.destroy()

#######EXITTTTTT#####################################################################
#####################################################################################

    def exit_program(self):
        # Menghentikan program
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = FindTeamApp(root)
    root.mainloop()