import pygame
import random
import math

# ================= INITIAL SETUP =================
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

# ================= IMAGES =================
background = pygame.image.load("E://Users//User//Downloads//spaceinvader//bg.jpg")

# -------- PLAYER (ROCKET) --------
playerImg = pygame.image.load("E://Users//User//Downloads//spaceinvader//rocket.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))   # ✅ Rocket resized
playerX = 370
playerY = 380
playerX_change = 0

# -------- ENEMY --------
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    img = pygame.image.load("E://Users//User//Downloads//spaceinvader//ufo.png")
    img = pygame.transform.scale(img, (40, 40))            # ✅ Enemy resized
    enemyImg.append(img)

    enemyX.append(random.randint(0, SCREEN_WIDTH - 40))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.4)
    enemyY_change.append(10)

# -------- BULLET --------
bulletImg = pygame.image.load(
    "E://Users//User//Downloads//spaceinvader//bullet-removebg-preview.png"
)
bulletImg = pygame.transform.scale(bulletImg, (12, 30))   # ✅ Bullet resized
bulletX = 0
bulletY = playerY
bulletY_change = 8
bullet_state = "ready"

# ================= SCORE =================
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

# ================= FUNCTIONS =================
def show_score():
    score = font.render(f"Score : {score_value}", True, (255, 255, 255))
    screen.blit(score, (10, 10))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # ✅ Bullet fires from center of rocket
    screen.blit(bulletImg, (x + 26, y - 20))

def is_collision(ex, ey, bx, by):
    distance = math.sqrt((ex - bx) ** 2 + (ey - by) ** 2)
    return distance < 27

# ================= GAME LOOP =================
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                playerX_change = 0

    # -------- PLAYER MOVEMENT --------
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64

    # -------- ENEMY MOVEMENT --------
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 40:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 40)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # -------- BULLET MOVEMENT --------
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

        if bulletY <= 0:
            bulletY = playerY
            bullet_state = "ready"

    player(playerX, playerY)
    show_score()
    pygame.display.update()


