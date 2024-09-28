import pygame
import os

pygame.font.init()
pygame.mixer.init()

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

GUN_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))

WIDTH, HEIGHT = 900, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spaceship Battle')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_TEXT_FONT = pygame.font.SysFont('comicsans', 100)


yellow_bullets = []
red_bullets = []


SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

FPS = 60
SPEED = 5
BULLET_SPEED = 7

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_on_screen(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health):

    SCREEN.blit(SPACE, (0,0))
   
    yellow_health_text = HEALTH_FONT.render('Health: ' + str(yellow_health), 1, WHITE)
    red_health_text = HEALTH_FONT.render('Health: ' + str(red_health), 1, WHITE)

    SCREEN.blit(yellow_health_text, (10, 10))
    SCREEN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    pygame.draw.rect(SCREEN, BLACK, BORDER)
    SCREEN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    SCREEN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(SCREEN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(SCREEN, RED, bullet)


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


def handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_health, red_health):
    for bullet in yellow_bullets:
        bullet.x += BULLET_SPEED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
        if yellow_health | red_health<= 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
        elif red_health | yellow_health <= 0:
            red_bullets.remove(bullet)

def display_winner_text(text):
    winner_text = WINNER_TEXT_FONT.render(text, 1, WHITE)
    SCREEN.blit(winner_text, (WIDTH//2 - winner_text.get_width()//2, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():

    yellow_health = 10
    red_health = 10

    yellow = pygame.Rect((10, 200), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
    red = pygame.Rect(850, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < 3:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2, 10, 5)
                    yellow_bullets.append(bullet)
                    GUN_FIRE_SOUND.play()
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < 3:
                    bullet = pygame.Rect(red.x - 30, red.y + red.height // 2, 10, 5)
                    red_bullets.append(bullet)
                    GUN_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()


            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()


        winner_text = ''
        if yellow_health <= 0:
            winner_text = 'Red Wins!'

        if red_health <= 0:
            winner_text = 'Yellow Wins!'
        
        if winner_text != '':
            display_winner_text(winner_text)
            break
        
        
        
        keys_pressed = pygame.key.get_pressed()
        yellow_moves(keys_pressed, yellow)
        red_moves(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_health, red_health)
        draw_on_screen(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health)
        

    main()

if __name__ == '__main__':
    main()
    