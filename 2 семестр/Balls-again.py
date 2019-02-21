import sys
import pygame

pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ball')
clock = pygame.time.Clock()

coord_x = 30
coord_y = 30
speedx = 50
speedy = 50
r = 20
x_second = 300
y_second = 400
speedx_second = 165
speedy_second = 165

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #отталкивание шариков
    if coord_x >= width - r or coord_x < r:                    
        speedx = -speedx
    if coord_y >= height - r or coord_y < r:
        speedy = -speedy

    if x_second >= width - r or x_second < r:      
        speedx_second = -speedx_second
    if y_second >= height - r or y_second < r:
        speedy_second = -speedy_second

    #прописываем ускорение по кнопкам
    if pygame.key.get_pressed()[pygame.K_UP]:      
        speedy-=5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        speedy+=5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        speedx-=5
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        speedx+=5

    #Добавим сопротивление воздуха
    speedx *= 0.97                                    
    speedy *= 0.97

    #И определение цвета
    rgb_red = (speedx ** 2 + speedy ** 2) ** 0.5                    
    if rgb_red > 255:
        rgb_red = 255

    balls_dist = (abs(coord_x - x_second) ** 2 + abs(coord_y - y_second) ** 2) ** 0.5
    if balls_dist<2*r:
        lenx = abs(speedx - vx_second)
        leny = abs(speedy - y_second)
        speedy1 = speedy - 2 * speedy * leny / ((speedx ** 2 + speedy ** 2) ** 0.5)
        speedx1 = speedx - 2 * speedx * leny/ ((speedx ** 2 + speedy ** 2) ** 0.5)
        speedy_second -= speedy * leny/((speedx_second ** 2 + speedy_second ** 2) ** 0.5)
        speedx_second -= speedx * leny/((speedx_second ** 2 + speedy_second ** 2) ** 0.5)

    coord_x += speedx * dt
    coord_y += speedy * dt

    x_second += speedx_second * dt
    y_second += speedy_second * dt

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (int(rgb_red), 100, 100), (int(coord_x), int(coord_y)), int(r))
    pygame.draw.circle(screen, (235, 100, 100), (int(x_second), int(y_second)), int(r))

    pygame.display.flip()
