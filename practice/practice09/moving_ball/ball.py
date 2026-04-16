import pygame

pygame.init()

W = 800
H = 480
R = 25

screen = pygame.display.set_mode((W, H))

running = True
circle_x = W//2
circle_y = H//2
clock = pygame.time.Clock()
FPS = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        circle_y -= 20
    if pressed_keys[pygame.K_DOWN]:
        circle_y += 20
    if pressed_keys[pygame.K_LEFT]:
        circle_x -= 20
    if pressed_keys[pygame.K_RIGHT]:
        circle_x += 20


    if circle_x - R < 0:
        circle_x = R
    if circle_x + R > W:
        circle_x = W - R
    if circle_y - R < 0:
        circle_y = R
    if circle_y + R > H:
        circle_y = H - R


    screen.fill('white')    
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), R)
    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()