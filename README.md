Générateur de stories pour les composants Next.js

Ce script Python automatise l'écriture de stories pour tous les composants Next.js d'un projet.

Utilisation

Clonez ce dépôt sur votre ordinateur.
Placez tous les fichiers .tsx de vos composants dans le dossier "components".
Exécutez le script generate_stories.py à l'aide de Python.
Les fichiers story correspondant à chaque composant seront créés dans le dossier "stories".

Exemple

Si vous avez un composant "Button" dans le fichier components/Button.tsx, le script créera un fichier stories/Button.stories.tsx avec le contenu suivant :

typescript
Copy code
import React from 'react';
import Button from '../components/Button';

export default {
  title: 'Button',
  component: Button,
};
Vous pouvez ensuite modifier ce fichier story selon vos besoins pour ajouter des variantes, des actions ou des informations supplémentaires sur votre composant.

