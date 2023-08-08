"""
Lien : https://docs.taipy.io/en/latest/getting_started/getting-started-gui/step_02/ReadMe/
Étape 2 : Éléments visuels

Date : 30-07-23
Éditeur : Laurent Reynaud
"""

from taipy.gui import Gui

text = "Le texte saisi sera affiché ici"

page = """
# Premiers essais avec la librairie TaiPy

Texte affiché : <|{text}|>

<|{text}|input|>
"""

Gui(page).run()
