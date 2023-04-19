import pygame
import random

def update_direction(keys, width, rows):
    global direccioX, direccioY
    
    pass

def move_snake_position(rows,w):
    global square_xpos, square_ypos, direccioX, direccioY
    # INSERT YOUR OPTIONAL CODE HERE

def move_position(xpos,ypos, width, rows):
    # INSERT YOUR CODE HERE
    pass

def snakeFirstPosition(w, rows, surface):
    x = random.randint(0,rows)
    y = random.randint(0,rows)
    return x,y

def drawGrid(w, rows, surface):
    sep = width/rows
    for posicio in range(rows):
        pos_inicial_x = (0+posicio*sep,0)
        pos_final_x = (0+posicio*sep,500)
        pos_inicial_y = (0,0+posicio*sep)
        pos_final_y = (500,posicio*sep)
        pygame.draw.line(surface,(255,255,255),pos_inicial_x, pos_final_x)
        pygame.draw.line(surface,(255,255,255),pos_inicial_y, pos_final_y)


 
def redrawWindow(surface):
    global rows, width, square_xpos, square_ypos
    surface.fill((0,0,0))
    drawGrid(width,rows, surface)
    move_snake_position(rows, width)
    pygame.draw.rect(surface,(255,0,0),pygame.Rect(square_xpos*width/rows,square_ypos*width/rows,width/rows,width/rows))
    pygame.display.update()

def main():
    global width, rows, square_xpos, square_ypos, direccioX, direccioY
    pygame.init()

    width = 500
    rows = 20
    
    win = pygame.display.set_mode((width,width))

    pygame.display.set_caption("SNAKE")

    square_xpos, square_ypos = snakeFirstPosition(width, rows, win)


    direccioX = 1
    direccioY = 0

    run = True
    while run:
        pygame.time.delay(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            update_direction(pygame.key.get_pressed(),width,rows)
        
        redrawWindow(win)
        
    pygame.quit()
        
    
main()
