import tkinter as tk
from tkinter import ttk
import loan_decision_engine

root = tk.Tk()
root.title("Loan Decision Engine")
root.geometry("400x300")
root.resizable(False, False)
root.configure(background="#F8F8F8")


def submit():
    personal_code = personal_code_entry.get()
    loan_amount = loan_amount_entry.get()
    loan_period = loan_period_entry.get()

    # Check if personal code, loan amount, and loan period are numeric
    if not personal_code.isnumeric() or not loan_amount.isnumeric() or not loan_period.isnumeric():
        decision_field.config(state="normal")
        decision_field.delete("1.0", "end")
        decision_field.insert("end", "Error: Personal code, loan amount, and loan period must be numeric")
        decision_field.config(state="disabled")
    else:
        personal_code = int(personal_code)
        loan_amount = int(loan_amount)
        loan_period = int(loan_period)

        decision_field.config(state="normal")
        decision_field.delete("1.0", "end")
        decision_field.insert("end", loan_decision_engine.decision_engine(personal_code, loan_amount, loan_period))
        decision_field.config(state="disabled")


personal_code_label = ttk.Label(root, text="Personal code:")
personal_code_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
personal_code_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
personal_code_entry.grid(row=0, column=1, padx=10, pady=10)

loan_amount_label = ttk.Label(root, text="Loan amount (€):")
loan_amount_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
loan_amount_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
loan_amount_entry.grid(row=1, column=1, padx=10, pady=10)

loan_period_label = ttk.Label(root, text="Loan period (months):")
loan_period_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")
loan_period_entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
loan_period_entry.grid(row=2, column=1, padx=10, pady=10)

decision_label = ttk.Label(root, text="Decision:")
decision_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")
decision_field = tk.Text(root, height=5, width=30, font=("Helvetica", 12), state="disabled")
decision_field.grid(row=3, column=1, padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=1, padx=10, pady=10)

for i in range(5):
    root.grid_rowconfigure(i, pad=5)
for i in range(2):
    root.grid_columnconfigure(i, pad=5)

root.mainloop()
