import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


def draw_body(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)


def draw_eye(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)


def draw_zrachok(surface, x, y, size, color):
    circle(surface, color, (x, y), size // 2)


def draw_mouth(screen, left, top, width, height, color):
    rect(screen, color, (left, top, width, height))


def draw_brovi(screen, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, color):
    polygon(screen, color, [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)])


def draw_all(surface, x, y, size, color_body, color_eye, color_zrachok, color_brovi):

    draw_body(surface, x, y, size, color_body)

    eye_size = 3 * size // 10
    x_eye1 = x - size // 5
    y_eye1 = y - size // 9
    draw_eye(surface, x_eye1, y_eye1, eye_size, color_eye)

    eye_size = 3 * size // 14
    x_eye2 = x + 6 * size // 25
    y_eye2 = y - size // 9
    draw_eye(surface, x_eye2, y_eye2, eye_size, color_eye)

    zrachok_size1 = size // 10
    draw_zrachok(surface, x_eye1, y_eye1, zrachok_size1, color_zrachok)
    zrachok_size2 = size // 14
    draw_zrachok(surface, x_eye2, y_eye2, zrachok_size2, color_zrachok)

    width = size // 2
    height = size // 10
    y_mouth = y + size // 4
    x_mouth = x - width // 2
    draw_mouth(screen, x_mouth, y_mouth, width, height, color_zrachok)

    x1 = x // 2
    y1 = y // 2
    x2 = x1 + size // 20
    y2 = y1 - size // 20
    x3 = x - size // 10
    y3 = y - size // 5
    x4 = x3 + size // 20
    y4 = y3 - size // 20
    draw_brovi(screen, x1, y1, x2, y2, x4, y4, x3, y3, x1, y1, color_brovi)

    x1 = 3 * x // 2
    y1 = y // 2 + y // 15
    x2 = x1 + size // 20
    y2 = y1 + size // 20
    x3 = x + size // 20
    y3 = y - size // 10
    x4 = x3 - size // 20
    y4 = y3 - size // 20
    draw_brovi(screen, x1, y1, x2, y2, x3, y3, x4, y4, x1, y1, color_brovi)

screen.fill((224,224,224))

draw_all(screen, 200, 200, 200, (255, 255, 0), (255, 0, 0), (0, 0, 0), (0, 0, 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
