import pygame
import os

WIDTH, HEIGHT = 900, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceship Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

FPS = 60
SPEED = 5
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

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

    
    if keys_pressed[pygame.K_a] and yellow.x - SPEED > 0: #left
        yellow.x -= SPEED
    if keys_pressed[pygame.K_d] and yellow.x + SPEED + yellow.width < BORDER.x: #right
        yellow.x += SPEED
    if keys_pressed[pygame.K_w] and yellow.y - SPEED > 0: #up
        yellow.y -= SPEED
    if keys_pressed[pygame.K_s] and yellow.y + SPEED + yellow.height + 15 < HEIGHT: #down
        yellow.y += SPEED

def red_moves(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - SPEED > BORDER.x + BORDER.width + 15: #left
        red.x -= SPEED
    if keys_pressed[pygame.K_RIGHT] and red.x + SPEED + red.width - 15 < WIDTH: #right
        red.x += SPEED
    if keys_pressed[pygame.K_UP] and red.y - SPEED > 0: #up
        red.y -= SPEED
    if keys_pressed[pygame.K_DOWN] and red.y + SPEED + red.height + 15< HEIGHT: #down
        red.y += SPEED
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
        red_moves(keys_pressed, red)
        

    pygame.quit()

if __name__ == '__main__':
    main()
    