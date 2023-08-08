"""
Lien : https://www.taipy.io/project/crea    ting-a-data-dashboard/

Date : 01-08-23
"""

import datetime
import pandas as pd
from taipy import Gui
import webbrowser

logo = 'data/dog.png'

def image_action(state):
    webbrowser.open("https://www.royalrepublic.net/")
    
def get_data(path=str):
    dataset = pd.read_csv(path)
    dataset['Date'] = pd.to_datetime(dataset['Date']).dt.date
    return dataset

dataset = get_data('data/weather.csv')

start_date = datetime.date(2019, 11, 26)
end_date = datetime.date(2021, 6, 21)

def start_date_onchange(state, var_name, value):
    state.start_date = value.date()

def end_date_onchange(state, var_name, value):
    state.end_date = value.date()

def filter_by_date_range(dataset, start_date, end_date):
    mask = (dataset['Date'] > start_date) & (dataset['Date'] <= end_date)
    return dataset.loc[mask]

def button_action(state):
    pass

section1="""

<center>
<|navbar|lov={[("Page1", "1er onglet"), ("https://www.taipy.io/project/creating-a-data-dashboard/", "Cours"), ("https://docs.taipy.io/en/latest/getting_started/", "3ème onglet")]}|>
</center>

Tableau de bord avec la librairie Taipy
=======================================

<|layout|columns=6 8
<|
### Mon tableau de bord 😁
<center>
<|file_selector|label="Chargement"|>
</center>
|>

<|
<|{logo}|image|height=250px|width=250px|on_action=image_action|>
|>
|>
"""

section2="""

### Data visualisation 😎

<|{dataset}|chart|mode=lines|x=Date|y[1]=MinTemp|y[2]=MaxTemp|color[1]=blue|color[2]=red|>

"""

section3="""

<|layout|columns= 1 5
<|
## Paramètres personnalisés
**Date de départ**\n\n<|{start_date}|date|not with_time|on_change=start_date_onchange|>
<br/><br/>
**Date de fin**\n\n<|{end_date}|date|not with_time|on_change=end_date_onchange|>
<br/>
<br/>
<|button|label=Appuyer|on_action=button_action|>
|>
<|
<center>
<|{dataset}|table|page_size=10|height=500px|width=65%|>
</center>
|>
|>
"""

Gui(page=section1+section2+section3).run(dark_mode=True)
