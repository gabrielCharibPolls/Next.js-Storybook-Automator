# Next.js-Storybook-Automator

Ce script Python automatise l'écriture de stories pour tous les composants Next.js d'un projet. Il fonctionne en deux étapes :

1. Scanner le fichier package.json pour vérifier si Storybook est installé dans le projet. 

   Le chemin du fichier package.json est défini dans la variable `package_file_path`. Si le fichier est trouvé, le script vérifie si la dépendance `"@storybook/react"` est présente dans la liste des dépendances. Si c'est le cas, le script continue, sinon il affiche un message d'erreur et s'arrête.

2. Parcourir les dossiers et sous-dossiers pour trouver le dossier "components" ou "ui", en excluant le dossier "node_modules".

   Le dossier "components" est prioritaire, mais si ce dernier n'est pas trouvé, le script recherche le dossier "ui". Le chemin complet du dossier trouvé est stocké dans la variable `components_folder_path`.

Une fois le dossier "components" ou "ui" trouvé, le script utilise les fichiers `.tsx` qu'il y trouve pour générer des fichiers story correspondant à chaque composant, qui seront créés dans le dossier "stories".

## Utilisation

1. Clonez ce dépôt sur votre ordinateur.
2. Placez tous les fichiers `.tsx` de vos composants dans le dossier "components" ou "ui".
3. Exécutez le script `generate_stories.py` à l'aide de Python.
4. Les fichiers story correspondant à chaque composant seront créés dans le dossier "stories".

## Exemple

Si vous avez un composant "Button" dans le fichier `components/Button.tsx`, le script créera un fichier `stories/Button.stories.tsx` avec le contenu suivant :

```typescript
import React from 'react';
import Button from '../components/Button';

export default {
  title: 'Button',
  component: Button,
};



mponent: Button,
};


## Notes 

- Ce script a été testé avec succès sur des projets Next.js 11.1.2 et Storybook 6.3.13.
- Ce script est fourni tel quel et n'est pas destiné à être utilisé en production. 

