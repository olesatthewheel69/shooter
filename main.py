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
pygame.mixer.music.load("space.ogg")
# pygame.mixer.music.play()
shot = pygame.mixer.Sound("fire.ogg")

ship = GameSprite("rocket.png", 5, 400, 70, 100, 10)
enemies = [GameSprite("ufo.png", randint(0, 620), -50, 80, 50, randint(1, 3)) for i in range(5)]
bullets = []
missed, killed = 0, 0

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(GameSprite("bullet.png", ship.rect.centerx - 7, ship.rect.top, 15, 20, -15))
                shot.play()
    window.blit(background, (0, 0))

    ship.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ship.rect.x > 5:
        ship.rect.x -= ship.speed
    if keys[pygame.K_RIGHT] and ship.rect.x < 620:
        ship.rect.x += ship.speed

    for enemy in enemies:
        enemy.draw()
        enemy.rect.y += enemy.speed
        if enemy.rect.y > height:
            enemy.rect.y = -50
            enemy.rect.x = randint(0, 620)
            enemy.speed = randint(1, 3)
            missed += 1
        elif enemy.rect.colliderect(ship.rect):
            game = False

    for bullet in bullets:
        bullet.draw()
        bullet.rect.y += bullet.speed
        if bullet.rect.y < 0:
            bullets.remove(bullet)
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                enemy.rect.y = -50
                enemy.rect.x = randint(0, 620)
                enemy.speed = randint(1, 3)
                if bullet in bullets:
                    bullets.remove(bullet)
                killed += 1

    pygame.display.update()
    clock.tick(60)