# Programa simples usando o Pygame

# Import a biblioteca pygame 
import pygame
pygame.init()

# Configuração da janela
screen = pygame.display.set_mode([500, 500])

# Executa até o usuário sair
running = True
while running:

    # Botão de fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche o fundo com a cor branco
    screen.fill((255, 255, 255))

    # Desenha um circulo purple
    pygame.draw.circle(screen, (138, 0, 196), (250, 250), 75)

    # Atualiza a tela
    pygame.display.flip()

# Fechar o pygame
pygame.quit()