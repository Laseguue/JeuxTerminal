# JeuxTerminal

# Jeux Terminal

## Description
Jeux Terminal est un jeu de combat simple où le joueur affronte un monstre. Le jeu est structuré en suivant le modèle MVC (Modèle-Vue-Contrôleur), avec des dossiers distincts pour les contrôleurs, les modèles et les vues.

## Règles du Jeu
Le joueur et le monstre ont des caractéristiques telles que la vie, l'agilité, la force, et la chance. Le but est de réduire les points de vie de l'adversaire à zéro. Le joueur a également des potions pour récupérer des points de vie.

## Comment Jouer
Exécutez le fichier [main.py](https://github.com/Laseguue/JeuxTerminal/blob/master/main.py) pour démarrer le jeu. Suivez les instructions à l'écran pour choisir le niveau de la partie et effectuer différentes actions pendant le jeu, telles qu'attaquer, boire une potion, ou fuir.

## Structure du Projet
- [main.py](https://github.com/Laseguue/JeuxTerminal/blob/master/main.py): Point d'entrée du jeu.
- [controleurs/game.py](https://github.com/Laseguue/JeuxTerminal/blob/master/controleurs/game.py): Contient la logique du jeu.
- [model/joueur.py](https://github.com/Laseguue/JeuxTerminal/blob/master/model/joueur.py): Définit la classe Joueur.
- [model/monstre.py](https://github.com/Laseguue/JeuxTerminal/blob/master/model/monstre.py): Définit la classe Monstre.
- [vues/menu.py](https://github.com/Laseguue/JeuxTerminal/blob/master/vues/menu.py): Gère l'affichage du menu et des options du jeu.

## Exigences
- Python 3.10 ou supérieur

## Auteur
[Laseguue](https://github.com/Laseguue)
