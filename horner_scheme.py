from tkinter import *


class Horner_scheme:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(400, 200)
        self.root.title('Schemat Hornera')

        self.main_label = Label(self.root, text="Ile ten wielomian ma współczynników(3-5): ")
        self.main_label.grid(row=0, column=0)

        self.main_entry = Entry(self.root)
        self.main_entry.grid(row=0, column=1)

        enter_button1 = Button(self.root, text="Enter", command=lambda: self.printing_factors())
        enter_button1.grid(row=0, column=2)

    # TODO Poprawić to całe żeby działało

    def computing_when_3(self, a, b, c, q):
        first_result = a

        f = q * first_result
        second_result = b + f

        g = q * second_result
        third_result = c + g

        results = [first_result, second_result, third_result]
        result_label = Label(self.root, text=results)
        result_label.grid(row=5, column=1)

    def computing_when_4(self, a, b, c, d, q):
        first_result = a

        f = q * first_result
        second_result = b + f

        g = q * second_result
        third_result = c + g

        h = q * third_result
        fourth_result = d + h

        results = [first_result, second_result, third_result, fourth_result]
        result_label = Label(self.root, text=results)
        result_label.grid(row=6, column=1)

    def computing_when_5(self, a, b, c, d, e, q):
        first_result = a

        f = q * first_result
        second_result = b + f

        g = q * second_result
        third_result = c + g

        h = q * third_result
        fourth_result = d + h

        i = q * fourth_result
        fifth_result = e + i

        results = [first_result, second_result, third_result, fourth_result, fifth_result]
        result_label = Label(self.root, text=results)
        result_label.grid(row=7, column=1)

    def printing_factors(self):
        number = int(self.main_entry.get())

        if number == 3:
            label2 = Label(self.root, text="Przez jaki pierwiastek bedziesz dzielić: ")
            label2.grid(row=4, column=0)

            e2 = Entry(self.root, width=7, borderwidth=1)
            e2.grid(row=4, column=1)

            enter_button2 = Button(self.root, text="Enter", command=lambda: self.computing_when_3(
                int(ex2.get()),
                int(ex.get()),
                int(e_free.get()),
                int(e2.get())))

            enter_button2.grid(row=4, column=2)

            result = Label(self.root, text="Wynik:")
            result.grid(row=5, column=0)

            label3a = Label(self.root, text="Podaj pierwszy współczynnik:")
            label3a.grid(row=1, column=0)

            label3b = Label(self.root, text="Podaj drugi współczynnik:")
            label3b.grid(row=2, column=0)

            label3c = Label(self.root, text="Podaj wyraz wolny:")
            label3c.grid(row=3, column=0)

            labelx2 = Label(self.root, text="x^2")
            labelx2.grid(row=1, column=2)

            labelx = Label(self.root, text="x")
            labelx.grid(row=2, column=2)

            ex2 = Entry(self.root, width=7, borderwidth=1)
            ex2.grid(row=1, column=1)

            ex = Entry(self.root, width=7, borderwidth=1)
            ex.grid(row=2, column=1)

            e_free = Entry(self.root, width=7, borderwidth=1)
            e_free.grid(row=3, column=1)


        elif number == 4:
            label2 = Label(self.root, text="Przez jaki pierwiastek bedziesz dzielić: ")
            label2.grid(row=5, column=0)

            e2 = Entry(self.root, width=7, borderwidth=1)
            e2.grid(row=5, column=1)

            enter_button2 = Button(self.root, text="Enter", command=lambda: self.computing_when_4(
                int(ex3.get()),
                int(ex2.get()),
                int(ex.get()),
                int(e_free.get()),
                int(e2.get())))

            enter_button2.grid(row=5, column=2)

            result = Label(self.root, text="Wynik:")
            result.grid(row=6, column=0)

            label3 = Label(self.root, text="Podaj pierwszy współczynnik:")
            label3.grid(row=1, column=0)

            label3a = Label(self.root, text="Podaj drugi współczynnik:")
            label3a.grid(row=2, column=0)

            label3b = Label(self.root, text="Podaj trzeci współczynnik:")
            label3b.grid(row=3, column=0)

            label3c = Label(self.root, text="Podaj wyraz wolny:")
            label3c.grid(row=4, column=0)

            labelx3 = Label(self.root, text="x^3")
            labelx3.grid(row=1, column=2)

            labelx2 = Label(self.root, text="x^2")
            labelx2.grid(row=2, column=2)

            labelx = Label(self.root, text="x")
            labelx.grid(row=3, column=2)

            ex3 = Entry(self.root, width=7, borderwidth=1)
            ex3.grid(row=1, column=1)

            ex2 = Entry(self.root, width=7, borderwidth=1)
            ex2.grid(row=2, column=1)

            ex = Entry(self.root, width=7, borderwidth=1)
            ex.grid(row=3, column=1)

            e_free = Entry(self.root, width=7, borderwidth=1)
            e_free.grid(row=4, column=1)


        elif number == 5:
            label2 = Label(self.root, text="Przez jaki pierwiastek bedziesz dzielić: ")
            label2.grid(row=6, column=0)

            e2 = Entry(self.root, width=7, borderwidth=1)
            e2.grid(row=6, column=1)

            enter_button2 = Button(self.root, text="Enter", command=lambda: self.computing_when_5(
                int(ex4.get()),
                int(ex3.get()),
                int(ex2.get()),
                int(ex.get()),
                int(e_free.get()),
                int(e2.get())))

            enter_button2.grid(row=6, column=2)

            result = Label(self.root, text="Wynik:")
            result.grid(row=7, column=0)

            label3 = Label(self.root, text="Podaj pierwszy współczynnik:")
            label3.grid(row=1, column=0)

            label3a = Label(self.root, text="Podaj drugi współczynnik:")
            label3a.grid(row=2, column=0)

            label3b = Label(self.root, text="Podaj trzeci współczynnik:")
            label3b.grid(row=3, column=0)

            label3c = Label(self.root, text="Podaj czwarty współczynnik:")
            label3c.grid(row=4, column=0)

            label3d = Label(self.root, text="Podaj wyraz wolny:")
            label3d.grid(row=5, column=0)

            labelx4 = Label(self.root, text="x^4")
            labelx4.grid(row=1, column=2)

            labelx3 = Label(self.root, text="x^3")
            labelx3.grid(row=2, column=2)

            labelx2 = Label(self.root, text="x^2")
            labelx2.grid(row=3, column=2)

            labelx = Label(self.root, text="x")
            labelx.grid(row=4, column=2)

            ex4 = Entry(self.root, width=7, borderwidth=1)
            ex4.grid(row=1, column=1)

            ex3 = Entry(self.root, width=7, borderwidth=1)
            ex3.grid(row=2, column=1)

            ex2 = Entry(self.root, width=7, borderwidth=1)
            ex2.grid(row=3, column=1)

            ex = Entry(self.root, width=7, borderwidth=1)
            ex.grid(row=4, column=1)

            e_free = Entry(self.root, width=7, borderwidth=1)
            e_free.grid(row=5, column=1)

        else:
            error_label = Label(self.root,
                                text="Przykro mi. W tym kalkulatorze nie będziesz w stanie obliczyć takiego równania")
            error_label.grid(row=1, column=0, columnspan=3)
