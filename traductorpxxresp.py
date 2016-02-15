#!/usr/bin/env python
# -*- coding:utf-8 -*-

#       Copyright 2015 Francisco Carrillo (https://github.com/pacocp)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

###############################################################################
#
#      Traductor de Pxxr Gvng - Español
#
###############################################################################

import sys #This is for the arguments
from sys import argv
import subprocess
import nltk

#DICCIONARIO CON TODAS LAS PALABRAS, toda la información viene de este hilo de forocoches
#http://www.forocoches.com/foro/showthread.php?t=4121257

diccionario = {9: "Una pistola de 9mm",
"bogos": "chico guapo",
"Bogos": "Chico guapo",
"balin": "Vivir vida manejando billetes",
"Balin": "Vivir la vida manejando billetes",
"bitch": "puta",
"Bitch": "Puta",
"Bitches": "Putas",
"bitches": "putas",
"booty": "culo",
"Booty": "Culo",
"bowlong": "fumar marihuana",
"Bowlong": "Fumar marihuana",
"bricks": "paquetes de droga",
"Bricks": "Paquetes de droga",
"buyate": "culo",
"Buyate": "Culo",
"canelo": "pringado",
"Canelo": "Pringado",
"cipollo": "tonto",
"Cipollo": "Tonto",
"clica": "grupo de colegas",
"Clica": "Grupo de colegas",
"clicka": "grupo de colegas",
"Clicka": "Grupo de colegas",
"coco": "cocaína",
"Coco": "Cocaína",
"cuira": "buena mierda",
"Cuira": "Buena mierda",
"djin": "genio",
"Djin": "Genio",
"dradis": "chavales",
"Dradis": "Chavales",
"dzebi": "polla",
"Dzebi": "Polla",
"esquiar": "esnifar",
"Esquiar": "Esnifar",
"feka": "pringado",
"Feka": "Pringado",
"feos": "policías",
"Feos": "Policías",
"flex": "presumir",
"Flex": "Presumir",
"flush": "dinero",
"Flush": "Dinero",
"G": "gansta",
"Gabra": "Cocaína",
"gabra": "cocaína",
"goler": "esnifar",
"Goler": "Esnifar",
"goofy": "pringado",
"Goofy": "Pringado",
"guero": "barrio",
"Guero": "Barrio",
"guillao": "subido",
"Guillao": "Subido",
"habibi": "cariño",
"Habibi": "Cariño",
"hash": "hachís",
"Hash": "Hachís",
"hashla": "traficante",
"Hashla": "Traficante",
"hauma": "barrio",
"Hauma": "Barrio",
"Hoes": "Putas",
"hoes": "putas",
"hood": "barrio",
"Hood": "Barrio",
"jamra": "rojo",
"Jamra": "Rojo",
"jaoua": "hermano",
"Jaoua": "Hermano",
"Jawa": "Chica cani pintada como una puerta",
"jawa": "chica cani pintada como una puerta",
"josear": "buscarse la vida",
"Josear": "Buscarse la vida",
"junkeao": "enganchado a las drogas",
"Junkeao": "Enganchado a las drogas",
"kahba": "puta",
"Kahba": "Puta",
"kexar": "alabar",
"Kexar": "Alabar",
"kush": "marihuana",
"Kush": "Marihuana",
"lache": "vergüenza",
"lache": "vergüenza",
"Lache": "Vergüenza",
"laifa": "vida",
"Laifa": "Vida",
"lana": "dinero",
"Lana": "Dinero",
"lileta": "pringado",
"Lileta": "Pringado",
"molly": "MDMA",
"Molly": "MDMA",
"mover la bola": "pillar 10 gramos fiados y sacarle dinero",
"Mover la bola": "Pillar 10 gramos fiados y sacarle dinero",
"nina": "pistola de 9 mm",
"Nina": "Pistola de 9 mm",
"nueve": "pistola de 9 mm",
"Nueve": "Pistola de 9 mm",
"palomo": "pringado",
"Palomo": "Pringado",
"pimpim": "chulear",
"Pimpim": "Chulear",
"pinki": "dedo meñique",
"Pinki": "Dedo meñique",
"pirri": "colega",
"Pirri": "Colega",
"plomet": "fumar marihuana",
"Plomet": "Fumar marihuana",
"pravla": "hablar",
"Pravla": "Hablar",
"queso": "pasta de cocaína",
"Queso": "Pasta de cocaína",
"ratchet": "chavala cani pintada como una puerta",
"Ratchet": "Chavala cani pintada como una puerta",
"ratchets": "chavalas cani pintadas como una puerta",
"Ratchets": "Chavalas cani pintadas como una puerta",
"rachet": "chavala cani pintada como una puerta",
"Rachet": "Chavala cani pintada como una puerta",
"rachets": "chavalas cani pintadas como una puerta",
"Rachets": "Chavalas cani pintadas como una puerta",
"roca": "cocaína",
"Roca": "Cocaína",
"shouf": "mira",
"Shouf": "Mira",
"snitches": "chivatos",
"Snitches": "Chivatos",
"snitchin": "chivarse",
"Snitchin": "Chivarse",
"tana": "báscula",
"Tana": "Báscula",
"yema": "guantazo",
"Yema": "Guantazo",
}

#############################################################################

filename = str(argv[1])
subprocess.call(['echo','>',"traduccion.txt"])
g = open("traduccion.txt",'w')
with open(filename) as f:
    text = f.read()
    for key in diccionario:
        text = text.replace(str(key), diccionario[key])

for word in text:
    g.write(word)

f.close()
g.close()
