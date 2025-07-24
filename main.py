#This Is An Open Sroce Project
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Coin Collector - Made In Pygame")
icon = pygame.image.load("assets/icon.ico")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Game Variables
PlayX = 0
PlayY = 0
Speed = 5
CoinsColleted = 0

# Load Images
PlayerIMG = pygame.image.load("assets/Player.png")
CoinIMG = pygame.image.load("assets/coin.png")

# Get Rects from images
player_rect = PlayerIMG.get_rect(topleft=(PlayX, PlayY))
coin_rect = CoinIMG.get_rect(topleft=(random.randint(20, 1260), random.randint(20, 700)))

# Font setup
font = pygame.font.SysFont("Arial", 36)

# Main Game Loop
running = True
while running:
    screen.fill("green")

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= Speed
    if keys[pygame.K_s]:
        player_rect.y += Speed
    if keys[pygame.K_a]:
        player_rect.x -= Speed
    if keys[pygame.K_d]:
        player_rect.x += Speed

    # Collision with coin
    if player_rect.colliderect(coin_rect):
        CoinsColleted += 1
        coin_rect.topleft = (random.randint(20, 1260), random.randint(20, 700))

    # Draw player and coin
    screen.blit(PlayerIMG, player_rect)
    screen.blit(CoinIMG, coin_rect)

    # Draw score text
    score_text = font.render(f"Coins Collected: {CoinsColleted}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    # Update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
