"""
Lien : https://docs.taipy.io/en/latest/getting_started/getting-started-gui/step_03/ReadMe/
Étape 3 : interaction

Date : 30-07-23
Éditeur : Laurent Reynaud
"""

from taipy.gui import Gui, notify

text = "Le texte saisi sera affiché ici"

# Definition of the page
page = """
# Premiers essais avec la librairie TaiPy

My text: <|{text}|>

<|{text}|input|>

<|Bouton d'exécution|button|on_action=on_button_action|>
"""

def on_button_action(state):
    notify(state, 'info', f'Information: {state.text}')
    state.text = "Bouton appuyé"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

Gui(page).run()
