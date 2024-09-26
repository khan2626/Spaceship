import pygame
import os

WIDTH, HEIGHT = 900, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceship Game')

WHITE = (255, 255, 255)
BLACK = (0,0,0)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

FPS = 60
SPEED = 5
BORDER = pygame.Rect(WIDTH/2, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def draw_on_screen(yellow, red):
    SCREEN.fill(WHITE)
    pygame.draw.rect(SCREEN, BLACK, BORDER)
    SCREEN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    SCREEN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_moves(keys_pressed, yellow):

    
    if keys_pressed[pygame.K_a]: #left
        yellow.x -= SPEED
    if keys_pressed[pygame.K_d]: #right
        yellow.x += SPEED
    if keys_pressed[pygame.K_w]: #up
        yellow.y -= SPEED
    if keys_pressed[pygame.K_s]: #down
        yellow.y += SPEED

def main():
    yellow = pygame.Rect((100, 200), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    red = pygame.Rect(700, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_on_screen(yellow, red)
        
        keys_pressed = pygame.key.get_pressed()
        yellow_moves(keys_pressed, yellow)
        

    pygame.quit()

if __name__ == '__main__':
    main()
    