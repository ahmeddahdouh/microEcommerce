# microEcommerce
Micro e-commerce starter project designed to help you learn and get familiar with FastAPI.

## Description`
L’objectif de ce projet est de développer une API simple qui simule le fonctionnement d’un micro site e-commerce. Ce projet servira de base pour apprendre et maîtriser l’utilisation de FastAPI, un framework moderne et performant pour la création d'API en Python. J’ai essayé de simplifier le maximum possible pour que ceci soit un dépôt starter project FastAPI pour les débutants qui souhaitent créer un site web e-commerce avec FastAPI.

Les principales fonctionnalités de cette API incluront :

Gestion des produits (création, lecture, mise à jour et suppression)

Gestion des utilisateurs et authentification

Traitement des commandes et suivi

gestion des stocks

L’API sera élaborée de manière modulaire et maintenable afin de promouvoir les bonnes pratiques de développement, telles que l’utilisation de pydantic pour la validation des données, et la documentation automatique offerte par FastAPI.

En complétant ce projet, vous acquerrez des compétences essentielles pour construire des applications web robustes et scalables en Python.
## Prérequis
Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- [Python](https://www.python.org/downloads/) (version 3.9 ou supérieure)
- [Poetry](https://python-poetry.org/docs/#installation) pour la gestion des dépendances

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <URL_DU_DEPOT>
   cd microEcommerce 
   ```
2.Créez un environnement virtuel :
   ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate` 
  ```
 3. Créez la base de données PostgreSQL et définissez les informations de connexion (comme l'hôte, le port, le nom d'utilisateur, le mot de passe et le nom de la base de données) dans le fichier `.env` sous forme de variables d'environnement.
4. Installez les dépendances avec Poetry :

   ```bash
   poetry install
   ```

4. Lancez le projet FastAPI :

   ```bash
   poetry run uvicorn main:app --reload
   ```

   Remplacez `main:app` par le chemin du fichier contenant l'instance de l'application FastAPI si nécessaire.

## Configuration

1. **Variables d'environnement :**
   Assurez-vous d'avoir un fichier `.env` contenant les variables d'environnement suivantes :

   ```
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=voicedetector_db_for_example
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```

   Modifiez ces valeurs selon votre configuration.

2. **Base de données :**
   PostgreSQL est utilisé pour stocker les données de l'application. Veillez à ce que votre base de données soit configurée et accessible avec les variables d'environnement spécifiées.

## Utilisation

- **Démarrer le serveur :** Utilisez la commande suivante pour démarrer le serveur :

   ```bash
   poetry run uvicorn main:app --reload
   ```

   Remplacez `main:app` par le chemin du fichier contenant l'application FastAPI.

- **Accéder à l'API :** Une fois le serveur démarré, accédez à l'API via `http://localhost:8000` ou l'URL indiquée par Uvicorn.
