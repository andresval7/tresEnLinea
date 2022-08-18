from email.utils import collapse_rfc2231_value
from tkinter import *
from tkinter import ttk
import numpy as np
 
class TresEnLinea():
 
    def __init__(self):  
        self.raiz = Tk()
        self.raiz.geometry('700x900')
        self.raiz.configure(bg = 'beige')
        self.raiz.title('Tres en Linea Andres Vallejo')
        self.marco1 = ttk.Frame(self.raiz, borderwidth=2, relief="raised", padding=(10,10))
        self.marco2 = ttk.Frame(self.raiz, borderwidth=2, relief="raised", padding=(10,10))
        self.marco3 = ttk.Frame(self.raiz, borderwidth=2, relief="raised", padding=(10,10))
        self.label1 = ttk.Label(self.marco1, text="Juego tres en Linea", font =("Arial ",30), padding =(5,5))
        #Se declara las variables globales de los puntajes de los jugadores 1 y 2.
        
        self.puntajeJ1 = 0
        self.puntajeJ2 = 0
        self.labelJ1 = ttk.Label(self.marco1, text ="Jugador 1: "+str(self.puntajeJ1), font =("Arial ",24), padding =(5,5))
        self.labelJ2 = ttk.Label(self.marco1, text ="Jugador 2: "+str(self.puntajeJ2), font =("Arial ",24), padding =(5,5))
        self.labelGanador = ttk.Label(self.marco1, text ="", font =("Arial ",24), padding =(5,5))
        self.separ1 = ttk.Separator(self.marco1, orient=HORIZONTAL)
        self.marco1.grid(column=0, row=0)
        self.label1.grid(column=0, row=0)
        self.labelJ1.grid(column=0, row=1)
        self.labelJ2.grid(column=0, row=2)
        self.labelGanador.grid(column=0,row=3)
        self.separ1.grid(column=0, row=3)
        # Se inicializan cada una de las casillas del juego, nueve en total
        
        
        self.imgVacio = PhotoImage(file="vacioIcon.png")
        self.imgX = PhotoImage(file = "xIcon.png")
        self.imgO = PhotoImage(file = "oIcon.png")
        self.casilla1 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla2 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla3 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla4 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla5 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla6 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla7 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla8 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        self.casilla9 = ttk.Button(self.marco2, text='', padding=(5,5), image = self.imgVacio)
        
        self.marco2.grid(column=0, row=1)
        self.casilla1.grid(column=0,row=0)
        self.casilla2.grid(column=1,row=0)
        self.casilla3.grid(column=2,row=0)
        self.casilla4.grid(column=0,row=1)
        self.casilla5.grid(column=1,row=1)
        self.casilla6.grid(column=2,row=1)
        self.casilla7.grid(column=0,row=2)
        self.casilla8.grid(column=1,row=2)
        self.casilla9.grid(column=2,row=2)
        
        self.btn_iniciar = ttk.Button(self.marco3, text="Iniciar / Reiniciar", padding=(5,5), command = self.iniciar)
        self.btn_limpiar = ttk.Button(self.marco3, text="Limpiar", padding=(5,5), command = self.limpiar)
        self.marco3.grid(column=0, row=3)
        self.btn_iniciar.grid(column=0,row=0,columnspan=2)
        self.btn_limpiar.grid(column=2,row=0,columnspan=2)
        
        self.casillas=[self.casilla1,self.casilla2,self.casilla3,self.casilla4,self.casilla5,
                       self.casilla6,self.casilla7,self.casilla8,self.casilla9]
        self.tablero = np.zeros((3,3),dtype=int)
        #print(self.tablero)
        
        self.marca="X"
        self.casilla1.configure(command=lambda: self.mostrar(self.casilla1,[0,0]))
        self.casilla2.configure(command=lambda: self.mostrar(self.casilla2,[0,1]))
        self.casilla3.configure(command=lambda: self.mostrar(self.casilla3,[0,2]))
        self.casilla4.configure(command=lambda: self.mostrar(self.casilla4,[1,0]))
        self.casilla5.configure(command=lambda: self.mostrar(self.casilla5,[1,1]))
        self.casilla6.configure(command=lambda: self.mostrar(self.casilla6,[1,2]))
        self.casilla7.configure(command=lambda: self.mostrar(self.casilla7,[2,0]))
        self.casilla8.configure(command=lambda: self.mostrar(self.casilla8,[2,1]))
        self.casilla9.configure(command=lambda: self.mostrar(self.casilla9,[2,2]))
        
        self.raiz.mainloop()

    def limpiar(self):
        self.marca="X"
        self.tablero = np.zeros((3,3),dtype=int)
        self.labelGanador.configure(text="")
        for i in self.casillas:
            i.configure(text="")
            i.configure(state=NORMAL)
            i.configure(image=self.imgVacio)
        
    def iniciar(self):
        self.puntajeJ1 = 0
        self.puntajeJ2 = 0
        self.labelJ1.configure(text="Jugador 1: "+str(self.puntajeJ1))
        self.labelJ2.configure(text="Jugador 2: "+str(self.puntajeJ2))
        self.limpiar()
    
    def mostrar(self,cas,coord):
        if self.marca=="X":
            cas.configure(image=self.imgX)
            self.tablero[coord[0],coord[1]]=1
            if self.comprobarGanador():
                self.labelGanador.configure(text="Ganador: Jugador 1")
                self.puntajeJ1=self.puntajeJ1+1
                self.labelJ1.configure(text="Jugador 1: "+str(self.puntajeJ1))
                for i in self.casillas:
                    i.configure(state=DISABLED)
            self.marca="O"
        else:
            cas.configure(image=self.imgO)
            self.tablero[coord[0],coord[1]]=-1
            if self.comprobarGanador():
                self.labelGanador.configure(text="Ganador: Jugador 2")
                self.puntajeJ2=self.puntajeJ2+1
                self.labelJ2.configure(text="Jugador 2: "+str(self.puntajeJ2))
                for i in self.casillas:
                    i.configure(state=DISABLED)
            self.marca= "X"
        #print(self.tablero)
        
    
    def comprobarGanador(self):
        if np.sum(self.tablero[0,:])==3 or np.sum(self.tablero[1,:])==3 or np.sum(self.tablero[2,:])==3:
            return True
        elif np.sum(self.tablero[:,0])==3 or np.sum(self.tablero[:,1])==3 or np.sum(self.tablero[:,2])==3:
            return True
        elif np.sum(np.trace(self.tablero))==3 or np.sum(np.trace(np.fliplr(self.tablero)))==3:
            return True
        elif np.sum(self.tablero[0,:])==-3 or np.sum(self.tablero[1,:])==-3 or np.sum(self.tablero[2,:])==-3:
            return True
        elif np.sum(self.tablero[:,0])==-3 or np.sum(self.tablero[:,1])==-3 or np.sum(self.tablero[:,2])==-3:
            return True
        elif np.sum(np.trace(self.tablero))==-3 or np.sum(np.trace(np.fliplr(self.tablero)))==-3:
            return True
        else:
            return False
        
        

 
def main():
    miApp = TresEnLinea()
    return 0

if __name__ == '__main__':
    main()