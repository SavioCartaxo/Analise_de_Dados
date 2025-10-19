asteroides = {1 : """
         ______
      .-"      "-.
    .'            '.
   /  .-"````"-.     \ 
  |  |        |      |
  \  \_.--._./     _/
   '._      _.-'"`
      `""''`

""",

2 : """
  .--.
 (    )
  '--'

""",

3 : """
      
   .-'---'-.
  /         \ 
 |           |
 \          .'
  `-.____.-'
""",

4 :"""
  _.-.
 (    )
  `-’`
"""}

"""
   ^
  /_\ 
 |=|=|
"""

import random

numero_sort = random.randint(1,4)
while True:
    print(asteroides[numero_sort])
    numero_sort = random.randint(1,4)