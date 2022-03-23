#!/usr/bin/env python3



import pylab as pl
import tkinter as tk

from pylab import linspace, pi, plot,sin,cos, show,grid,legend
from os.path import basename, splitext
from tkinter import *



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Grafy"

    def __init__(self):

        super().__init__(className=self.name)

        self.var_entryKonec = tk.IntVar()
        self.var_entryStart = tk.IntVar()
        self.var_entryF = tk.IntVar()
        self.var_entryA = tk.IntVar()       
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Grafy")
        self.lbl.pack()
        self.btnVypsat = tk.Button(self, text="Načíst ze souboru", command=self.zeSouboru)
        self.btnVypsat.pack()
        self.lbl1 = tk.Label(self, text="Počáteční čas")
        self.lbl1.pack()
        self.entryStart  = tk.Entry(self, textvariable = self.var_entryStart)
        self.entryStart.pack()
        self.lbl2 = tk.Label(self, text="koncový čas")
        self.lbl2.pack()
        self.entryKonec  = tk.Entry(self, textvariable = self.var_entryKonec)
        self.entryKonec.pack()
        self.lbl3 = tk.Label(self, text="Frekvence")
        self.lbl3.pack()
        self.entryF  = tk.Entry(self, textvariable = self.var_entryF)
        self.entryF.pack()
        self.lbl4 = tk.Label(self, text="Amplituda")
        self.lbl4.pack()
        self.entryA  = tk.Entry(self, textvariable = self.var_entryA)
        self.entryA.pack()
        self.btnGraf = tk.Button(self, text="Načíst graf", command=self.graf)
        self.btnGraf.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()
        

    def about(self):
        window = About(self)
        window.grab_set()

    def quit(self, event=None):
        super().quit()
    
    def graf(self):
        self.f = self.var_entryF.get()
        self.a = self.var_entryA.get()
        self.k = self.var_entryKonec.get()
        self.s = self.var_entryStart.get()
        t = pl.linspace(self.s, 10/self.f, self.f*10000)
        y = self.a * (pl.cos(2*pi*self.f*t ))
        pl.plot(t,y)

        pl.title("výkon")
        pl.xlabel("t[s]")
        pl.ylabel("u[V],i[A], p[W]")
        pl.show()

    def zeSouboru(self):
        f = open("soubor-win.txt", "r")
        x = []
        y = []
        while 1:
            radek = f.readline()
            if radek =="":
                break
            cisla = radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        f.close()
        pl.figure()
        pl.plot(x,y)
        pl.grid(True)
        pl.show()


app = Application()
app.mainloop()