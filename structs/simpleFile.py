#coding: utf-8

# F     I  F     O
# First In First Out

import simplePy.simplePy as simple

class simpleFile():
    def __init__(self, v_simplePy):
        if v_simplePy == simple.simplePy():
            self.content = []

    def __str__(self):
        return str(self.content)

    def ajouter(self, integer):
        self.content.append(integer)

    def enlever(self):
        #return self.content.pop()
        newfile = self.content[1:]
        self.content = newfile[:]

    def taille(self):
        return len(self.content)

    def est_vide(self):
        return self.taille() == 0