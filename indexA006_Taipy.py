"""
Lien : https://www.youtube.com/watch?v=OpHAncCb8Zo&list=PLhwJzRGWkHBOMFoXHlKie1s3UvOqiY14n&index=1
Cours : 1 - Getting started with Taipy GUI

Date : 01-08-23
"""

from taipy import Gui

var_name = "James"
link = "https://docs.taipy.io/en/latest/manuals/gui/viselements/"
value = 5

page = """
# Bienvenue dans la librairie Taipy 

Bonjour ! Mon nom est <|{var_name}|>

Exemple d'un widget (<|{link}|>) <br/> <br/>
<|{value}|slider|min=1|max=20|>

"""
Gui(page=page).run(dark_mode=True)
