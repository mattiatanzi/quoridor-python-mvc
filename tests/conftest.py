import sys
import os

# Calcola il percorso assoluto della root del progetto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Aggiunge la root al sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)