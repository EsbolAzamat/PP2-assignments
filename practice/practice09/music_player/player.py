import pygame
import os

pygame.init()

W = 800
H = 480

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

playlist = [i for i in os.listdir("music") if i.endswith(".mp3")]
current = 0

pygame.mixer.music.load("music/" + playlist[current])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            
            if event.key == pygame.K_s:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()

            if event.key == pygame.K_n:
                current = (current + 1) % len(playlist)
                pygame.mixer.music.load("music/" + playlist[current])
                pygame.mixer.music.play()

            if event.key == pygame.K_b:
                current = (current - 1) % len(playlist)
                pygame.mixer.music.load("music/" + playlist[current])
                pygame.mixer.music.play()

            if event.key == pygame.K_q:
                running = False

        
        screen.fill('black')
        font = pygame.font.SysFont("Verdana", 20)
        track = "Track: " +  playlist[current]

        screen.blit(font.render(track, True, 'white'), (20, 100))
        screen.blit(font.render("P-play S-stop N-next B-back Q-quit", True, "white"), (20, 150))


        pygame.display.flip()
pygame.quit()