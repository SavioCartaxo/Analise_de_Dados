import os
import time
import msvcrt
from random import randint


asteroides = {0 : """
         ______
      .-"      "-.
    .'            '.
   /  .-"````"-.     \ 
  |  |        |      |
  \  \_.--._./     _/
   '._      _.-'"`
      `""''`

""",

1 : """
  .--.
 (    )
  '--'

""",

2 : """
      
   .-'---'-.
  /         \ 
 |           |
 \          .'
  `-.____.-'
""",

3 :"""
  _.-.
 (    )
  `-’`
"""}
nave = [
    "  ^",
    " /_\ ",
    "|=|=|"
]


mapa = [['1']* 15] * 30

mapa[10][10]= '0'
for _ in mapa:
    for i in _:
        print(i, end='')
    print('\n') 

contador_asteroides = 0
#while True:
 #   if contador_asteroides < 5:
  #      asteriode = randint(0,3)