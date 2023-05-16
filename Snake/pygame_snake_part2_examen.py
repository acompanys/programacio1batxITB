import pygame
import random

def update_direction(keys, width, rows):
    #S'encarrega d'actualitzar la direcció de la serp
    global direccioX, direccioY
    if keys[pygame.K_LEFT] and (not(direccioX == 1)):
        direccioX = -1
        direccioY = 0
    elif keys[pygame.K_RIGHT] and (not(direccioX == -1)):
        direccioX = 1
        direccioY = 0
    elif keys[pygame.K_UP] and (not(direccioY == 1)):
        direccioX = 0
        direccioY = -1
    elif keys[pygame.K_DOWN] and (not(direccioY == -1)):
        direccioX = 0
        direccioY = 1

def move_snake_position(rows,w):
    #S'encarrega del moviment de la serp
    global snake, direccioX, direccioY

    for pos in range(len(snake)-1):
        snake[len(snake)-1-pos][0]=snake[len(snake)-pos-2][0]
        snake[len(snake)-1-pos][1]=snake[len(snake)-pos-2][1]

    snake[0][0] += direccioX
    snake[0][1] += direccioY

    if snake[0][0] >= rows:
        snake[0][0] = 0
    elif snake[0][0] < 0:
        snake[0][0] = rows-1
    if snake[0][1] >= rows:
        snake[0][1] = 0
    elif snake[0][1] < 0:
        snake[0][1] = rows-1

def enlarge_snake(snake):
    #S'encarrega de fer més gran la serp
    global direccioX, direccioY, width, rows

    snake.append([snake[len(snake)-1][0]-direccioX, snake[len(snake)-1][1]-direccioY])
    return snake

def snakeFirstPosition(w, rows, surface):
    #Crea la posició inicial de la serp
    return [[random.randint(0,rows-1), random.randint(0,rows-1)]]

def apple_first_pos(rows):
    #Crea la posició inicial de la serp
    return random.randint(0,rows-1),random.randint(0,rows-1)

def drawGrid(w, rows, surface):
    #Dibuixa la graella
    for pos in range(1,rows):
        pygame.draw.line(surface,(255,255,255),(0,pos*(width//rows)), (width,pos*(width//rows)))
        pygame.draw.line(surface,(255,255,255),(pos*(width//rows),0), (pos*(width//rows), width))

def draw_snake(surface, snake):
    #Dibuixa la serp
    for pos in snake:
        pygame.draw.rect(surface, (255,0,0),pygame.Rect(pos[0]*width/rows,pos[1]*width/rows,width/rows, width/rows))

def draw_apple(surface, x, y):
    #Dibuixa la poma
    pygame.draw.rect(surface, (0,255,0),pygame.Rect(x*width/rows,y*width/rows,width/rows, width/rows))

def check_end_game(snake):
    #Comprova si s'ha acabat la partida
    for pos1 in range(len(snake)):
        for pos2 in range(len(snake)):
            if (not pos1==pos2) and (snake[pos1][0] == snake[pos2][0]) and (snake[pos1][1]==snake[pos2][1]):
                return True
    return False

def redrawWindow(surface):
    #Actualitza la pantalla
    global rows, width, snake, apple_x, apple_y
    surface.fill((0,0,0))
    drawGrid(width,rows, surface)
    move_snake_position(rows, width)
    draw_apple(surface, apple_x, apple_y)
    draw_snake(surface,snake)
    pygame.display.update()

def main():
    #Funció principal
    global width, rows
    global snake, direccioX, direccioY, apple_x, apple_y
    global score

    pygame.init()
    width = 500
    rows = 20
    win = pygame.display.set_mode((width,width))
    pygame.display.set_caption("SNAKE by Albert")

    snake = snakeFirstPosition(width, rows, win)
    apple_x, apple_y = apple_first_pos(rows)

    direccioX = 1
    direccioY = 0
    score = 0

    run = True
    #Bucle principal
    while run:
        pygame.time.delay(150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            update_direction(pygame.key.get_pressed(),width,rows)

        #Comprovació de si es troba la poma
        if(snake[0][0]==apple_x and snake[0][1]==apple_y):
            apple_x, apple_y = apple_first_pos(rows)
            score += 1
            snake = enlarge_snake(snake)
            
        
        if (check_end_game(snake)):
            print("Game Over!", "Score: "+str(score))
            apple_x, apple_y = apple_first_pos(rows)
            snake = snakeFirstPosition(width, rows, win)
            score = 0
            run = False
        redrawWindow(win)

    pygame.quit()
        
    
main()
