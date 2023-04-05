import pygame
from pygame.locals import * 
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    radius = 10
    x = 0
    y = 0
    points = []
    mousepos = None
    while True:
        screen.fill((255,255,255))
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    return draw_rectangle()
                if event.key == pygame.K_l:
                    return draw_line()
                if event.key == pygame.K_c:
                    return draw_circle()
        pygame.display.flip()
        
        clock.tick(60)
        
def draw_line():    
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    radius = 5
    x = 0
    y = 0
    points = []
    drawing = False
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    mode = BLACK
    while True:

        screen.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    return draw_rectangle()
                if event.key == pygame.K_l:
                    return draw_line()
                if event.key == pygame.K_c:
                    return draw_circle()
                # determine if a letter key was pressed
                
                if event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
                
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        pygame.display.flip()
        
        clock.tick(60)
        
def drawLineBetween(screen, index, start, end, width,color_mode):
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    mode = BLACK
    if color_mode == BLACK:
        color = (0, 0, 0)
    elif color_mode == BLUE:
        color = (0, 0, 255)
    elif color_mode == GREEN:
        color = (0,0,255)
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

        
def draw_rectangle():
    mousepos = None
    boxes = []
    clock = pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((640, 480))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    mode = BLACK
    while 1:

        screen.fill(WHITE)

        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                mousepos = [event.pos[0], event.pos[1], 0, 0]


            if event.type == MOUSEBUTTONUP:
                boxes.append(mousepos)
                mousepos = None

            if event.type == MOUSEMOTION and mousepos != None:
                mousepos = [mousepos[0], mousepos[1], event.pos[0] - mousepos[0], event.pos[1] - mousepos[1]]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    mode = GREEN
                if event.key == pygame.K_b:
                    mode = BLUE
                if event.key == pygame.K_r:
                    return draw_rectangle()
                if event.key == pygame.K_l:
                    return draw_line()
                if event.key == pygame.K_c:
                    return draw_circle()
        for box in boxes:
            pygame.draw.rect(screen, mode, box, 1)

        if mousepos != None:
            pygame.draw.rect(screen, mode, mousepos, 1)
def draw_circle():
    start = (0, 0)
    size = (0, 0)
    drawing = False
    mousepos = None
    boxes = []
    clock = pygame.time.Clock()
    FPS = 60
    screen = pygame.display.set_mode((640, 480))
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    mode = BLACK
    while 1:

        screen.fill(WHITE)

        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                start = event.pos
                size = 0, 0
                drawing = True

            elif event.type == MOUSEBUTTONUP:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
                cir = (start,size)
                boxes.append(cir)
                drawing = False
            elif event.type == MOUSEMOTION and drawing:
                end = event.pos
                size = end[0] - start[0], end[1] - start[1]
      
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    mode = GREEN
                if event.key == pygame.K_b:
                    mode = BLUE
                if event.key == pygame.K_r:
                    return draw_rectangle()
                if event.key == pygame.K_l:
                    return draw_line()
                if event.key == pygame.K_c:
                    return draw_circle()

        for circ in boxes:
            pygame.draw.ellipse(screen, mode, circ, 3)
        pygame.draw.ellipse(screen, mode, (start, size), 2)
        pygame.display.update()
        clock.tick(FPS)
    

main()
