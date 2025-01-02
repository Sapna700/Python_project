import pygame
import random

# Define the Fruit class
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))  # Example size, change as needed
        self.image.fill((255, 0, 0))  # Example color, change as needed
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(-100, -40)  # Start above the screen

    def update(self):
        self.rect.y += 5  # Example speed, change as needed
        if self.rect.top > screen.get_height():
            self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
            self.rect.y = random.randint(-100, -40)  # Reset position above the screen

# Define the Basket class
class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 30))  # Example size, change as needed
        self.image.fill((0, 0, 255))  # Example color, change as needed
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() // 2
        self.rect.bottom = screen.get_height() - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5  # Example speed, change as needed
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5  # Example speed, change as needed
        # Keep the basket within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen.get_width():
            self.rect.right = screen.get_width()

# Initialize Pygame and create the screen, clock, and sprite groups
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
falling_objects = pygame.sprite.Group()

# Create the basket
basket = Basket()
all_sprites.add(basket)

# Create initial fruits
for _ in range(5):  # Example number of initial fruits
    fruit = Fruit()
    all_sprites.add(fruit)
    falling_objects.add(fruit)

# Main game loop
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    all_sprites.update()

    # Check for collisions
    caught_fruit = pygame.sprite.spritecollideany(basket, falling_objects)
    if caught_fruit:
        score += 1
        print(f"Score: {score}")
        caught_fruit.kill()  # Remove the caught fruit from the group
        new_fruit = Fruit()  # Create a new fruit
        all_sprites.add(new_fruit)
        falling_objects.add(new_fruit)

    # Clear the screen
    screen.fill((255, 255, 255))  # Example background color, change as needed

    # Draw all sprites
    all_sprites.draw(screen)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()