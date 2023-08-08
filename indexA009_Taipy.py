"""
Lien : https://www.youtube.com/watch?v=w-tMYCB-I3A&list=PLhwJzRGWkHBOMFoXHlKie1s3UvOqiY14n&index=4

Cours : 4 - Organizing the layout of your application
Date : 02-08-23
"""

from taipy.gui import Gui
import pandas as pd

data = pd.read_csv("data/dataset.csv")
slider_value_1 = 0
slider_value_2 = 0
slider_value_3 = 0
toggle_value_1 = None

page_1 = """
<|navbar|>

#TUTORIEL TAIPY GUI - Layouts

<|Description extensible|expandable|expanded=False|

##Comment ça fonctionne ? 

<|layout|columns= 1 3 2|

<|{data}|table|width=99%|>

<|{data}|table|width=99%|>

<|{data}|table|width=99%|>

|>

|>
"""

page_2 = """
<|navbar|>

<|layout|columns=1 1 1|

    <|
###FIRST COLUMN
Chosen Dataset:  
<|{toggle_value_1}|toggle|lov=Dataset A; Dataset B; Dataset C|>
    |>

    <|
###SECOND COLUMN
Parameter 1:  
<|{slider_value_1}|slider|>  

Parameter 2:  
<|{slider_value_2}|slider|>  

Parameter 3:  
<|{slider_value_3}|slider|>  
    |>

    <|
###THIRD COLUMN
Button 1:  
<|Clean Data|button|>  

Button 2:  
<|Predict Data|button|>  

Button 3:  
<|New Scenario|button|>  
    |>

|>

<|layout|columns=1 4|
    <|
###Dataset
<|{data}|table|width=99%|>
    |>

    <|
###Data Visualization  
<|{data}|chart|x=time|y[1]=A|y[2]=B|>
    |>

|>
"""

if __name__ == '__main__':
    pages = {"Onglet_1": page_1, "Onglet_2": page_2}
    gui = Gui(pages=pages)
    gui.run(dark_mode=True)
