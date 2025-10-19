import msvcrt
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(): # Retorna o Nome da Pessoa após ela digitar
    limpar_tela()
    nome = ''
    while True:
        limpar_tela()
        print(f"""
      _________________________________
     /                                  |
    |                                   |
    |     Bem-vindo ao asteroids.py     |
    |                                   |
    |         Digite seu nome:          |
    |                                   |
    |{nome:^35}|
    |                                   |
    |                                  /
    ---------------------------------""")
        
        tecla = msvcrt.getch()
            
        if tecla != b'\r':
            nome += tecla.decode()    
        else:
            break
        
        if len(nome) == 35:
            break
    
    return nome