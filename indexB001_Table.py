"""
Lien : https://www.taipy.io/tips/using-tables/

Avec Taipy, c'est possible de présenter des tables 😲😲😲
https://docs.taipy.io/en/develop/manuals/gui/viselements/table/

Date : 01-08-23
Éditeur : Laurent Reynaud
"""

from taipy.gui import Gui, notify
import pandas as pd

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

# Propriétés de la page @
page_properties = {
    "filter":True, # Filtre
    "class_name":"rows-bordered rows-similar", # épaisseur des lignes de la DF
    "style":my_df_table_style, # Récupération de la fonction my_df_table_style
    "on_edit":my_df_on_edit, # Récupération de la fonction my_df_on_edit
    "on_add":my_df_on_add, # Récupération de la fonction my_df_on_add
    "on_delete":my_df_on_delete, # Récupération de la fonction my_df_on_delete
    }

# Configuration de la présentation de la page @
page = """
<|{my_df}|table|properties=page_properties|>
"""

if __name__ == '__main__':
    Gui(page=page).run()
