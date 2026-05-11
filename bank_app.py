from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
import random
accounts, employees = {}, {}
bank_data = {
    "SBI": [("Suraram", "SBIN001"), ("Banjara Hills", "SBIN002")],
    "HDFC": [("KPHB", "HDFC001")],
    "ICICI": [("Alwal", "ICIC001")],
    "AXIS": [("Isnapur", "AXIS001")]
}
def generate_account_number():
    while True:
        acc = random.randint(1000000000, 9999999999)
        if acc not in accounts:
            return acc
def clear_root():
    for w in a.winfo_children():
        w.destroy()
def show_main():
    clear_root()
    Label(a, text=" ASTM BANKHUB ", font=("Arial", 36, "bold")).grid(row=0, column=0, columnspan=9, pady=40)
    Button(a, text="Create Account", command=create_account, width=30, font=("Arial", 14)).grid(row=1, column=4, pady=10)
    Button(a, text="Transfer/Deposit/View", command=account_ops, width=30, font=("Arial", 14)).grid(row=2, column=4, pady=10)
    Button(a, text="Employee Login", command=employee_login_menu, width=30, font=("Arial", 14)).grid(row=3, column=4, pady=10)
def create_account():
    clear_root()
    Label(a, text="Create Account", font=("Arial", 28)).grid(row=0, column=4, pady=20)
    entries = {}
    for i, text in enumerate(["Full Name", "Mobile"]):
        Label(a, text=text, font=("Arial", 12)).grid(row=i+1, column=3, sticky=W, padx=5, pady=2)
        entries[text] = Entry(a, font=("Arial", 12))
        entries[text].grid(row=i+1, column=4, pady=2)
    Label(a, text="Account Type", font=("Arial", 12)).grid(row=3, column=3, sticky=W)
    acc_type = StringVar()
    acc_menu = ttk.Combobox(a, textvariable=acc_type, values=["Saving", "Current"], state="readonly", font=("Arial", 12))
    acc_menu.grid(row=3, column=4)
    Label(a, text="Address", font=("Arial", 12)).grid(row=4, column=3, sticky=W)
    entries["Address"] = Entry(a, font=("Arial", 12))
    entries["Address"].grid(row=4, column=4)
    photo_path = StringVar()
    def browse_photo():
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if file:
            photo_path.set(file)
    Button(a, text="Upload Photo", command=browse_photo, font=("Arial", 12)).grid(row=5, column=3, sticky=W)
    Label(a, textvariable=photo_path, font=("Arial", 10)).grid(row=5, column=4, sticky=W)
    bank_cb, branch_cb = StringVar(), StringVar()
    Label(a, text="Bank", font=("Arial", 12)).grid(row=6, column=3, sticky=W)
    bank_menu = ttk.Combobox(a, textvariable=bank_cb, values=list(bank_data), state="readonly", font=("Arial", 12))
    bank_menu.grid(row=6, column=4)
    Label(a, text="Branch - IFSC", font=("Arial", 12)).grid(row=7, column=3, sticky=W)
    branch_menu = ttk.Combobox(a, textvariable=branch_cb, state="readonly", font=("Arial", 12))
    branch_menu.grid(row=7, column=4)
    def update_branch(_):
        branch_menu['values'] = [f"{b} - {i}" for b, i in bank_data[bank_cb.get()]]
    bank_menu.bind("<<ComboboxSelected>>", update_branch)
    def submit():
        name = entries["Full Name"].get()
        mobile = entries["Mobile"].get()
        atype = acc_type.get()
        addr = entries["Address"].get()
        bank, branch_info = bank_cb.get(), branch_cb.get()
        if not all([name, mobile, atype, addr, bank, branch_info]) or not mobile.isdigit():
            return messagebox.showerror("Error", "All fields must be filled correctly.")
        branch, ifsc = branch_info.split(" - ")
        acc_no = generate_account_number()
        balance = 1000 if atype == "Saving" else 10000
        accounts[acc_no] = {
            "name": name, "mobile": mobile, "type": atype, "address": addr,
            "photo": photo_path.get(), "bank": bank, "branch": branch,
            "ifsc": ifsc, "balance": balance
        }
        msg = f"Account created!\n\nUser Full Name: {name}\nMobile No: {mobile}\nAddress: {addr}\nAccount Type: {atype}\nAccount Number: {acc_no}\nBank: {bank} - {branch}\nBalance: ₹{balance}"
        messagebox.showinfo("Success", msg)
        show_main()
    Button(a, text="Submit", command=submit, font=("Arial", 12)).grid(row=8, column=4, pady=10)
    Button(a, text="Back", command=show_main, font=("Arial", 12)).grid(row=8, column=3, pady=10)
