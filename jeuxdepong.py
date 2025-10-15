import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Positions et tailles
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
opponent = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# Boucle principale
clock = pygame.time.Clock()
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -7
            if event.key == pygame.K_DOWN:
                player_speed = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0

    # Déplacement joueur
    player.y += player_speed
    player.y = max(player.y, 0)
    player.y = min(player.y, HEIGHT - player.height)

    # Déplacement adversaire (IA basique)
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed
    opponent.y = max(opponent.y, 0)
    opponent.y = min(opponent.y, HEIGHT - opponent.height)

    # Déplacement balle
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collisions avec le haut/bas
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Collisions avec les raquettes
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    # Réinitialisation si la balle sort
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH // 2 - 15, HEIGHT // 2 - 15
        ball_speed_x *= -1

    # Dessin
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(60)
    