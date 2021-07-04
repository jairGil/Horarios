class Hora:
    _hora: int
    _minuto: int

    def __init__(self, hora: int, minuto: int) -> None:
        self._hora = hora
        self._minuto = minuto

    def set_hora(self, hora: int) -> None:
        if hora > 0 and hora < 24:
            self._hora = hora
        else:
            self._hora = 0
    
    def set_minuto(self, minuto: int) -> None:
        if minuto > 0 and minuto < 60:
            self._minuto = minuto
        else:
            self._minuto = 0