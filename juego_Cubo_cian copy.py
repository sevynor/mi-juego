import tkinter as tk 

ventana = tk.Tk()
ventana.title("juego")
ventana.geometry("1200x900")

class Player:

    def __init__(self, alto, ancho, velocidad, color, cajas):

        self.posicionX = 50
        self.posicionY = 500
        self.velocidad = velocidad
        self.alto = alto
        self.ancho = ancho

        self.cajas = cajas

        self.jugador = tk.Canvas(ventana, width=ancho, height=alto, bg=color)
        self.jugador.place(x=self.posicionX, y=self.posicionY)

        self.teclado = ventana.bind("<Key>", self.teclaValor)


    def teclaValor(self, event):

        moverX = self.posicionX
        moverY = self.posicionY
        self.ifColision = False

        self.tecla = {event.keysym}
        self.tecla = str(self.tecla).replace("'", "")
        self.tecla = str(self.tecla).replace("{", "")
        self.tecla = str(self.tecla).replace("}", "")
        
        if self.tecla == "w":

            moverY -= self.velocidad
            

        elif self.tecla == "s":

            moverY += self.velocidad
            

        elif self.tecla == "a":
            moverX -= self.velocidad


        elif self.tecla == "d":
            moverX += self.velocidad

        for caja in self.cajas:

            colisionDerecho = moverX + self.ancho
            colisionIzquierdo = moverX
            colisionArriba = moverY
            colisionAbajo = moverY + self.alto

            if colisionArriba <= caja.colisionArriba and colisionAbajo >= caja.colisionAbajo:
                
                if colisionIzquierdo <= caja.colisionDerecho and colisionIzquierdo >= caja.colisionIzquierdo:
                    self.ifColision = True
                    print("colision en la " + caja.nombre)

                elif colisionDerecho >= caja.colisionIzquierdo and colisionDerecho <= caja.colisionDerecho:
                    self.ifColision = True
                    print("colision en la " + caja.nombre)

            elif colisionAbajo >= caja.colisionArriba and colisionAbajo <= caja.colisionAbajo:
                
                if colisionIzquierdo <= caja.colisionDerecho and colisionIzquierdo >= caja.colisionIzquierdo:
                    
                    self.ifColision = True
                    print("colision en la " + caja.nombre)

                elif colisionDerecho >= caja.colisionIzquierdo and colisionDerecho <= caja.colisionDerecho:
                    self.ifColision = True
                    print("colision en la " + caja.nombre)

                if colisionIzquierdo <= caja.colisionIzquierdo and colisionDerecho > caja.colisionDerecho:
                    self.ifColision = True
                    print("colision en la " + caja.nombre)
            
            elif colisionArriba <= caja.colisionAbajo and colisionArriba >= caja.colisionArriba:

                if colisionIzquierdo <= caja.colisionIzquierdo and colisionDerecho > caja.colisionDerecho:
                    self.ifColision = True
                    print("colision en la  " + caja.nombre)

            
                elif colisionDerecho >= caja.colisionIzquierdo and colisionDerecho <= caja.colisionDerecho:
                    
                    self.ifColision = True
                    print("colision en la " + caja.nombre)
                    
                elif colisionIzquierdo <= caja.colisionDerecho and colisionIzquierdo >= caja.colisionIzquierdo:
                    
                    self.ifColision = True
                    print("colision en la " + caja.nombre)


            
        if not self.ifColision:
            self.movimiento(moverX=moverX, moverY=moverY)
            self.ifColision = False
        else:
            self.movimiento(moverX=self.posicionX, moverY=self.posicionY)
                

    def movimiento(self, moverX, moverY):
        self.posicionX = moverX
        self.posicionY = moverY

        self.jugador.place(x=self.posicionX, y=self.posicionY)

class Cajas:

    def __init__(self, alto, ancho, posicionX, posicionY, color, nombre):

        self.jugador = tk.Canvas(ventana, width=ancho, height=alto, bg=color)
        self.jugador.place(x=posicionX, y=posicionY)
        self.nombre = nombre

        self.posicionX = posicionX
        self.posicionY = posicionY
        self.alto = alto
        self.ancho = ancho

        self.colisionDerecho = self.posicionX + self.ancho
        self.colisionIzquierdo = self.posicionX
        self.colisionArriba = self.posicionY 
        self.colisionAbajo = self.posicionY + self.alto

caja_1 = Cajas(alto=50, ancho=50, color="grey", posicionY=500, posicionX=300, nombre="caja 1")
caja_2 = Cajas(alto=100, ancho=50, color="grey", posicionY=500, posicionX=450, nombre="caja 2")
caja_3 = Cajas(alto=30, ancho=300, color="grey", posicionY=350, posicionX=600, nombre="caja 3")
caja_4 = Cajas(alto=300, ancho=300, color="grey", posicionY=470, posicionX=800, nombre="caja 4")
caja_5 = Cajas(alto=300, ancho=50, color="grey", posicionY=200, posicionX=550, nombre="caja 5")
caja_6 = Cajas(alto=10, ancho=10, color="grey", posicionY=320, posicionX=200, nombre="caja 6")

player_1 = Player(alto=50, ancho=50, velocidad=10, color="cyan", cajas=[caja_1,caja_2,caja_3, caja_4,caja_5,caja_6])

ventana.mainloop()