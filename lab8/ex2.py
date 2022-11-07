import pygame
import numpy as np
from pygame.draw import *
from random import randint
pygame.init()

n = 5 #  number of balls
FPS = 30
screen = pygame.display.set_mode((1200, 900))

pi = np.pi
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
amount = 0
x_balls = [] #  координаты шариков
y_balls = [] #  координаты шариков
r_balls = [] #  радиусы шариков
color_balls = [] # цвета шариков
velocity_x_balls = [] # пр. скоростей на оси
velocity_y_balls = [] # пр. скоростей на оси
 
def new_ball(i):
    '''рисует шарики'''
    circle(screen, color_balls[i], (x_balls[i], y_balls[i]), r_balls[i])

def spawn(n):
    '''создаёт заданное число шариковов (1 очко) и белый (10 очков)'''
    for i in range(n):
        x_balls.append(randint(100, 1100))
        y_balls.append(randint(100, 800))
        r_balls.append(randint(10, 100))
        velocity_x_balls.append(randint(-10,10))
        velocity_y_balls.append(randint(-10,10))
        color_balls.append(COLORS[randint(0, 5)])
        new_ball(i)
    x_balls.append(randint(100, 1100))
    y_balls.append(randint(100, 800))
    r_balls.append(randint(10, 100))
    velocity_x_balls.append(randint(-10,10) * 10)
    velocity_y_balls.append(randint(-10,10) * 10)
    color_balls.append(WHITE)
    new_ball(n)

def formate(x_balls, y_balls, r_balls, velocity_x_balls, velocity_y_balls):
    '''list ---> np.array'''
    return (np.array(x_balls), np.array(y_balls), np.array(r_balls),
            np.array(velocity_x_balls), np.array(velocity_y_balls))


def tap(event, amount):
    '''считываем нажатие и определяем, попали ли в шарик'''
    x, y = event.pos
    white_tap = ((x_balls[n] - x)**2 + (y_balls[n] - y)**2) <= ((r_balls[n])**2)
    if max(((x_balls - x)**2 + (y_balls - y)**2) <= ((r_balls)**2)):
        return 1 + 9 * int(white_tap)
    return 0

def move(x_balls, y_balls, velocity_x_balls, velocity_y_balls):
    ''''''
    x_balls += velocity_x_balls
    y_balls += velocity_y_balls
    return x_balls, y_balls

def hit(i):
    '''столкновение со стенами цветных'''
    bool_x = ((x_balls[i] + r_balls[i]) >= 1200) or ((x_balls[i] - r_balls[i]) <= 0)
    bool_y = ((y_balls[i] + r_balls[i]) >= 900) or ((y_balls[i] - r_balls[i]) <= 0)
    if bool_x and (not bool_y): 
        velocity_x_balls[i] = (-1) * velocity_x_balls[i]
        velocity_y_balls[i] = randint(-10,10)
    if bool_y and (not bool_x): 
        velocity_y_balls[i] = (-1) * velocity_y_balls[i]
        velocity_x_balls[i] = randint(-10,10)
    if bool_x and bool_y:
        velocity_x_balls[i] = (-1) * velocity_x_balls[i]
        velocity_y_balls[i] = (-1) * velocity_y_balls[i]
 
def white_hit():
    '''как взаимодействует со стенами белый'''
    x_balls[n], y_balls[n] = (x_balls[n])%1200, (y_balls[n])%900
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False
spawn(n)

x_balls, y_balls, r_balls, velocity_x_balls, velocity_y_balls = formate(
x_balls, y_balls, r_balls, velocity_x_balls, velocity_y_balls)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
            ''''Нажимаем лев. кн. мыши, чтобы кликнуть'''
            print('Click!')
            amount += tap(event, amount)
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 3):
            '''Нажимаем прав. кн. мыши, чтобы вывести счёт'''
            print('Счёт:', amount)
    pygame.display.update()
    screen.fill(BLACK)
    x_balls, y_balls = move(x_balls, y_balls, velocity_x_balls,
                            velocity_y_balls)
    new_ball(n)
    white_hit()
    for i in range(n):
        hit(i)
        new_ball(i)
pygame.quit()
