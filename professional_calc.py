from tkinter import *


class Professional_calc:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(500, 600)
        self.root.title("Profesjonalny kalkulator")

        self.font = ('Verdana', 15)

        self.main_entry = Entry(self.root, width=45, borderwidth=10)
        self.main_entry.grid(row=0, column=0, columnspan=4)

        self.button1 = Button(self.root, text='1', font=self.font, padx=16, command=lambda: self.button_click(1))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self.root, text='2', font=self.font, padx=16, command=lambda: self.button_click(2))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.root, text='3', font=self.font, padx=16, command=lambda: self.button_click(3))
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.root, text='4', font=self.font, padx=16, command=lambda: self.button_click(4))
        self.button4.grid(row=2, column=0)

        self.button5 = Button(self.root, text='5', font=self.font, padx=16, command=lambda: self.button_click(5))
        self.button5.grid(row=2, column=1)

        self.button6 = Button(self.root, text='6', font=self.font, padx=16, command=lambda: self.button_click(6))
        self.button6.grid(row=2, column=2)

        self.button7 = Button(self.root, text='7', font=self.font, padx=16, command=lambda: self.button_click(7))
        self.button7.grid(row=1, column=0)

        self.button8 = Button(self.root, text='8', font=self.font, padx=16, command=lambda: self.button_click(8))
        self.button8.grid(row=1, column=1)

        self.button9 = Button(self.root, text='9', font=self.font, padx=16, command=lambda: self.button_click(9))
        self.button9.grid(row=1, column=2)

        self.button0 = Button(self.root, text='0', font=self.font, padx=16, command=lambda: self.button_click(0))
        self.button0.grid(row=4, column=0)

        self.button_plus = Button(self.root, text='+', font=self.font, padx=10)
        self.button_plus.grid(row=1, column=3)

        self.button_minus = Button(self.root, text='-', font=self.font, padx=15)
        self.button_minus.grid(row=2, column=3)

        self.button_multiply = Button(self.root, text='*', font=self.font, padx=13)
        self.button_multiply.grid(row=3, column=3)

        self.button_divide = Button(self.root, text='/', font=self.font, padx=16)
        self.button_divide.grid(row=4, column=3)

        self.button_equal = Button(self.root, text='=', font=self.font, padx=13)
        self.button_equal.grid(row=4, column=2)

        self.button_clear = Button(self.root, text='C', font=self.font, padx=15, command=self.clear)
        self.button_clear.grid(row=4, column=1)

    def button_click(self, number):
        current_number = self.main_entry.get()
        self.main_entry.delete(0, END)
        self.main_entry.insert(0, str(current_number) + str(number))

    def clear(self):
        self.main_entry.delete(0, END)
