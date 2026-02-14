#------------------------CREAR CLASES DE JUGADOR------------------------
#Vamos a crear una clase de jugador que tenga atributos como nombre, vida, ataque y defensa
#La clase de jugador tendrá un método para recibir daño, que restará la cantidad de daño recibido a la vida del jugador, teniendo en cuenta su defensa.

class Jugador:
    def __init__(self, nombre,vida,ataque_especial, ataque, defensa_fisica, defensa_especial, velocidad, tipo, habilidades,naturaleza, nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque_especial = ataque_especial
        self.ataque = ataque
        self.defensa_fisica = defensa_fisica
        self.defensa_especial = defensa_especial
        self.velocidad = velocidad
        self.tipo = tipo
        self.habilidades = habilidades
        self.naturaleza = naturaleza
        self.nivel = nivel

    def recibir_danio(self):
        danio_real = self.ataque - self.defensa_fisica
        self.vida -= danio_real
        return print(f"Daño recibido: {danio_real}")ts


class Guerrero(Jugador):
    def __init__(self, nombre, armadura):
        super().__init__(nombre, vida=120, ataque=15, defensa=10+armadura)
        self.armadura = armadura
        





#Ejemplo de uso:
guerrero1 = Guerrero("Thor")
mago1 = Mago("Gandalf")
print(f"{guerrero1.nombre} tiene {guerrero1.vida} de vida.")
danio = mago1.ataque
danio_real = guerrero1.recibir_danio(danio)
print(f"{mago1.nombre} ataca a {guerrero1.nombre} causando {danio_real} de daño.")
print(f"{guerrero1.nombre} tiene {guerrero1.vida} de vida después del ataque.")

#--------------------CREAO SERVIDOR CON SOCKETS----------------------
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def manejar_cliente(conn, addr):
    print(f"Conectado con {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        mensaje = data.decode()
        print(f"Mensaje recibido: {mensaje}")
        conn.send("Acción recibida".encode())
    conn.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor iniciado...")

while True:
    conn, addr = servidor.accept()
    thread = threading.Thread(target=manejar_cliente, args=(conn, addr))
    thread.start()

#--------------------CREAO CLIENTE CON SOCKETS----------------------
import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

while True:
    mensaje = input("Acción: ")
    cliente.send(mensaje.encode())
    respuesta = cliente.recv(1024).decode()
    print("Servidor:", respuesta)

#Integración de la clase de jugador con el servidor y cliente de sockets:
jugadores = {}

jugadores[nombre] = Mago(nombre)