import curses
import random
import time

def menu(tela):
    curses.curs_set(1)
    tela.clear()
    tela.refresh()

    nome_jogador = ""
    layout = [
        " _________________________________",
        "/                                 |",
        "|                                 |",
        "|     Bem-vindo ao Babbage:       |",
        "|    Uma aventura no espaço       |",
        "|                                 |",
        "|      Digite seu nome abaixo     |",
        "|                                 |",
        "| Nome:                           |",
        "|                                 |",
        "\\_________________________________/",
        ' ',
        '<- LEFT; -> RIGHT; 💥 SPACE; Q - QUIT'
    ]

    altura, largura = tela.getmaxyx()
    inicio_y = altura // 2 - len(layout) // 2
    inicio_x = largura // 2 - len(layout[0]) // 2

    while True:
        tela.clear()

        for i, linha in enumerate(layout):
            tela.addstr(inicio_y + i, inicio_x, linha)

        tela.addstr(inicio_y + 8, inicio_x + 8, nome_jogador + "_")

        tela.refresh()
        tecla = tela.getch()

        if tecla in [10, 13] and nome_jogador.strip():
            break
        elif tecla in (curses.KEY_BACKSPACE, 127, 8):
            nome_jogador = nome_jogador[:-1]
        elif 32 <= tecla <= 126 and len(nome_jogador) < 25:
            nome_jogador += chr(tecla)

    curses.curs_set(0)
    return nome_jogador

def mostrar_game_over(tela):
    tela.clear()
    curses.curs_set(0)

    game_over_texto = [
        "  ██████   █████  ███    ███ ███████     ███████ ██    ██ ███████ ██████  ",
        " ██       ██   ██ ████  ████ ██          ██   ██ ██    ██ ██      ██   ██ ",
        " ██   ███ ███████ ██ ████ ██ █████       ██   ██ ██    ██ █████   ██████  ",
        " ██    ██ ██   ██ ██  ██  ██ ██          ██   ██ ██    ██ ██      ██   ██ ",
        "  ██████  ██   ██ ██      ██ ███████     ███████  ██████  ███████ ██   ██ ",
    ]

    altura, largura = tela.getmaxyx()
    inicio_y = altura // 2 - len(game_over_texto) // 2
    inicio_x = largura // 2 - len(game_over_texto[0]) // 2

    for i, linha in enumerate(game_over_texto):
        tela.addstr(inicio_y + i, inicio_x, linha, curses.color_pair(4))

    tela.refresh()

def jogo(tela):
    curses.curs_set(0)
    tela.nodelay(True)
    tela.timeout(100)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    nave = [
        r"   /^\   ",
        r"  /|0|\  ",
        r" |=|0|=| "
    ]

    altura_nave = len(nave)
    largura_nave = len(nave[0])
    posicao_x = 0
    posicao_y = 30

    largura_area = 50
    inicio_x = 50
    pontuacao = 0

    tiros = []
    obstaculos = [(random.randint(0, 3), inicio_x + random.randint(6, 44)) for _ in range(8)]

    frame = 0
    velocidade = 7
    ultimo_tiro = -10
    intervalo_tiro = 2

    while True:
        tela.clear()
        altura, largura = tela.getmaxyx()

        if posicao_y + altura_nave >= altura or inicio_x + largura_area >= largura:
            tela.addstr(0, 0, "Aumente o tamanho da janela do terminal.")
            tela.refresh()
            continue

        for linha in range(altura):
            tela.addstr(linha, inicio_x, "|", curses.color_pair(3))
            tela.addstr(linha, inicio_x + largura_area - 1, "|", curses.color_pair(3))

        tela.addstr(0, 20, f'Pontuação: {pontuacao}')

        if frame % velocidade == 0:
            novos_obstaculos = []
            for y, x in obstaculos:
                nova_y = y + 1
                colisao_x = x + 1

                if nova_y >= posicao_y:
                    if (posicao_y <= nova_y <= posicao_y + altura_nave - 1 and
                        inicio_x + posicao_x - 1 <= colisao_x <= inicio_x + posicao_x + largura_nave):

                        altura_terminal, largura_terminal = tela.getmaxyx()
                        mensagem = f"{nome_jogador}, sua pontuação foi: {pontuacao}"

                        mostrar_game_over(tela)
                        tela.addstr(altura_terminal // 2 + 4, (largura_terminal - len(mensagem)) // 2, mensagem)
                        tela.refresh()
                        time.sleep(5)
                        return

                    novo_x = random.randint(inicio_x + 5, inicio_x + largura_area - 5)
                    novos_obstaculos.append((random.randint(0, 3), novo_x))
                else:
                    novos_obstaculos.append((nova_y, x))
            obstaculos = novos_obstaculos

        simbolos_inimigos = ['<|>', '>|<']
        for y, x in obstaculos:
            tela.addstr(y, x, random.choice(simbolos_inimigos), curses.color_pair(1))

        limite_x = largura_area - largura_nave - 1
        posicao_x = max(1, min(posicao_x, limite_x))

        for i, linha in enumerate(nave):
            tela.addstr(posicao_y + i, inicio_x + posicao_x, linha, curses.color_pair(2))

        novos_tiros = []
        for y, x in tiros:
            if y > 0:
                y -= 1
                if (y, x) in obstaculos:
                    obstaculos.remove((y, x))
                    pontuacao += 1
                    tela.addstr(0, 20, f'Pontuação: {pontuacao}')
                    obstaculos.append((random.randint(0, 10), inicio_x + random.randint(5, 45)))

                    if 15 < pontuacao < 35:
                        obstaculos.append((random.randint(0, 10), inicio_x + random.randint(5, 45)))
                    if pontuacao == 100:
                        for _ in range(100):
                            obstaculos.append((random.randint(0, 10), inicio_x + random.randint(5, 45)))
                else:
                    novos_tiros.append((y, x))
                    tela.addstr(y, x, "💥")
        tiros = novos_tiros

        tela.refresh()
        frame += 1

        tecla = tela.getch()
        if tecla == curses.KEY_RIGHT:
            posicao_x += 1
        elif tecla == curses.KEY_LEFT:
            posicao_x -= 1
        elif tecla == ord(' '):
            if frame - ultimo_tiro >= intervalo_tiro:
                tiro_x = inicio_x + posicao_x + nave[0].index("/") + 1
                tiros.append((posicao_y, tiro_x))
                ultimo_tiro = frame
        elif tecla == ord('q'):
            return

nome_jogador = curses.wrapper(menu)
curses.wrapper(jogo)