"""
Lien : https://www.youtube.com/watch?v=M32xhZP04yo&list=PLhwJzRGWkHBOMFoXHlKie1s3UvOqiY14n&index=3
Cours : 3 - Changing line types using Taipy charts

Date : 02-08-23
"""

from taipy import Gui
import pandas as pd

my_df = pd.read_csv('data/dataset.csv')

line_charts="""

# Tutorial de la librairie TAIPY
## Graphique en lignes

<|{my_df}|chart|x=time|y[1]=A|y[2]=B|color[1]=red|color[2]=green|line[1]=dash|line[2]=dot|>

"""

Gui(line_charts).run(dark_mode=True)
