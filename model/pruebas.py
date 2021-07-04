from hora import Hora
from horario import Horario

if __name__ == "__main__":
    h = Horario()
    h1 = Hora(2, 30)
    h2 = Hora(2, 50)
    h1.set_hora(1)
    print(h1)
    print(h2)
    print(h1.compara_hora(h2))

    h.inserta_clase("Lu", h1, h2)
    h.inserta_clase("Mi", h1, h2)
    print(h)
