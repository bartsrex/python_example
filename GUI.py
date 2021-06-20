import tkinter as tk
from Data import Stan, Ksiazka

class Window():

    def __init__(self):
        self.stan = Stan()
        self.result = '0'

    def initWindow(self):
        window = tk.Tk()

        title = tk.Label(master=window,text='Witaj w bibliotece!')
        book_no_label = tk.Label(master=window,text="Podaj numer katalogowy ksiazki")
        self.book_no_entry = tk.Entry(master=window)
        spr_na_stanie = tk.Button(master=window,text="Sprawdź na stanie", command=self.spr_stan())
        dodaj = tk.Button(master=window,text="Dodaj do katalogu", command=self.dodaj_do_stanu())
        result = tk.Label(master=window, text=self.result)

        title.pack()
        book_no_label.pack()
        self.book_no_entry.pack()
        spr_na_stanie.pack()
        dodaj.pack()
        result.pack()

        window.mainloop()

    def dodaj_do_stanu(self):
        nr_kat = self.book_no_entry.get()
        res = Stan.dodaj_do_stanu(self.stan, nr_kat)
        if res:
            self.result = "Dodano do stanu"
        else:
            self.result = "Już na stanie"

    def spr_stan(self):
        nr_kat = self.book_no_entry.get()
        res = Stan.spr_czy_na_stanie(self.stan, nr_kat)
        self.result = str(res)