def account_ops():
    clear_root()
    Label(a, text="Transfer/Deposit/View", font=("Arial", 24)).grid(row=0, column=4, pady=20)
    Label(a, text="Your Account No:", font=("Arial", 12)).grid(row=1, column=3, sticky=W)
    acc_entry = Entry(a, font=("Arial", 12)); acc_entry.grid(row=1, column=4)
    Label(a, text="Receiver A/C:", font=("Arial", 12)).grid(row=2, column=3, sticky=W)
    recv_entry = Entry(a, font=("Arial", 12)); recv_entry.grid(row=2, column=4)
    Label(a, text="Amount:", font=("Arial", 12)).grid(row=3, column=3, sticky=W)
    amt_entry = Entry(a, font=("Arial", 12)); amt_entry.grid(row=3, column=4)
    def deposit():
        try:
            acc, amt = int(acc_entry.get()), float(amt_entry.get())
            if acc in accounts and amt > 0:
                accounts[acc]['balance'] += amt
                messagebox.showinfo("Success", f"₹{amt} deposited")
        except:
            messagebox.showerror("Error", "Invalid input")
    def transfer():
        try:
            s, r, a = int(acc_entry.get()), int(recv_entry.get()), float(amt_entry.get())
            if s in accounts and r in accounts and accounts[s]['balance'] >= a > 0:
                accounts[s]['balance'] -= a
                accounts[r]['balance'] += a
                messagebox.showinfo("Success", f"₹{a} transferred")
            else:
                messagebox.showerror("Error", "Check balance or details")
        except:
            messagebox.showerror("Error", "Invalid input")
    def view():
        try:
            acc = int(acc_entry.get())
            a_data = accounts.get(acc)
            if a_data:
                info = f"{acc}\n{a_data['name']}, {a_data['bank']}, {a_data['branch']}\n₹{a_data['balance']}"
                messagebox.showinfo("Details", info)
        except:
            messagebox.showerror("Error", "Invalid account")
    Button(a, text="Deposit", command=deposit, font=("Arial", 12)).grid(row=4, column=3, pady=5)
    Button(a, text="Transfer", command=transfer, font=("Arial", 12)).grid(row=4, column=4)
    Button(a, text="View", command=view, font=("Arial", 12)).grid(row=5, column=3, pady=5)
    Button(a, text="Back", command=show_main, font=("Arial", 12)).grid(row=5, column=4)
def employee_login_menu():
    clear_root()
    Label(a, text="Employee Login", font=("Arial", 24)).grid(row=0, column=4, pady=20)
    Button(a, text="New Employee", command=new_employee, font=("Arial", 12)).grid(row=1, column=4, pady=5)
    Button(a, text="Existing Employee", command=existing_employee, font=("Arial", 12)).grid(row=2, column=4, pady=5)
    Button(a, text="Back", command=show_main, font=("Arial", 12)).grid(row=3, column=4, pady=5)
def new_employee():
    clear_root()
    Label(a, text="Register Employee", font=("Arial", 24)).grid(row=0, column=4, pady=20)
    Label(a, text="Full Name", font=("Arial", 12)).grid(row=1, column=3, sticky=W)
    name = Entry(a, font=("Arial", 12)); name.grid(row=1, column=4)
    Label(a, text="Employee ID", font=("Arial", 12)).grid(row=2, column=3, sticky=W)
    emp_id = Entry(a, font=("Arial", 12)); emp_id.grid(row=2, column=4)
    Label(a, text="Bank", font=("Arial", 12)).grid(row=3, column=3, sticky=W)
    bank = StringVar()
    bank_menu = ttk.Combobox(a, textvariable=bank, values=list(bank_data), state="readonly", font=("Arial", 12))
    bank_menu.grid(row=3, column=4)
    def save():
        if name.get() and emp_id.get() and bank.get():
            employees[emp_id.get()] = {"name": name.get(), "bank": bank.get()}
            messagebox.showinfo("Success", "Employee Registered")
            show_main()
        else:
            messagebox.showerror("Error", "All fields required")
    Button(a, text="Register", command=save, font=("Arial", 12)).grid(row=4, column=4, pady=10)
    Button(a, text="Back", command=employee_login_menu, font=("Arial", 12)).grid(row=4, column=3)
def existing_employee():
    clear_root()
    Label(a, text="Employee Access", font=("Arial", 20)).grid(row=0, column=4, pady=20)
    Label(a, text="Enter Employee ID", font=("Arial", 12)).grid(row=1, column=3, sticky=W)
    emp_id = Entry(a, font=("Arial", 12)); emp_id.grid(row=1, column=4)

    def view_users():
        eid = emp_id.get()
        if eid in employees:
            bank = employees[eid]["bank"]
            clear_root()
            Label(a, text=f"{bank} Users", font=("Arial", 16)).grid(row=0, column=4, pady=5)
            r = 1
            for acc, data in accounts.items():
                if data["bank"] == bank:
                    Label(a, text=f"{acc}: {data['name']} | {data['branch']} | ₹{data['balance']}", font=("Arial", 12)).grid(row=r, column=4, sticky=W)
                    r += 1
            Button(a, text="Back", command=show_main, font=("Arial", 12)).grid(row=r+1, column=4, pady=10)
        else:
            messagebox.showerror("Error", "Invalid ID")

    Button(a, text="View Accounts", command=view_users, font=("Arial", 12)).grid(row=2, column=4, pady=5)
    Button(a, text="Back", command=employee_login_menu, font=("Arial", 12)).grid(row=3, column=4)

a = Tk()
a.title(" ASTM BANKHUB ")
a.geometry("700x650")
show_main()
a.mainloop()