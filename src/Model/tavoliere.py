from Model.grafo import Grafo


class Tavoliere:
    """Contiene il tavoliere di gioco.
    
    Attributi
    ---------
    nome: tavoliere
        Il tavoliere di gioco realizzato con un grafo
    
    Metodi:
    -------

    nome get_adiacente
        Restituisce l'adiacente presente ad un nodo specifico
    """

    def __init__(self):
        self.tavoliere = Grafo()

    def get_adiacente(self,nodo,posizione):
        return self.tavoliere.get_adiacente(nodo,posizione)
    
    def piazza_muro(self, id_giocatore : str, azione: str):pass