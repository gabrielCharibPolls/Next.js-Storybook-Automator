import os
import re
import shutil
import subprocess
import json
import openai

#####################################################################
# Chemin vers le dossier des composants Next.js
# attention => faire en sorte que çà fonctionne avec ui/compoent 
# ou faire en sorte qu'il escane tout les repertotire et 
# sous_repertoire pour trouver  les composants 
######################################################################


#########################################################################
## etape 1 : verifier si storybook est installer dans le project 
## si c'est pas le cas il installe via la commande 
#########################################################################
# Chemin du fichier package.json
package_file_path = "package.json"

try:
    # Charger le contenu du fichier package.json
    with open(package_file_path) as package_file:
        package_data = json.load(package_file)

    # Vérifier si la clé "devDependencies" est présente
    if "devDependencies" in package_data:
        # Vérifier si la dépendance Storybook est présente
        if "@storybook/react" not in package_data["devDependencies"]:
            # Demander à l'utilisateur s'il souhaite installer Storybook
            install_storybook = input("Storybook n'est pas installé. Voulez-vous l'installer ? (y/n) ")

            if install_storybook.lower() == "y":
                # Demander à l'utilisateur le chemin du répertoire d'installation
                install_path = input("Entrez le chemin du répertoire d'installation de Storybook : ")

                # Installer la dépendance Storybook dans le répertoire spécifié
                subprocess.run(["npm", "install", "--save-dev", "@storybook/react"], cwd=install_path)
                print("Storybook a été installé avec succès dans le répertoire :", install_path)
            else:
                print("Storybook n'a pas été installé.")
        else:
            print("Storybook est déjà installé.")
    else:
        print("La clé 'devDependencies' est manquante dans le fichier package.json.")
        install_storybook = input("Storybook n'est pas installé. Voulez-vous l'installer ? (y/n) ")
        if install_storybook.lower() == "y":
            install_path = input("Entrez le chemin du répertoire d'installation de Storybook : ")

            # Installer la dépendance Storybook dans le répertoire spécifié
            subprocess.run(["npm", "install", "--save-dev", "@storybook/react"], cwd=install_path)
            print("Storybook a été installé avec succès dans le répertoire :", install_path)

except FileNotFoundError:
    print("Le fichier package.json n'a pas été trouvé.")
except json.JSONDecodeError:
    print("Le fichier package.json est invalide ou malformé.")



###########################################################################################################
# etape 2 : rechercher dans tout les dossiers et sous-dossiers un dossier qui s'appel components ou ui 
#########################################################################################################


def find_components_folder():
    """
    Fonction qui recherche le dossier "components" ou "ui" dans un projet Next.js
    à partir du répertoire en cours, en excluant le dossier "node_modules".

    :return: le chemin complet du dossier "components" ou "ui" s'il est trouvé, None sinon
    """
    for root, dirs, files in os.walk('.'):
        if "node_modules" in dirs:
            dirs.remove("node_modules")  # exclure le dossier "node_modules" de la recherche
        if "components" in dirs:
            return os.path.join(root, "components")
        elif "ui" in dirs:
            return os.path.join(root, "ui")
    return None

components_folder_path = find_components_folder()
if components_folder_path is not None:
    print(f"Le dossier 'components' ou 'ui' se trouve ici : {components_folder_path}")
else:
    print("Le dossier 'components' ou 'ui' n'a pas été trouvé.")


###########################################################################
#  lister tout les compsoants 
###########################################################################
def list_components():
    components_folder_path = find_components_folder()
    if components_folder_path is not None:
        print('###########################################################')
        print('### liste de composants ')
        print('###########################################################')
        component_list = []
        for file_name in os.listdir(components_folder_path):
            if file_name.endswith(".js"):
                component_list.append(file_name)
        
        # Affichage de la liste des composants
        for component in component_list:
            print(component)
    else:
        print("Le dossier 'components' ou 'ui' n'a pas été trouvé.")

list_components()




