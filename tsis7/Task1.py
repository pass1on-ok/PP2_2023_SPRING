import pygame
import time
import math

# Initialize Pygame
pygame.init()

# Set the window size and title
size = (700, 700)
pygame.display.set_caption("Mickey Mouse Clock")

# Load the Mickey Mouse image
mickey_image = pygame.image.load("mickeyclock1.jpeg")

# Define the clock positions
center_x = size[0] // 2
center_y = size[1] // 2
radius = min(center_x, center_y) - 50

# Create a Pygame window
screen = pygame.display.set_mode(size)

# Set the clock font and color
font = pygame.font.SysFont(None, 48)
color = (255, 255, 255)

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get the current time
    current_time = time.localtime()

    # Calculate the angles of the hands
    seconds_angle = math.radians(current_time.tm_sec * 6 - 90)
    minutes_angle = math.radians(current_time.tm_min * 6 - 90)

    # Rotate the Mickey Mouse image
    seconds_hand = pygame.transform.rotate(mickey_image, math.degrees(seconds_angle))
    minutes_hand = pygame.transform.rotate(mickey_image, math.degrees(minutes_angle))

    # Draw the clock face
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, (center_x, center_y), radius, 5)

    # Draw the hands
    screen.blit(seconds_hand, (center_x - seconds_hand.get_width() // 2, center_y - seconds_hand.get_height() // 2))
    screen.blit(minutes_hand, (center_x - minutes_hand.get_width() // 2, center_y - minutes_hand.get_height() // 2))

    # Update the clock text
    clock_text = font.render(time.strftime("%I:%M:%S %p"), True, (0,0,0))
    screen.blit(clock_text, (size[0] // 2 - clock_text.get_width() // 2, size[1] // 2 + radius + 10))

    # Update the display
    pygame.display.flip()

    # Wait for one second
    time.sleep(1)
