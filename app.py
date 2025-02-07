#coding: utf-8

"""
Petit programme permettant de jouer à pile ou face
"""
import random

entree = ""
while(entree.lower() != "stop"):
  piece = random.randint(0, 1)
  entree = input("Pile ou face ? ('stop' pour arrêter) : ")
  if (entree.lower() == "pile") and (piece == 1):
    print("C'est gagné !")
  elif (entree.lower() == "face") and (piece == 0):
    print("C'est gagné !")
  else:
    print("C'est perdu !")
    
