from tkinter import *
from normal_calc import Normal_calc
from professional_calc import Professional_calc
from horner_scheme import Horner_scheme


win = Tk()
win.minsize(300, 250)
win.maxsize(300, 250)
win.title("Kalkulator maturzysty")

big_font = ("Verdana", 19)
small_font = ("Verdana", 10)

title = Label(win, text=" Kalkulator maturzysty", font=big_font)
title.grid(row=0, column=0, columnspan=3)

label_pass = Label(win, text=" ")
label_pass.grid(row=1, column=1)

button_normal_calc = Button(win, text="Prosty kalkulator", command=Normal_calc, padx=32, pady=4, font=small_font)
button_normal_calc.grid(row=2, column=1)

label_pass1 = Label(win, text=" ")
label_pass1.grid(row=3, column=1)

button_professional_calc = Button(win, text='Profesjonalny kalkulator ', command=Professional_calc, padx=6, pady=4, font=small_font)
button_professional_calc.grid(row=4, column=1)

label_pass2 = Label(win, text=" ")
label_pass2.grid(row=5, column=1)

button_horner_scheme = Button(win, text=' Schemat Hornera', command=Horner_scheme, padx=27, pady=4, font=small_font)
button_horner_scheme.grid(row=6, column=1)

win.mainloop()