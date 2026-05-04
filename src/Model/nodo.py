class Nodo:
    def __init__(self, valore_iniziale: str):
        self.nodo = valore_iniziale

    def __eq__(self, nodo: Nodo) -> bool:
        return self.get_valore_nodo() == nodo.get_valore_nodo()
    
    def get_valore_nodo(self)-> str:
        return self.get_valore_nodo