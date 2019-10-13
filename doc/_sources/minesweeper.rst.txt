=========================
:mod:`minesweeper` module
=========================



Ce module définit les fonctions permettant de

* créer un jeu de démineur,
* accéder à quelques états possibles d'une case,
* accéder à quelques états possibles du jeu.

Il nécessite le module :mod:`cell`.

Définition d'un type énuméré
============================

* Une classe pour définir un *type énuméré* décrivant les trois états possibles
  d'un jeu.

  .. autoclass:: minesweeper.GameState
   

Constructeur
============
* La fonction qui crée un jeu de démineur :

  .. autofunction:: minesweeper.make_game
		  
Sélecteurs
==========


* Un jeu possède des dimensions (largeur et hauteur).

  .. autofunction:: minesweeper.get_width

  .. autofunction:: minesweeper.get_height
		  
* Un jeu possède des cases.

  .. autofunction:: minesweeper.get_cell


* Un jeu est dans un état gagnant, perdant ou inachevé.
		  
  .. autofunction:: minesweeper.get_state

Modificateurs
=============


* Révéler toutes les cases d'un jeu à partir d'une case donnée.

  .. autofunction:: minesweeper.reveal_all_cells_from


Divers
======

* Une fonction pour obtenir les coordonnées des cellule voisines d'une cellule.

  .. autofunction:: minesweeper.neighborhood
