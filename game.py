import pygame
import random

pygame.init()

# creating surface
WINDOW_HEIGHT = 967
WINDOW_WIDTH = 760

surface = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 192, 203)
BLUE = (0, 0, 255)

# Loop starters
# start loop starter
start_run = True
# Main game loop starter
runner = True

# start menu

# surface colour
surface.fill(PINK)

# draw a frame
rect = (pygame.draw.rect(surface, BLACK, (320, 480, 360, 180), 10))

# set start fonts
START_FONT = pygame.font.Font('Gumdrop-ALJ72.ttf', 100)
START = START_FONT.render('START', True, WHITE)
START_RECT = START.get_rect()
START_RECT.center = rect.center

TITLE1_FONT = pygame.font.Font('Gumdrop-ALJ72.ttf', 60)
TITLE2_FONT = pygame.font.Font('Gumdrop-ALJ72.ttf', 300)
TITLE3_FONT = pygame.font.Font('Gumdrop-ALJ72.ttf', 20)

TITLE1 = TITLE1_FONT.render('catch the', True, WHITE)
TITLE2 = TITLE2_FONT.render('clown', True, WHITE)
TITLE3 = TITLE3_FONT.render('haghani edition', True, WHITE)

TITLE1_RECT = TITLE1.get_rect()
TITLE2_RECT = TITLE2.get_rect()
TITLE3_RECT = TITLE3.get_rect()

TITLE1_RECT.center = (500, 100)
TITLE2_RECT.center = (500, 250)
TITLE3_RECT.center = (500, 350)

# sounds
start_effect = pygame.mixer.Sound('Jump-SoundBible.com-1007297584.wav')

# start loop
while start_run:
    # blit texts
    surface.blit(START, START_RECT)
    surface.blit(TITLE1, TITLE1_RECT)
    surface.blit(TITLE2, TITLE2_RECT)
    surface.blit(TITLE3, TITLE3_RECT)
    for event_ in pygame.event.get():
        if event_.type == pygame.QUIT:
            start_run = False
            runner = False

        # switch to game page
        elif event_.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event_.pos[0]
            mouse_y = event_.pos[1]
            if 320 < mouse_x < 680 and mouse_y > 320 and mouse_y > 480:
                radius = 0
                start_effect.play()
                while True:
                    next_page = pygame.draw.circle(surface, BLACK, (500, 400), radius)
                    radius += 10
                    pygame.time.delay(1)
                    pygame.display.update()
                    if radius == 1000:
                        break
                surface.fill(BLACK)
                start_run = False

    # update
    pygame.display.update()

# main game

# set images
target = pygame.image.load('Rashid2.png')
target_rect = target.get_rect()
target_rect.centerx = WINDOW_HEIGHT // 2
target_rect.centery = WINDOW_WIDTH // 2

# variables
FPS = 60
clock = pygame.time.Clock()
TARGET_STARTING_VELOCITY = 3
TARGET_ACCELERATION = 0.5
STARTING_LIVES = 5
STARTING_POS = (WINDOW_HEIGHT // 2, WINDOW_WIDTH // 2)

score = 0
lives = STARTING_LIVES
target_velocity = TARGET_STARTING_VELOCITY
y = random.randint(1, 3)
x = random.randint(1, 3)

# set fonts
font = pygame.font.Font('Franxurter.ttf', 50)

lives_text = font.render('lives: ' + str(lives), True, WHITE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_HEIGHT - 20, 0)

score_text = font.render('score: ' + str(score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (0, 0)

game_over_text = font.render('Game Over', True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_HEIGHT // 2, WINDOW_WIDTH // 2)

continue_text = font.render('Press any key to continue', True, RED)
continue_rect = continue_text.get_rect()
continue_rect.centerx = WINDOW_HEIGHT // 2
continue_rect.top = game_over_rect.bottom

# background
background = pygame.image.load('background.png')
background_rect = background.get_rect()
background_rect.bottom = WINDOW_WIDTH
background_rect.centerx = WINDOW_HEIGHT // 2

# sounds and music
click_sound = pygame.mixer.Sound('click_sound.wav')
click_sound.set_volume(0.3)
miss_sound = pygame.mixer.Sound('miss_sound.wav')
miss_sound.set_volume(0.3)
pygame.mixer.music.load('ctc_background_music.wav')

# play music
pygame.mixer.music.play(-1, 0.0)

# game loop
while runner:
    mouse_pos = pygame.mouse.get_pos()

    if y == 1:
        if target_rect.top > background_rect.top:
            target_rect.y -= target_velocity
            pygame.display.update()

        elif target_rect.top <= background_rect.top:
            y = random.randint(1, 3)
            x = random.randint(1, 3)
            print(y)
            continue

    elif y == 2:
        if target_rect.bottom < WINDOW_WIDTH:
            target_rect.y += target_velocity
            pygame.display.update()

        elif target_rect.bottom >= WINDOW_WIDTH:
            y = random.randint(1, 3)
            x = random.randint(1, 3)
            print(y)
            continue

    if x == 1:
        if target_rect.left > 0:
            target_rect.x -= target_velocity
            pygame.display.update()

        elif target_rect.left <= 0:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            print(x, '===')
            continue

    elif x == 2:
        if target_rect.right < WINDOW_HEIGHT:
            target_rect.x += target_velocity
            pygame.display.update()

        elif target_rect.right >= WINDOW_HEIGHT:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            print(x, '===')
            continue

    elif x == 3 and y == 3:
        x = random.randint(1, 3)
        y = random.randint(1, 3)

    elif x == 3 and y != 3:
        pass

    elif y == 3 and x != 3:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runner = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if target_rect.collidepoint(mouse_pos):
                click_sound.play()
                y_bug = y
                x_bug = x
                y = random.randint(1, 3)
                x = random.randint(1, 3)
                while y == y_bug and x == x_bug:
                    y = random.randint(1, 3)
                    x = random.randint(1, 3)
                    if y != y_bug or x != x_bug:
                        break
                print('h')
                score += 1
                target_velocity += TARGET_ACCELERATION
                continue

            else:
                miss_sound.play()
                lives -= 1

        # game over
        if lives == 0:
            surface.blit(game_over_text, game_over_rect)
            surface.blit(continue_text, continue_rect)
            pygame.display.update()
            pygame.mixer.music.stop()
            pause = True
            while pause:
                for event__ in pygame.event.get():
                    if event__.type == pygame.KEYDOWN:
                        score = 0
                        target_velocity = TARGET_STARTING_VELOCITY
                        lives = STARTING_LIVES
                        target_rect.center = STARTING_POS
                        pygame.mixer.music.play(-1, 0.0)
                        pause = False

                    if event__.type == pygame.QUIT:
                        pause = False
                        runner = False

    # update texts
    score_text = font.render('score: ' + str(score), True, WHITE)
    lives_text = font.render('lives: ' + str(lives), True, WHITE)

    # blit texts
    surface.fill(BLACK)
    surface.blit(lives_text, lives_rect)
    surface.blit(score_text, score_rect)

    # blit images
    surface.blit(background, background_rect)
    surface.blit(target, target_rect)

    surface.blit(target, target_rect)

    # update
    pygame.display.update()

    # tick the clock
    clock.tick(FPS)

pygame.quit()
