from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
class Menu(object):
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Pi")
        self.fonte = ("Press Start", 15,)
        self.tela.config(background="black")
        self.tela.geometry("600x600")
        self.texto=Label(self.tela,text="Grafico",font=self.fonte,background="black",foreground="yellow")
        self.fonte=("Press Start", 14)


        self.botaografico = Button(self.tela, text="Grafico de Seno", font=self.fonte, activebackground="black",activeforeground="white", command=self.abrirS, border=8, background="black", foreground="white")
        self.botaoArqui=Button(self.tela, text="Grafico de cos", font=self.fonte, activebackground="black",activeforeground="white", command=self.abrirC, border=8, background="black", foreground="white")

        self.botaografico.grid(row=2,column=2,sticky='EW',columnspan=2)
        self.botaoArqui.grid(row=1,column=2,sticky='EW',columnspan=2)
        self.texto.grid(row=0, column=2, sticky='EW', columnspan=2)

    def rodar(self):
        self.tela.mainloop()
    def abrirS(self):
        tela=Seno()
        tela.rodar()
    def abrirC(self):
        tela=Cos()
        tela.rodar()
class Seno(object):
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Pi")
        self.fonte = ("Press Start", 15,)
        self.tela.config(background="black")
        self.tela.geometry("800x800")

        self.texto = Label(self.tela, text="Sen", font=self.fonte, background="black", foreground="yellow")
        self.texto2 = Label(self.tela, text="A", font=self.fonte, background="black", foreground="yellow")
        self.texto3= Label(self.tela, text="B", font=self.fonte, background="black", foreground="yellow")
        self.texto4 = Label(self.tela, text="M", font=self.fonte, background="black", foreground="yellow")
        self.texto5 = Label(self.tela, text="LIM", font=self.fonte, background="black", foreground="yellow")
        self.texto6 = Label(self.tela, text="a", font=self.fonte, background="black", foreground="yellow")
        self.texto7 = Label(self.tela, text="b", font=self.fonte, background="black", foreground="yellow")

        self.caixa=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.caixa2=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.caixa3=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.caixa4 = Entry(self.tela, font=self.fonte, border=8, background="black", foreground="white")
        self.caixa5= Entry(self.tela, font=self.fonte, border=8, background="black", foreground="white")
        self.resultado=Label(self.tela, text="", font=self.fonte, background="black", foreground="yellow")

        self.botao=Button(self.tela, text="grafico", font=self.fonte, activebackground="black",activeforeground="white", command=self.Grafico, border=8, background="black", foreground="white")
        self.botaoS=Button(self.tela, text="Salva", font=self.fonte, activebackground="black",activeforeground="white", command=self.salvar, border=8, background="black", foreground="white")


        self.texto.grid(row=0,column=2,sticky='EW',columnspan=2)
        self.texto2.grid(row=1,column=0,sticky='EW')
        self.texto3.grid(row=2, column=0, sticky='EW')
        self.texto4.grid(row=3, column=0, sticky='EW')
        self.texto5.grid(row=4, column=2, sticky='EW',columnspan=2)
        self.texto6.grid(row=5, column=0, sticky='EW')
        self.texto7.grid(row=6, column=0, sticky='EW')
        self.resultado.grid(row=7,column=2,sticky='EW',columnspan=2)

        self.caixa.grid(row=1,column=2,sticky='EW',columnspan=1)
        self.caixa2.grid(row=2, column=2, sticky='EW', columnspan=1)
        self.caixa3.grid(row=3, column=2, sticky='EW', columnspan=1)
        self.caixa4.grid(row=5, column=2, sticky='EW', columnspan=1)
        self.caixa5.grid(row=6, column=2, sticky='EW', columnspan=1)
        self.botao.grid(row=8,column=2,sticky='EW',columnspan=2)
        self.botaoS.grid(row=9,column=2,sticky='EW',columnspan=2)
        self.cont=0

    def rodar(self):
        detro = self.caixa.get()
        esqueda = self.caixa2.get()
        direita = self.caixa3.get()
        if (esqueda) == "":
            self.resultado['text'] = f"{esqueda}sen(x){direita}"
        else:
            self.resultado['text'] = f"{esqueda}sen({detro}){direita}"
        self.tela.mainloop()
    def Grafico(self):
        global lista2, lista
        try:
            detro = self.caixa.get()
            esqueda =self.caixa2.get()
            direita = self.caixa3.get()
            limA=self.caixa4.get()
            limB=self.caixa5.get()
            if (detro != ""):
                detro=float(detro)
            if (esqueda != ""):
                esqueda=float(esqueda)
            else:
                esqueda=0
            if (direita != ""):
                direita=float(direita)
            else:
                direita=0
            if (limA !=""):
                limA=str(limA)
            else:
                limA=0
            if (limB != ""):
                limB = str(limB)
            else:
                limB=6
            lista = []
            lista2 = []
            print(limA,limB)
            if(detro==""):
                limA = str(limA)
                limB = str(limB)
                if(limA!=""and limA.isdigit() == True and limB.isdigit() == True):
                    limA=float(limA)
                    limB=float(limB)
                    self.resultado['text'] = f"{esqueda}sen(x){direita}"
                    plt.title(f"{esqueda}sen(x){direita}")
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    for x in np.arange(limA, limB, 0.01):
                        if(direita<0):
                            lista.append(x)
                            xx = esqueda*np.sin(x)-direita
                            lista2.append(xx)
                        else:
                            lista.append(x)
                            xx = esqueda * np.sin(x) + direita
                            lista2.append(xx)
                    plt.plot(lista, lista2)
                    plt.show()

            else:
                limA = str(limA)
                limB = str(limB)
                print(limB.isdigit())
                if (limA != "" and limA.isdigit() == True and limB.isdigit() == True):
                    limA = float(limA)
                    limB = float(limB)
                    limB=6.28
                    self.resultado['text'] = f"{esqueda}sen({detro}){direita}"
                    plt.title(f"{esqueda}sen({detro}){direita}")
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    re=limB/detro
                    for x in np.arange(limA,re, 0.01):
                        if (direita < 0):
                            lista.append(x)
                            xx = esqueda * np.sin(2*x) - direita
                            lista2.append(xx)
                        else:
                            lista.append(x)
                            xx = esqueda * np.sin(2*x) + direita
                            lista2.append(xx)
                    plt.plot(lista, lista2)
                    plt.show()
        except ValueError:
            erro=ValueError
            self.resultado['text']=f"{erro}"
    def salvar(self):
        self.cont = self.cont+1
        self.Grafico()
        plt.savefig(f'{self.cont}.png')
