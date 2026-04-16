import pygame
import datetime

pygame.init()

W = 800
H = 800
center = (W // 2, H // 2)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

image_clock = pygame.image.load("images/clock.png").convert_alpha()
mickey = pygame.image.load("images/mickey.png").convert_alpha()
hand_l = pygame.image.load("images/hand_left_centered.png").convert_alpha()
hand_r = pygame.image.load("images/hand_right_centered.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    now = datetime.datetime.now()
    m = now.minute
    s = now.second


    minutes_angle = -(m * 6 + s * 0.1)
    second_angle   = -(s * 6)

    
    rotated_minutes = pygame.transform.rotate(hand_l, minutes_angle)
    rotated_hours   = pygame.transform.rotate(hand_r, second_angle)

    
    clock_rect = image_clock.get_rect(center=center)
    mickey_rect = mickey.get_rect(center=center)
    minutes_rect = rotated_minutes.get_rect(center=center)
    hours_rect = rotated_hours.get_rect(center=center)

    
    screen.fill((255, 255, 255))

    screen.blit(image_clock, clock_rect)
    screen.blit(mickey, mickey_rect)
    screen.blit(rotated_hours, hours_rect)
    screen.blit(rotated_minutes, minutes_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print(hours_rect)