=========================
:mod:`cell` module
=========================



Ce module définit les fonctions permettant de

* créer une cellule (case) du jeu de démineur,
* accéder à quelques attributs d'une cellule,
* modifier quelques attributs d'une cellule.


Constructeur
============
* La fonction qui crée une cellule :

  .. autofunction:: cell.make


Prédicats et sélecteurs
=======================

* Une cellule peut contenir une bombe ou non.

  .. autofunction:: cell.is_bomb

* Une cellule peut être marquée par une bombe hypothétique ou non.
  
  .. autofunction:: cell.is_hypothetic_bomb

* Une cellule peut être révélée ou non.
		  
  .. autofunction:: cell.is_revealed

* Une cellule possède un certain nombre de bombes dans son voisinage.

  .. autofunction:: cell.number_of_bombs_in_neighborhood



Modificateurs
=============

* Pour révéler le contenu d'une cellule

  .. autofunction:: cell.reveal

* Pour marquer une cellule comme contenant hypothétiquement une bombe.

  .. autofunction:: cell.set_hypothetic

* Pour démarquer une cellule contenant hypothétiquement une bombe.

  .. autofunction:: cell.unset_hypothetic

* Pour préciser le nombre de bombes dans le voisinage d'une cellule

  .. autofunction:: cell.set_number_of_bombs_in_neighborhood
