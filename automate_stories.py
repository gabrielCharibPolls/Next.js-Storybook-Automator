import os
import re
import shutil
import subprocess

#####################################################################
# Chemin vers le dossier des composants Next.js
# attention => faire en sorte que çà fonctionne avec ui/compoent 
# ou faire en sorte qu'il escane tout les repertotire et 
# sous_repertoire pour trouver  les composants 
######################################################################
COMPONENTS_PATH = "path/to/nextjs/components"
######################################################################
# Chemin vers le dossier de sortie pour les stories
######################################################################
STORIES_PATH = "path/to/output/stories"
######################################################################
# Regex pour extraire le nom du composant à partir du nom de fichier
COMPONENT_NAME_REGEX = r"^(.*?)\.js$"
######################################################################
# Supprimer le dossier de sortie s'il existe déjà
######################################################################
if os.path.exists(STORIES_PATH):
    shutil.rmtree(STORIES_PATH)
######################################################################
# Créer le dossier de sortie
######################################################################
os.mkdir(STORIES_PATH)
######################################################################
# Parcourir tous les fichiers du dossier des composants
######################################################################
for filename in os.listdir(COMPONENTS_PATH):
    ######################################################################
    # Vérifier si le fichier est un fichier JavaScript 
    # faire en sorte que ça marche aussi pour type script 
    # dans lideal pas juste pour react / next.js 
    # mais les autres framwork 
    ######################################################################
    if filename.endswith(".js"):
        ######################################################################
        # Extraire le nom du composant à partir du nom de fichier
        ######################################################################
        component_name = re.match(COMPONENT_NAME_REGEX, filename).group(1)
        subprocess.run(
            f"npx storycap {os.path.join(COMPONENTS_PATH, filename)} --out {os.path.join(STORIES_PATH, component_name)}.stories.js",
            shell=True,
            check=True
        )
print("Toutes les stories ont été générées avec succès !")



