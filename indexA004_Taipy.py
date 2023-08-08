"""
Lien : https://docs.taipy.io/en/latest/getting_started/getting-started-gui/step_04/ReadMe/
Étape 4 : Graphiques

Date : 30-07-23
Éditeur : Laurent Reynaud
"""

from taipy.gui import Gui, notify
import pandas as pd

dataframe = pd.DataFrame({"Text":['Test', 'Other', 'Love'],
                          "Score Pos":[1, 1, 4],
                          "Score Neu":[2, 3, 1],
                          "Score Neg":[1, 2, 0],
                          "Overall":[0, -1, 4]})

property_chart = {"type":"bar",
                  "x":"Text",
                  "y[1]":"Score Pos",
                  "y[2]":"Score Neu",
                  "y[3]":"Score Neg",
                  "y[4]":"Overall",
                  "color[1]":"green",
                  "color[2]":"grey",
                  "color[3]":"red",
                  "type[4]":"line"
                 }

# Definition of the page
page = """
# Premiers essais avec la librairie TaiPy

<|{dataframe}|table|>

<|{dataframe}|chart|properties={property_chart}|>
"""

Gui(page).run()
