import pygame

width, height = 900, 400
screen = pygame.display.set_mode((width, height))

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()
    