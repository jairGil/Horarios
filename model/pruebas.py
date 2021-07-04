from hora import Hora

if __name__ == "__main__":
    h1 = Hora(2, 30)
    h2 = Hora(3, 30)
    h1.set_hora(3)
    print(h1)
    print(h1.compara_hora(h2))