class Cos(object):
    def __init__(self):
        self.tela = Tk()
        self.tela.title("Pi")
        self.fonte = ("Press Start", 15,)
        self.tela.config(background="black")
        self.tela.geometry("800x800")

        self.texto = Label(self.tela, text="Cos", font=self.fonte, background="black", foreground="yellow")
        self.texto2 = Label(self.tela, text="A", font=self.fonte, background="black", foreground="yellow")
        self.texto3= Label(self.tela, text="B", font=self.fonte, background="black", foreground="yellow")
        self.texto4 = Label(self.tela, text="M", font=self.fonte, background="black", foreground="yellow")
        self.texto5 = Label(self.tela, text="LIM", font=self.fonte, background="black", foreground="yellow")
        self.texto6 = Label(self.tela, text="a", font=self.fonte, background="black", foreground="yellow")
        self.texto7 = Label(self.tela, text="b", font=self.fonte, background="black", foreground="yellow")

        self.caixa=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.caixa2=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.caixa3=Entry(self.tela,font=self.fonte,border=8,background="black",foreground="white")
        self.caixa4 = Entry(self.tela, font=self.fonte, border=8, background="black", foreground="white")
        self.caixa5= Entry(self.tela, font=self.fonte, border=8, background="black", foreground="white")
        self.resultado=Label(self.tela, text="", font=self.fonte, background="black", foreground="yellow")

        self.botao=Button(self.tela, text="grafico", font=self.fonte, activebackground="black",activeforeground="white", command=self.Grafico, border=8, background="black", foreground="white")
        self.botaoS=Button(self.tela, text="Salva", font=self.fonte, activebackground="black",activeforeground="white", command=self.salvar, border=8, background="black", foreground="white")


        self.texto.grid(row=0,column=2,sticky='EW',columnspan=2)
        self.texto2.grid(row=1,column=0,sticky='EW')
        self.texto3.grid(row=2, column=0, sticky='EW')
        self.texto4.grid(row=3, column=0, sticky='EW')
        self.texto5.grid(row=4, column=2, sticky='EW',columnspan=2)
        self.texto6.grid(row=5, column=0, sticky='EW')
        self.texto7.grid(row=6, column=0, sticky='EW')
        self.resultado.grid(row=7,column=2,sticky='EW',columnspan=2)

        self.caixa.grid(row=1,column=2,sticky='EW',columnspan=1)
        self.caixa2.grid(row=2, column=2, sticky='EW', columnspan=1)
        self.caixa3.grid(row=3, column=2, sticky='EW', columnspan=1)
        self.caixa4.grid(row=5, column=2, sticky='EW', columnspan=1)
        self.caixa5.grid(row=6, column=2, sticky='EW', columnspan=1)
        self.botao.grid(row=8,column=2,sticky='EW',columnspan=2)
        self.botaoS.grid(row=9,column=2,sticky='EW',columnspan=2)
        self.cont=0

    def rodar(self):
        detro = self.caixa.get()
        esqueda = self.caixa2.get()
        direita = self.caixa3.get()
        if (esqueda) == "":
            self.resultado['text'] = f"{esqueda}cos(x){direita}"
        else:
            self.resultado['text'] = f"{esqueda}cos({detro}){direita}"
        self.tela.mainloop()
    def Grafico(self):
        global lista2, lista
        try:
            detro = self.caixa.get()
            esqueda =self.caixa2.get()
            direita = self.caixa3.get()
            limA=self.caixa4.get()
            limB=self.caixa5.get()
            if (detro != ""):
                detro=float(detro)
            if (esqueda != ""):
                esqueda=float(esqueda)
            else:
                esqueda=0
            if (direita != ""):
                direita=float(direita)
            else:
                direita=0
            if (limA !=""):
                limA=str(limA)
            else:
                limA=0
            if (limB != ""):
                limB = str(limB)
            else:
                limB=6.28
            lista = []
            lista2 = []
            if(detro==""):
                limA = str(limA)
                limB = str(limB)
                if(limA!=""and limA.isdigit() == True and limB.isdigit() == True):
                    limA=float(limA)
                    limB=float(limB)
                    self.resultado['text'] = f"{esqueda}cos(x){direita}"
                    plt.title(f"{esqueda}cos(x){direita}")
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    for x in np.arange(limA, limB, 0.01):
                        if(direita<0):
                            lista.append(x)
                            xx = esqueda*np.cos(x)-direita
                            lista2.append(xx)
                        else:
                            lista.append(x)
                            xx = esqueda * np.cos(x) + direita
                            lista2.append(xx)
                    plt.plot(lista, lista2)
                    plt.show()

            else:
                limA = str(limA)
                limB = str(limB)
                if (limA != "" and limA.isdigit() == True and limB.isdigit() == True):
                    limA = float(limA)
                    limB = float(limB)
                    limB=6.28
                    self.resultado['text'] = f"{esqueda}cos({detro}){direita}"
                    plt.title(f"{esqueda}cos({detro}){direita}")
                    plt.xlabel("X")
                    plt.ylabel("Y")
                    re=limB/detro
                    print(re)
                    for x in np.arange(limA,re, 0.01):
                        print(x)
                        if (direita < 0):
                            lista.append(x)
                            xx = esqueda * np.cos(2*x) - direita
                            lista2.append(xx)
                        else:
                            lista.append(x)
                            xx = esqueda * np.cos(2*x) + direita
                            lista2.append(xx)
                    plt.plot(lista, lista2)
                    plt.show()
        except ValueError:
            erro=ValueError
            self.resultado['text']=f"{erro}"
    def salvar(self):
        self.cont = self.cont+1
        self.Grafico()
        plt.savefig(f'{self.cont}.png')
