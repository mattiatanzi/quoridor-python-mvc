


from src.Model.parametri_partita import ErroreParametriPartita


class ParametriPartitaView:

    def stampa_errore_parametri(self, errore: ErroreParametriPartita):
        print(f"Errore Parametri:  + {errore}")
