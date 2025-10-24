# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 14:44:25 2025

@author: LENOVO
"""
# etudiant . py
import numpy as np
class etudiant:
    def __init__(self,matricule,nom,prenom,nbrNotes=0):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.nbrNotes=nbrNotes
        self.tabNotes=[]
    def get_matricule(self):
        return self.matricule
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_nbrNotes(self):
        return self.nbrNotes
    def get_tabNotes(self):
        return self.tabNotes
    def set_matricule(self,matricule):
        self.matricule
    def set_nom(self,nom):
        self.nom
    def set_prenom(self,prenom):
        self.prenom
    def set_nbrNotes(self,nbrNotes):
        self.nbrNotes
    def set_tabNotes(self,tabNotes):
        self.tabNotes
    def saisie(self):
        try:
           self.nbrNotes=int(input("entrer le nombre de note:")) 
           self.tabNotes=[]
           for i in range(self.nbrNotes):
               note=float(input("entrer la note"))
               if 0<=note<=20:
                   self.tabNotes.append(note)
               else:
                   print("note invalide")
                   return 
               def affichage(self):
                    print("matricule:")
                    print("nom:",)
                    print("prenom:",)
                    print("Notes:",) 
                    print("moyenne:",)
               def moyenne(self):
                     if self.nbrNotes==0:
                        return 0
                     else:
                          return sum(self.tabNotes) / self.nbrNotes
                     def admis(self):
                          return(sum( self.tabNotes)/(self.tabNotes))>=10
                      