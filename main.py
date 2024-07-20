import pygame
from random import randint

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

width, height = 700, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooter")
background = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (width, height))

game = True
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()

ship = GameSprite("rocket.png", 5, 400, 80, 100, 10)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    window.blit(background, (0, 0))

    ship.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship.rect.x > 5:
        ship.rect.x -= ship.speed
    if keys[pygame.K_RIGHT] and ship.rect.x < 620:
        ship.rect.x += ship.speed

    pygame.display.update()
    clock.tick(60)