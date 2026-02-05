import pygame
import random
import os

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 73

pygame.init()

background_image = pygame.transform.scale(
    pygame.image.load("E://Users//User//Downloads//bg.jpg"),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
) if os.path.exists("E://Users//User//Downloads//bg.jpg") else pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

if not os.path.exists("E://Users//User//Downloads//bg.jpg"):
    background_image.fill(pygame.Color("white"))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1500)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.set_color(color)

    def set_color(self, color):
        self.color = color
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, self.rect.width, self.rect.height))

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color("black"), 20, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color("red"), 20, 30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.set_color(pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            sprite2.set_color(pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You Win!", True, pygame.Color("black"))
        screen.blit(
            win_text,
            ((SCREEN_WIDTH - win_text.get_width()) // 2,
             (SCREEN_HEIGHT - win_text.get_height()) // 2)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
