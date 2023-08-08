import pandas as pd
from taipy import Gui

n_week = 40

my_df = pd.read_csv('data/titanic.csv')

page = """

# Bases de la librairie TaiPy

Nombre de semaines : <|{n_week}|>

<|{n_week}|slider|min=1|max=40|>

# Données des occupants du Titanic

<|{my_df}|table|height=480px|width=1500px|>

## Données graphiques des survivants par sexe

<|{my_df}|chart|type=bar|x=Sex|y=Survived|>

"""

Gui(page=page).run(dark_mode=True)
