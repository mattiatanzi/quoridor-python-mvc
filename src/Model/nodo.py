class Nodo:
    """Contiene informazioni del nodo del grafo.

    Attributi:
    ---------
    nome: nodo
        Contiene il valore del nodo
    Metodi:
    -------
    nome __eq__:
        Variazione funzionale del metodo di equivalenza tra nodi
    nome __hash__:
        Variazioen funzionale del metodo di controllo hash
    nome get_valore_nodo:
        Restituisce il valore del nodo
    """

    def __init__(self, valore_iniziale: str):
        self.nodo = valore_iniziale

    def __eq__(self, nodo: "Nodo") -> bool:
        return self.get_valore_nodo() == nodo.get_valore_nodo()

    def __hash__(self):
        return hash(self.nodo)

    def get_valore_nodo(self) -> str:
        return self.nodo
