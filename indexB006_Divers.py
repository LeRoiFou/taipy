"""
Autres widgets

Style des titres... : https://docs.taipy.io/en/release-2.2/manuals/gui/styling/

Date : 08-08-23
Editeur : Laurent Reynaud
"""

from taipy.gui import Gui
import pandas as pd

"""CONFIGURATION DE LA PAGE 01 : DF"""

# Récupération du fichier .csv converti en df pandas
my_df = pd.read_csv('data/weather.csv')

# Récupération du fichier .csv pour divers widgets
data = pd.read_csv("data/dataset.csv") 

# Selon la température, recourir aux couleurs configurées dans le fichier css
def my_df_table_style(state, index, row):
    # Si dans le champ MinTemp la valeur est < à 0...
    if row.MinTemp < 5:
        # Récupérer la configuration de la couleur dans le fichier css
        result = 'brrr'
    elif row.MaxTemp > 30:
        result = 'grrr'
    else:
        result = ''
    return result

# Propriété de divers widgets
slider_value_1 = 0
slider_value_2 = 0
slider_value_3 = 0
toggle_value = None

# Propriétés de la DF sur la page @
df_properties = {
    "filter":True, # Filtre
    "class_name":"rows-bordered rows-similar", # épaisseur des lignes de la DF
    "style":my_df_table_style, # Récupération de la fonction my_df_table_style
    "width":"70 %",
    }

# Configuration de présentation de la page @ 
page="""
## Présentation d'une dataframe et divers widgets

<|Données masquées/affichées|expandable|expanded=False|

<|layout|columns= 2 3 2|

### Barre de défilement ### {: .title_toggle }

### Boutons d'exécution ### {: .title_button }

### Autres widgets ### {: .title_slider }

|>
     
<|layout|columns= 2 3 2|

     <|

<|{slider_value_1}|slider|>  
  
<|{slider_value_2}|slider|>  
 
<|{slider_value_3}|slider|> 
    
    |>
    
    <|
    
<|Bouton n° 1|button|>  

<|Bouton n° 2|button|>  

<|Bouton n° 3|button|> 
    
    |>

    <|
    
<|{toggle_value}|toggle|lov=Dataset A; Dataset B; Dataset C|>
    
    |>
|>
|>

### Dataframe ### {: .title_df }

<|{my_df}|table|properties=df_properties|>

"""

pages = {"/": page,}

Gui(pages=pages).run(dark_mode=True)
