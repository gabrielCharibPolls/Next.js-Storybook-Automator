# Générateur de stories pour les composants Next.js

Ce script Python automatise l'écriture de stories pour tous les composants Next.js d'un projet.

## Utilisation

1. Clonez ce dépôt sur votre ordinateur.
2. Placez tous les fichiers `.tsx` de vos composants dans le dossier "components".
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
