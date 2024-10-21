import tkinter as tk

class Board:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.create_widgets()

    def create_widgets(self):
        # Ajouter un label
        self.fenetre.geometry("500x500")
        label = tk.Label(self.fenetre, text="Bataile Navale", font=("Helvetica", 16))
        label.pack()

        buttonframe = tk.Frame(self.fenetre)
        for i in range(10):
            for j in range(10):
                btn1 = tk.Button(buttonframe, text="", height=self.fenetre.winfo_height()*2, width=self.fenetre.winfo_width()*5)
                btn1.grid(row=i, column=j, sticky=tk.W + tk.E)
        buttonframe.pack(padx = (25, 0), fill='x')


    def run(self):
        # Lancer la boucle principale de Tkinter
        self.fenetre.mainloop()



app = Board()
app.run()
