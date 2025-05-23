
import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rampage Gorilla")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (0, 0, 200)

# Game settings
FPS = 60
PLAYER_SIZE = 50
ITEM_SIZE = 30
NUM_ITEMS = 10
SMASH_RANGE = 60

# Gorilla class
class Gorilla(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Household Item class
class HouseholdItem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ITEM_SIZE, ITEM_SIZE))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect(topleft=(x, y))

# Create sprite groups
all_sprites = pygame.sprite.Group()
items = pygame.sprite.Group()

# Create player
player = Gorilla()
all_sprites.add(player)

# Create household items
for _ in range(NUM_ITEMS):
    x = random.randint(0, WIDTH - ITEM_SIZE)
    y = random.randint(0, HEIGHT - ITEM_SIZE)
    item = HouseholdItem(x, y)
    all_sprites.add(item)
    items.add(item)

# Score and font
score = 0
font = pygame.font.SysFont(None, 36)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Smash mechanic
    if keys[pygame.K_SPACE]:
        for item in items.copy():
            if player.rect.colliderect(item.rect.inflate(SMASH_RANGE, SMASH_RANGE)):
                item.kill()
                score += 10

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()
