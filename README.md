# Projet Backdoor en Python - Hacking Éthique

## Introduction
Ce projet est conçu à des fins éducatives pour illustrer le développement et le fonctionnement d'une backdoor simple en Python. Il se compose de deux parties principales : un fichier client (`backdoor_client.py`) et un fichier serveur (`backdoor_server.py`). L'objectif est de fournir une expérience pratique pour comprendre les vulnérabilités des systèmes informatiques et les moyens de les sécuriser.

## Avertissement
Ce projet est créé exclusivement dans un but éducatif dans le cadre de l'apprentissage du hacking éthique. Il ne doit être utilisé que dans un environnement de test ou avec des systèmes pour lesquels vous avez une autorisation explicite de tester. L'utilisation de ce code sur des réseaux ou des systèmes sans permission est illégale et contraire à l'éthique. En utilisant ce projet, vous acceptez d'assumer l'entière responsabilité de vos actions.

## Prérequis
- Python 3.x
- Connaissances de base en programmation Python
- Connaissances de base en réseaux informatiques

## Installation
1. Clonez ce dépôt sur votre machine locale.
2. Naviguez dans le dossier du projet.

## Usage
### Serveur
Pour démarrer le serveur, exécutez la commande suivante dans un terminal : python backdoor_server.py
Le serveur se mettra à l'écoute des connexions entrantes.

### Client
Sur la machine cible, exécutez le fichier client avec Python : python backdoor_client.py
Une fois le client exécuté, il se connectera au serveur, permettant l'exécution de commandes à distance.

## Fonctionnalités
- Exécution de commandes shell à distance
- Transfert de fichiers (client -> serveur)
- Capture d'écran

## Contribution
Les contributions à ce projet sont les bienvenues, surtout pour améliorer la sécurité et les aspects éducatifs. Veuillez soumettre vos pull requests ou ouvrir des issues pour toute suggestion ou amélioration.
