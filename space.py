import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption("Space Invaders")

# Load the player image
player_image = pygame.image.load("player.png")

# Set the player's starting position
player_x = 400
player_y = 550

# Load the enemy image
enemy_image = pygame.image.load("enemy.png")

# Scale down the enemy image
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

# Set the enemy's starting position
enemy_x = 50
enemy_y = 50

# Set the enemy's movement speed
enemy_speed = 5

import pygame

# Define a player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__()

        # Load the player image
        self.image = pygame.image.load("player.png")

        # Set the player's starting position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set the player's movement speed
        self.speed = 5

    def update(self):
        # Handle keyboard events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            # Create a new bullet
            bullet = Bullet(self.rect.centerx, self.rect.top)
            # Add the bullet to the sprites group
            sprites.add(bullet)
            # Add the bullet to the bullets group
            bullets.add(bullet)

# Define a bullet sprite class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__()

        # Load the bullet image
        self.image = pygame.image.load("bullet.jpg")
        self.image = pygame.transform.scale(self.image, (50, 50))
        # Set the bullet's starting position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set the bullet's movement speed
        self.speed = -10

    def update(self):
        # Move the bullet up the screen
        self.rect.y += self.speed

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption("Space Invaders")

# Create a sprites group to hold all sprites
sprites = pygame.sprite.Group()

# Create a bullets group to hold all bullets
bullets = pygame.sprite.Group()

# Create the player sprite
player = Player(400, 550)

# Add the player sprite to the sprites

# Add the player sprite to the sprites group
sprites.add(player)

# Set the game loop to run at 60 FPS
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update all sprites
    sprites.update()
    
    # Check if the bullet and enemy are colliding
    

    # Remove any bullets that have gone off the screen
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            sprites.remove(bullet)
            bullets.remove(bullet)
    

   # Move the enemy
    enemy_x += enemy_speed
    
    # Reverse the enemy's direction if it hits the edge of the screen
    if enemy_x > 750 or enemy_x < 0:
        enemy_speed *= -1


    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw all sprites
    sprites.draw(screen)
     # Draw the enemy
    screen.blit(enemy_image, (enemy_x, enemy_y))
    # Update the display
    pygame.display.flip()
    
    # Limit the game loop to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()

