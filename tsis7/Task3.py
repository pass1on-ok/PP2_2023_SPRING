import pygame


pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")


ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_color = (255, 0, 0)


key_bindings = {
    pygame.K_UP: (0, -20),
    pygame.K_DOWN: (0, 20),
    pygame.K_LEFT: (-20, 0),
    pygame.K_RIGHT: (20, 0),
}


clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key in key_bindings:
                dx, dy = key_bindings[event.key]
                new_x = ball_x + dx
                new_y = ball_y + dy
                if 0 <= new_x - ball_radius <= screen_width and \
                   0 <= new_y - ball_radius <= screen_height:
                    ball_x = new_x
                    ball_y = new_y

    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

    
    clock.tick(60)  
