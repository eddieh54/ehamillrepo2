import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Snake")
icon = pygame.image.load("images.png")
pygame.display.set_icon(icon)

black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

snake_x = random.randint(100, 700)
snake_y = random.randint(100, 500)
food_x = random.randint(100, 700)
food_y = random.randint(100, 500)

running = True

while running:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill(green)
        pygame.draw.rect(screen,blue,[snake_x,snake_y,20,20])
        pygame.draw.rect(screen,red,[food_x,food_y,20,20])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                snake_x -= 10
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                snake_x += 10
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                snake_y += 10
            if event.key == pygame.K_UP or event.key == ord('w'):
                snake_y -= 10
    if snake_x == 0 or snake_x == 800:
        print('game over')
        running = False
    if snake_y == 0 or snake_y == 600:
        print('game over')
        running = False
    pygame.display.update()
