import pygame
import os

WIDTH, HEIGHT = 900, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceship Game')

WHITE = (255, 255, 255)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (55, 40)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (55, 40)), 270)

def draw_on_screen():
    SCREEN.fill(WHITE)
    SCREEN.blit(YELLOW_SPACESHIP, (300,100))
    SCREEN.blit(RED_SPACESHIP, (700, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_on_screen()

    pygame.quit()

if __name__ == '__main__':
    main()
    