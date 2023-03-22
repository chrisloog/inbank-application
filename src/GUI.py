import tkinter
import loan_decision_engine


def main():
    window = tkinter.Tk()

    window.title("Loan Decision Engine")
    window.geometry('800x400')

    tkinter.Label(window, text='Personal code').grid(row=0)
    tkinter.Label(window, text='Loan amount').grid(row=1)
    tkinter.Label(window, text='Loan period').grid(row=2)
    tkinter.Label(window, text='Result').grid(row=3)

    personal_code = tkinter.Entry(window, width=15)
    personal_code.grid(column=1, row=0)
    personal_code.focus()  # Set focus to entry widget

    loan_amount = tkinter.Entry(window, width=15)
    loan_amount.grid(column=1, row=1)

    loan_period = tkinter.Entry(window, width=15)
    loan_period.grid(column=1, row=2)

    result = tkinter.Entry(window, width=30)
    result.grid(column=1, row=3)

    def clicked():
        p_code = int(personal_code.get())
        l_amount = int(loan_amount.get())
        l_period = int(loan_period.get())
        output = loan_decision_engine.decision_engine(p_code, l_amount, l_period)
        result.insert(0, output)

    btn = tkinter.Button(window, text="Click Me", command=clicked)
    btn.grid(column=1, row=4)

    window.mainloop()


if __name__ == '__main__':
    main()
