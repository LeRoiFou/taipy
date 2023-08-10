"""
Les images

Date : 08-08-23
Editeur : Laurent Reynaud
"""

from taipy.gui import Gui, Icon, navigate, notify
import pandas as pd
import webbrowser

"""CONFIGURATION DE LA PAGE 01 : DF"""

# Récupération du fichier .csv converti en df pandas
my_df = pd.read_csv('data/weather.csv')

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

# Modification des valeurs dans la DF éditée
def my_df_on_edit(state, var_name, action, payload):
    index = payload["index"] # index de la ligne
    col = payload["col"] # nom de la colonne
    value = payload["value"] # nvlle valeur cellule en fct du type de la colonne
    user_value = payload["user_value"] # nouvelle valeur fournie par l'utilisateur
 
    old_value = state.my_df.loc[index, col]
    new_my_df = state.my_df.copy()
    new_my_df.loc[index, col] = value
    state.my_df = new_my_df
    
    # Message : information 'I'
    # https://docs.taipy.io/en/release-2.2/manuals/reference/taipy.gui.notify/
    notify(state, "I", f"Valeur modifiée de '{old_value}' à '{value}'")

# Ajout d'une nouvelle ligne dans la DF
def my_df_on_add(state, var_name, action, payload):
    
    empty_row = pd.DataFrame(
        [[None for _ in state.my_df.columns]], columns=state.my_df.columns)
    state.my_df = pd.concat([empty_row, state.my_df], axis=0, ignore_index=True)
    
    # Message : succès 'S'
    # https://docs.taipy.io/en/release-2.2/manuals/reference/taipy.gui.notify/
    notify(state, "S", "Nouvelle ligne ajoutée")
    
# Suppression d'une ligne dans la DF
def my_df_on_delete(state, var_name, action, payload):
    
    index = payload["index"] # row index
    state.my_df = state.my_df.drop(index=index)
    
    # Message : alerte 'W'
    # https://docs.taipy.io/en/release-2.2/manuals/reference/taipy.gui.notify/
    notify(state, "W", f"Ligne supprimée à l'index n° '{index}' 😱")

# Propriétés de la DF sur la page @
df_properties = {
    "filter":True, # Filtre
    "class_name":"rows-bordered rows-similar", # épaisseur des lignes de la DF
    "style":my_df_table_style, # Récupération de la fonction my_df_table_style
    "on_edit":my_df_on_edit, # Récupération de la fonction my_df_on_edit
    "on_add":my_df_on_add, # Récupération de la fonction my_df_on_add
    "on_delete":my_df_on_delete, # Récupération de la fonction my_df_on_delete
    }

# Configuration de présentation de la page @ - page 1
page1="""
## Page 1 - Présentation d'une dataframe

<|{my_df}|table|properties=df_properties|>
"""

"""CONFIGURATION DE LA PAGE 02 : HYPERLIENS ET IMAGE"""

# Récupération de l'image
image = 'data/dog.png'

# Insertion d'un lien à l'image
def image_action(state):
    webbrowser.open("https://www.royalrepublic.net/")

# Propriété de l'image sur la page @
image_properties = {
    "height":'250px',
    'width':'250px',
    'on_action':'image_action',
}

# Configuration de présentation de la page @ - page 2
page2="""
# Hyperliens et image

Cette page a été conçue avec la librairie [Taipy](https://www.taipy.io/)

<|{image}|image|properties=image_properties|>
"""

"""CONFIGURATION DU MENU"""

# Menu multi-pages
def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)

# Propriétés du menu sur la page @
menu_list = [  # Icônes des menus
    ('Page-1', Icon('data/forward.png', 'Page 1')),
    ('Page-2', Icon('data/play.png', 'Page 2'))]
menu_properties = {
    "on_action":on_menu, # Récupération de la fonction on_menu
}

# Configuration de présentation de la page @ avec le menu
page ="<|menu|label=Menu|lov={menu_list}|properties=menu_properties|>"
pages = {
    "/": page,
    "Page-1": page1,
    "Page-2": page2,
}

Gui(pages=pages).run(dark_mode=True)
