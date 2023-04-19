import pygame
import random

def update_direction(keys, width, rows):
    global direccioX, direccioY
    if keys[pygame.K_LEFT]:
        direccioX = -1
        direccioY = 0
    elif keys[pygame.K_RIGHT]:
        direccioX = 1
        direccioY = 0
    elif keys[pygame.K_UP]:
        direccioX = 0
        direccioY = -1
    elif keys[pygame.K_DOWN]:
        direccioX = 0
        direccioY = 1
    pass

def move_snake_position(rows,w):
    global square_xpos, square_ypos, direccioX, direccioY
    square_xpos += direccioX*width//rows
    square_ypos += direccioY*width//rows

    if square_xpos >= width:
        square_xpos = 0
    elif square_xpos < 0:
        square_xpos = width-width//rows
    if square_ypos >= width:
        square_ypos = 0
    elif square_ypos < 0:
        square_ypos = width- width//rows

def move_position(xpos,ypos, width, rows):
    # INSERT YOUR CODE HERE
    pass

def snakeFirstPosition(w, rows, surface):
    
    return random.randint(0,rows)*width//rows, random.randint(0,rows)*width//rows

def drawGrid(w, rows, surface):
    for pos in range(1,rows):
        pygame.draw.line(surface,(255,255,255),(0,pos*(width//rows)), (width,pos*(width//rows)))
        pygame.draw.line(surface,(255,255,255),(pos*(width//rows),0), (pos*(width//rows), width))
    pass

 
def redrawWindow(surface):
    global rows, width, square_xpos, square_ypos
    surface.fill((0,0,0))
    drawGrid(width,rows, surface)
    move_snake_position(rows, width)
    pygame.draw.rect(surface, (255,0,0),pygame.Rect(square_xpos,square_ypos,width//rows, width//rows))
    print(square_xpos, square_ypos)
    pygame.display.update()

def main():
    global width, rows, square_xpos, square_ypos, direccioX, direccioY
    pygame.init()

    width = 500
    rows = 60
    
    win = pygame.display.set_mode((width,width))

    pygame.display.set_caption("SNAKE")

    square_xpos, square_ypos = snakeFirstPosition(width, rows, win)

    direccioX = 1
    direccioY = 0

    run = True
    while run:
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            update_direction(pygame.key.get_pressed(),width,rows)
        
        
        
        redrawWindow(win)
        
    pygame.quit()
        
    
main()
