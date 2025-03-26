import pygame
pygame.init()
# Create the display surface object of specific dimension
window = pygame.display.set_mode ((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
ORANGE = (255, 94, 0)
# Draw solid circle
pygame.draw.rect(window, ORANGE, (300, 300,300,300), 0)
pygame.display.update()
# Render the text
text = ("Hello, Pygame!", True, (34, 23, 12))  # White color

# Game loop
running = True
while running:
# Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()