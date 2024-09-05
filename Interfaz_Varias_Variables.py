from tkinter import *
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from math import sin, pi 


def integrantes():
    messagebox.showinfo('Integrantes',"""
*John Rodríguez V.
""")


def ventana1():
    root=Tk()
    root.title("Cálulo aproximado de la Ventana de Viviani")
    root.geometry("900x300")
    root.config(bg="azure2")
    root.config(bd=10)
    root.config(relief="groove")
    #root.iconbitmap('ESPOL_icono.ico')


    textovent2="""A continuación podrá aproximar la longitud de arco de la ventana de Viviani
con el uso de sumatoria de Riemann, definiendo la cantidad de subintervalos de la sumatoria """
    Label(root,text=textovent2,font=('Franklin Gothic Demi',15)).place(x=30,y=25)

    advertenci1='*Obs. si digita una cantidad muy grande de subintervalos (mayor a 10000000) puede tardar en hacer el cálculo '
    Label(root,text=advertenci1,font=('Franklin Gothic Demi',10)).place(x=50,y=250)

    subintervalo=StringVar()    
    subinter=Entry(root,textvariable=subintervalo)
    subinter.place(x=183,y=120)
    
    
    cantidadsubLabel=Label(root, text='Cantidad de susbintervalos:')
    cantidadsubLabel.place(x=30,y=120)

    
    def f(x):
        return 2*(5/(2**(1/2)))*(3+sin(x))**(1/2)
    
    def CalculoLongitud():
        po= 0
        pf= 2*pi
        n= float(subinter.get())
        delta_x= (po-pf)/n
        i= 0
        longitud=0
        while(i<=(n+1)):
            longitud=f(pf+delta_x*i)*delta_x+longitud
            i=i+1
        messagebox.showinfo("Resultado","El resultado es: "+str(abs(longitud))+" centímetros")
            
    botoncalculo = Button(root, text='Calcular',command=CalculoLongitud).place(x=312,y=118)


    root.mainloop()
 

def grafica():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    t=np.linspace(0,2*np.pi,100)   
    X = 5*np.cos(t)
    Y = 5*np.sin(t)+5
    Z = (-10)*(((1-np.sin(t))/2)**(1/2))
    X1 = 5*np.cos(t)
    Y1 = 5*np.sin(t)+5
    Z1 = (10)*(((1-np.sin(t))/2)**(1/2))
    ax.plot(X1,Y1,Z1, label='curva parametrizada')
    ax.plot(X,Y,Z, label='curva parametrizada')
    ax.legend()
    plt.show()

    
    
raiz = Tk()
raiz.title("Proyecto de Cálculo de Varias Variables")
raiz.geometry("400x450")
raiz.config(bg="azure2")
raiz.config(bd=10)
raiz.config(relief="groove")

#raiz.iconbitmap('ESPOL_icono.ico')

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)
infoMenu = Menu(barraMenu,tearoff=0)
infoMenu.add_command(label='Integrantes',command=integrantes)

barraMenu.add_cascade(label='Info',menu=infoMenu)
    

#imagen3=PhotoImage(file='ESPOL_Logo.png')
#Label(raiz,image=imagen3).place(x=88,y=20)


titulo = 'Bienvenido Usuario'
Label(raiz,text=titulo,font=('Franklin Gothic Demi',15)).place(x=100,y=220)


botonperimetro = Button(raiz, text="""Cálculo aproximado de la longitud
de arco de la ventana de Viviani""",font=('Franklin Gothic Demi',15),command=ventana1).place(x=30,y=280)
botongrafica = Button(raiz,text="""Gráfica de la Ventana de Viviani""",font=('Franklin Gothic Demi',15),command=grafica).place(x=40,y=365)


raiz.mainloop()
