import pygame
import random

def draw_snake(surface):
    global snake_positions
    for element in snake_positions:
        pygame.draw.rect(surface, (255,0,0), (element[0], element[1], width // rows, width // rows))

def obstacleFirstPosition(surface):
    global square_xpos, square_ypos, width
    separacio = width / rows
    x = random.randint(0,rows-1)
    y = random.randint(0,rows-1)

    while (x*separacio == square_xpos) and (y*separacio == square_ypos):
        x = random.randint(0,rows-1)
        y = random.randint(0,rows-1)

    print("Snake_x:",square_xpos, "-- Snake_y:",square_ypos)
    print("Obstacle_x:",x*separacio, "-- Obstacle_y:",y*separacio)

    return x*separacio, y*separacio

def update_direction(keys, width, rows):
    global direccioX, direccioY
 
    if keys[pygame.K_LEFT] and direccioX != 1:
        direccioX = -1
        direccioY = 0
            
    elif keys[pygame.K_RIGHT] and direccioX != -1:
        direccioX = 1
        direccioY = 0
                    
    elif keys[pygame.K_UP] and direccioY != 1:
        direccioX = 0
        direccioY = -1
             
    elif keys[pygame.K_DOWN] and direccioY != -1:
        direccioX = 0
        direccioY = 1


def move_snake_position(surface, rows,w):
    global square_xpos, square_ypos, direccioX, direccioY, obs_xpos, obs_ypos, snake_positions, pending_positions
    separacio = w / rows
    
    square_xpos = square_xpos + separacio * direccioX
    square_ypos = square_ypos + separacio * direccioY

    if (square_xpos < 0):
        square_xpos = (rows-1)*separacio
    elif (square_xpos >= w):
        square_xpos = 0
    elif (square_ypos < 0):
        square_ypos = (rows-1)*separacio
    elif (square_ypos >= w):
        square_ypos = 0

    snake_positions = [[square_xpos, square_ypos]] + snake_positions
    snake_positions.pop(len(snake_positions)-1)


    if len(pending_positions) != 0:
        if pending_positions[0] not in snake_positions:
            snake_positions += [pending_positions.pop(0)]


    if(square_xpos == obs_xpos) and (square_ypos == obs_ypos):
        obs_xpos, obs_ypos = obstacleFirstPosition(surface)
        pending_positions = pending_positions + [[square_xpos,square_ypos]]



def snakeFirstPosition(w, rows, surface):
    separacio = w / rows
    x = random.randint(0,rows-1)
    y = random.randint(0,rows-1)

    return x*separacio, y*separacio


def drawGrid(w, rows, surface):
    separacio = w / rows
    acumulat = separacio
    for i in range(rows -1):
        pygame.draw.line(surface, (255,255,255),(0,acumulat),(w,acumulat))
        pygame.draw.line(surface, (255,255,255),(acumulat,0),(acumulat,w))
        acumulat += separacio
    

 
def redrawWindow(surface):
    global rows, width, square_xpos, square_ypos, obs_xpos, obs_ypos
    surface.fill((0,0,0))
    drawGrid(width,rows, surface)
    move_snake_position(surface, rows, width)
    pygame.draw.rect(surface, (0,255,0), (obs_xpos, obs_ypos, width // rows, width // rows))
    draw_snake(surface)
    #pygame.draw.rect(surface, (255,0,0), (square_xpos, square_ypos, width // rows, width // rows))
    pygame.display.update()


def main():
    global width, rows, square_xpos, square_ypos, direccioX, direccioY, obs_xpos, obs_ypos, snake_positions, pending_positions
    pygame.init()

    width = 600
    rows = 10

    win = pygame.display.set_mode((width,width))

    pygame.display.set_caption("SNAKE")

    square_xpos, square_ypos = snakeFirstPosition(width, rows, win)
    snake_positions = [[square_xpos, square_ypos]]
    pending_positions = []
    obs_xpos, obs_ypos = obstacleFirstPosition(win)

    direccioX = 1
    direccioY = 0

    run = True
    while run:
        pygame.time.delay(70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            update_direction(pygame.key.get_pressed(),width,rows)
        
        redrawWindow(win)
        
    pygame.quit()
    
main()
