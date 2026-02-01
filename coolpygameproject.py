import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My first game screen")

BACKGROUND_COLOR = (255,255,255)
RECTANGLE_COLOR = (0, 128, 255)
TEXT_COLOR = (255, 255, 255)

rect_width = 200
rect_height = 100
rectangle = pygame.Rect(
    (WIDTH - rect_width) // 2,
    (HEIGHT - rect_height) // 2,
    rect_width,
    rect_height
)

font = pygame.font.SysFont(None, 36)
text_surface = font.render("Hello Pygame!", True, TEXT_COLOR)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, RECTANGLE_COLOR, rectangle)
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