def generate_chat_response(user_input):
    # Votre clé d'API OpenAI
    openai.api_key = "#################"

    # Liste des composants
    components = [
        "Component1",
        "Component2",
        "Component3",
      
    ]

    # Concaténation des composants avec le texte de l'utilisateur
    chat_input = f"Liste des composants : {', '.join(components)}\nUtilisateur : {user_input}"

    # Appel à l'API de chat GPT pour obtenir la réponse générée
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=chat_input,
        max_tokens=30  # Définir le nombre de tokens souhaité
    )
    # Récupération de la réponse générée
    chat_response = response.choices[0].text.strip()

    return chat_response

# Exemple d'utilisation
user_input = input("puta pregunta ")
response = generate_chat_response(user_input)
print("Bot : " + response)





#########################################################################
# Récupère la liste de tous les fichiers .tsx dans le dossier components
# files = os.listdir("components")
# tsx_files = [file for file in files if file.endswith(".tsx")]
# ########################################################################################
# # Parcours chaque fichier .tsx et crée un fichier story pour chaque composant
# for file in tsx_files:
#     # Récupère le nom du composant en retirant l'extension .tsx
#     component_name = file.replace(".tsx", "")
    
#     # Écrit le contenu du fichier story pour le composant
#     with open(f"stories/{component_name}.stories.tsx", "w") as f:
#         f.write(f"import React from 'react';\n")
#         f.write(f"import {component_name} from '../components/{component_name}';\n")
#         f.write(f"\n")
#         f.write(f"export default {{\n")
#         f.write(f"  title: '{component_name}',\n")
#         f.write(f"  component: {component_name},\n")
#         f.write(f"}};\n")

############################################################################
################code depe lerning #########################################
############################################################################


# # Charger les données d'entraînement
# train_data = [...] # Les données d'entraînement
# train_labels = [...] # Les labels d'entraînement

# # Définir le modèle
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(128, activation='relu', input_shape=(len(train_data[0]),)),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dropout(0.5),
#     tf.keras.layers.Dense(len(train_labels[0]), activation='softmax')
# ])

# # Compiler le modèle
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # Entraîner le modèle
# model.fit(train_data, train_labels, epochs=50, batch_size=32)

# # Générer des prédictions
# predictions = model.predict([...]) # Les données de test

# # Afficher les prédictions
# print(predictions)
########################################################################




# COMPONENTS_PATH = "path/to/nextjs/components"
# ######################################################################
# # Chemin vers le dossier de sortie pour les stories
# ######################################################################
# STORIES_PATH = "path/to/output/stories"
# ######################################################################
# # Regex pour extraire le nom du composant à partir du nom de fichier
# COMPONENT_NAME_REGEX = r"^(.*?)\.js$"
# ######################################################################
# # Supprimer le dossier de sortie s'il existe déjà
# ######################################################################
# if os.path.exists(STORIES_PATH):
#     shutil.rmtree(STORIES_PATH)
# ######################################################################
# # Créer le dossier de sortie
# ######################################################################
# os.mkdir(STORIES_PATH)
# ######################################################################
# # Parcourir tous les fichiers du dossier des composants
# ######################################################################
# for filename in os.listdir(COMPONENTS_PATH):
#     ######################################################################
#     # Vérifier si le fichier est un fichier JavaScript 
#     # faire en sorte que ça marche aussi pour type script 
#     # dans lideal pas juste pour react / next.js 
#     # mais les autres framwork 
#     ######################################################################
#     if filename.endswith(".js"):
#         ######################################################################
#         # Extraire le nom du composant à partir du nom de fichier
#         ######################################################################
#         component_name = re.match(COMPONENT_NAME_REGEX, filename).group(1)
#         subprocess.run(
#             f"npx storycap {os.path.join(COMPONENTS_PATH, filename)} --out {os.path.join(STORIES_PATH, component_name)}.stories.js",
#             shell=True,
#             check=True
#         )
# print("Toutes les stories ont été générées avec succès !")



