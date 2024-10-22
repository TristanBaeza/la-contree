import pygame
from dataclasses import dataclass
pygame.init()


@dataclass
class Player(pygame.sprite.Sprite):
    health: int
    max_health: int
    attack: int
    velocity: int
    image: pygame.Surface
    rect: pygame.Rect


pygame.display.set_caption("La contrée")
screen = pygame.display.set_mode((1080, 691))

background = pygame.image.load("assets/tapis_contree_modifie.jpg")

player_image = pygame.image.load("assets/cartes-gif/2c.jpg")
player1 = Player(health=100, max_health=100, attack=10, velocity=10, image=player_image, rect=player_image.get_rect())

running = True

while running:
    screen.blit(background, (0, 0))
    screen.blit(player1.image, player1.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture")
