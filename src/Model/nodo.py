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
        Variazione funzionale del metodo di controllo hash
    nome get_valore_nodo:
        Restituisce il valore del nodo
    nome set_valore_nodo:
        Imposta il valore del nodo
    """

    def __init__(self, valore_iniziale: str):
        self.__id_nodo = valore_iniziale

    def __eq__(self, nodo: "Nodo") -> bool:
        """Confronto di due nodi."""
        return self.get_valore_id_nodo() == nodo.get_valore_id_nodo()

    def __hash__(self):
        """Genera codice hash per dizionario."""
        return hash(self.__id_nodo)

    def get_valore_id_nodo(self) -> str:
        return self.__id_nodo

    def set_valore_id_nodo(self, valore: str):
        self.__id_nodo = valore
