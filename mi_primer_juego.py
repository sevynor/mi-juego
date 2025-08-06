import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x300")

def revisar():
    caja1.colision()
    caja2.colision()

class Players:

    def __init__(self, posicionX, posicionY, velocidad, alto, ancho, color):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.velocidad = velocidad
        self.alto = alto
        self.ancho = ancho

        self.player = tk.Canvas(ventana, height=alto, width=ancho, bg=color)
        self.player.place(x=posicionX, y=posicionY)
        
        boton_arriba = tk.Button(ventana, text="↑", command= lambda: self.movimiento(0, -self.velocidad))
        boton_arriba.pack()

        boton_abajo = tk.Button(ventana, text="↓", command= lambda: self.movimiento(0, self.velocidad))
        boton_abajo.pack()

        boton_derecha = tk.Button(ventana, text="→", command= lambda: self.movimiento(self.velocidad, 0))
        boton_derecha.pack()

        boton_izquierda = tk.Button(ventana, text="←", command= lambda: self.movimiento(-self.velocidad, 0))
        boton_izquierda.pack()


    def movimiento(self, moverX, moverY):
        
        self.moverX = moverX
        self.moverY = moverY
        self.ifmover = 0
        
        revisar()

    def mover(self):
            if self.ifmover > 1:
                self.posicionX += self.moverX
                self.posicionY += self.moverY
                self.player.place(x=self.posicionX, y=self.posicionY)
                self.ifmover = 0
class Cajas:
    
    def __init__(self, posicionX, posicionY, alto, ancho, color, player, ifColision):
    
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.alto = alto
        self.ancho = ancho
        self.player = player

        self.caja = tk.Canvas(ventana, height=alto, width=ancho, bg=color)
        self.caja.place(x=posicionX, y=posicionY)
            

    def colision(self):
        global colisiono
        if int(self.player.posicionX)  + self.player.moverX > self.posicionX - self.player.moverX and int(self.player.posicionY)  + self.player.moverY < self.posicionY - self.player.moverY:
            pass
        else:
            self.player.ifmover += 1
            self.player.mover()

player1 = Players(posicionX=0, posicionY=0, velocidad=50, color="blue", alto=50, ancho=50)

caja1 = Cajas(posicionX=450, posicionY=0, player=player1, color="red", alto=50, ancho=50, ifColision=True)
caja2 = Cajas(posicionX=350, posicionY=0, player=player1, color="red", alto=50, ancho=50, ifColision=True)

ventana.mainloop()