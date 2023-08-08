"""
Lien : https://docs.taipy.io/en/latest/getting_started/getting-started-gui/step_01/ReadMe/
Étape 1 : Première page Web

Date : 30-07-23
Éditeur : Laurent Reynaud
"""

from taipy import Gui

page = "Ceci est ma **première** page !"

Gui(page=page).run() # use_reloader=True
