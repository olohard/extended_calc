from tkinter import *


class Normal_calc:
    def __init__(self):
        self.root = Tk()

        self.root.minsize(291, 280)
        self.root.maxsize(291, 280)
        self.root.title("Klasyczny kalkulator")

        self.font = ('Verdana', 22)

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

        self.button_plus = Button(self.root, text='+', font=self.font, padx=10, command=self.addition)
        self.button_plus.grid(row=1, column=3)

        self.button_minus = Button(self.root, text='-', font=self.font, padx=15, command=self.subtraction)
        self.button_minus.grid(row=2, column=3)

        self.button_multiply = Button(self.root, text='*', font=self.font, padx=13, command=self.multiplication)
        self.button_multiply.grid(row=3, column=3)

        self.button_divide = Button(self.root, text='/', font=self.font, padx=16, command=self.division)
        self.button_divide.grid(row=4, column=3)

        self.button_equal = Button(self.root, text='=', font=self.font, padx=13, command=self.equasion)
        self.button_equal.grid(row=4, column=2)

        self.button_clear = Button(self.root, text='C', font=self.font, padx=15, command=self.clear)
        self.button_clear.grid(row=4, column=1)

    def button_click(self, number):
        current_number = self.main_entry.get()
        self.main_entry.delete(0, END)
        self.main_entry.insert(0, str(current_number) + str(number))

    def clear(self):
        self.main_entry.delete(0, END)

    def addition(self):
        global first_number
        first_number = int(self.main_entry.get())

        global math
        math = 'add'

        self.main_entry.delete(0, END)

    def subtraction(self):
        global first_number
        first_number = int(self.main_entry.get())

        global math
        math = 'subtract'

        self.main_entry.delete(0, END)

    def multiplication(self):
        global first_number
        first_number = int(self.main_entry.get())

        global math
        math = 'multiplicate'

        self.main_entry.delete(0, END)

    def division(self):
        global first_number
        first_number = int(self.main_entry.get())

        global math
        math = 'divide'

        self.main_entry.delete(0, END)

    def equasion(self):
        second_number = self.main_entry.get()
        self.main_entry.delete(0, END)

        if math == "add":
            self.main_entry.insert(0, first_number + int(second_number))

        if math == "subtract":
            self.main_entry.insert(0, first_number - int(second_number))

        if math == "multiplicate":
            self.main_entry.insert(0, first_number * int(second_number))

        if math == "divide":
            self.main_entry.insert(0, first_number / int(second_number))
            
