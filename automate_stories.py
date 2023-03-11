import os
import re
import shutil
import subprocess
import json


#####################################################################
# Chemin vers le dossier des composants Next.js
# attention => faire en sorte que çà fonctionne avec ui/compoent 
# ou faire en sorte qu'il escane tout les repertotire et 
# sous_repertoire pour trouver  les composants 
######################################################################


#########################################################################
## etpe 1 : verifier si storybook est installer dans le project 
## si c'est pas le cas il installe via la commande 
#########################################################################



# Chemin vers le fichier package.json 
package_file_path = "chemin/vers/package.json"

# Charger le contenu du fichier package.json
with open(package_file_path) as package_file:
    package_data = json.load(package_file)

# Vérifier si la dépendance Storybook est présente
if "@storybook/react" not in package_data["dependencies"]:
    # Installer la dépendance Storybook
    subprocess.run(["npm", "install", "--save-dev", "@storybook/react"])






# Récupère la liste de tous les fichiers .tsx dans le dossier components
files = os.listdir("components")
tsx_files = [file for file in files if file.endswith(".tsx")]

# Parcours chaque fichier .tsx et crée un fichier story pour chaque composant
for file in tsx_files:
    # Récupère le nom du composant en retirant l'extension .tsx
    component_name = file.replace(".tsx", "")
    
    # Écrit le contenu du fichier story pour le composant
    with open(f"stories/{component_name}.stories.tsx", "w") as f:
        f.write(f"import React from 'react';\n")
        f.write(f"import {component_name} from '../components/{component_name}';\n")
        f.write(f"\n")
        f.write(f"export default {{\n")
        f.write(f"  title: '{component_name}',\n")
        f.write(f"  component: {component_name},\n")
        f.write(f"}};\n")

############################################################################
################code depe lerning #########################################
############################################################################


# Charger les données d'entraînement
train_data = [...] # Les données d'entraînement
train_labels = [...] # Les labels d'entraînement

# Définir le modèle
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(len(train_data[0]),)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(train_labels[0]), activation='softmax')
])

# Compiler le modèle
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entraîner le modèle
model.fit(train_data, train_labels, epochs=50, batch_size=32)

# Générer des prédictions
predictions = model.predict([...]) # Les données de test

# Afficher les prédictions
print(predictions)
########################################################################




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



