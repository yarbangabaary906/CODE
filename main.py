# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 08:34:55 2025

@author: LENOVO
"""

#main.py
from point import point
def main():
       p1=point(" p1 ",2,5);
       p2=point(" p2 ",8,7);
       p1.affiche();
       p2.affiche();
       p1.deplace(0.5,1.5);
       p1.affiche();
       p2.setX(2.5);
       p1.setY(0);
       d=p1.distance(p2);
       print("la distance entre", p1.getNom()," et ",p2.getNom()," est ",d)
main()
      
         