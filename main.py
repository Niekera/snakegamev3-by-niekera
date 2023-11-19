import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10

pygame.init()
surface = pygame.display.set_mode([800, 800])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('1.jpg').convert()

def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    surface.blit(img, (0, 0))

    [pygame.draw.rect(surface,  (235, 225, 52), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))

    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE

        # Teleport snake to the opposite edge if it goes beyond the boundaries
        x = x % RES
        y = y % RES

        snake.append((x, y))
        snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            close_game()

    pygame.display.flip()
    clock.tick(fps)
    close_game()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }

pygame.quit()
quit()
