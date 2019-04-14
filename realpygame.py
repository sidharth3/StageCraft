import pygame
import sys
pygame.init()

bg = pygame.image.load(r"c:\users\sudharshan\pictures\bg.jpg")
bg = pygame.transform.scale(bg, (640, 480))
bgrect = bg.get_rect()

img3 = pygame.image.load(r'c:\users\sudharshan\pictures\bullet.png')
img3 = pygame.transform.scale(img3, (60, 60))
img4 = img3
img1 = pygame.image.load(r"c:\users\sudharshan\downloads\player.png")
img1 = pygame.transform.scale(img1, (160, 120))
img2 = pygame.transform.flip(img1, True, False)
health1 = pygame.image.load(r'c:\users\sudharshan\pictures\health.png')
health2 = pygame.image.load(r'c:\users\sudharshan\pictures\health1.png')
h1rect = health1.get_rect()
h2rect = health2.get_rect()
w = 640
h = 480
h2rect = h2rect.move(w-200, 0)

bar1 = [200, 20] # Dimensions of healthbars
bar2 = [200, 20]


coolrect = img3.get_rect()
coolrect2 = img4.get_rect()
health1 = pygame.transform.scale(health1, bar1)
health2 = pygame.transform.scale(health2, bar2)


speed1 = [0,0]
speed2 = [0,0]

screen = pygame.display.set_mode((w, h))

coolrect = coolrect.move(0,370)
coolrect2 = coolrect2.move(600,370)                        

black = 255, 255, 255

font = pygame.font.SysFont('Ariel', 30)
def text_disp(x):
    return font.render(x, False, (0, 0, 0))

def reduce1(x):
    bar1[0] -= x
    
def reduce2(x):
    h2rect.move_ip(1, 0)
    bar2[0] -= x

emotion = "Test" # Any emotion
ct = "3"

while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speed1[0]=10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speed2[0]-=10
    
    if (bar1[0] <= 0 or bar2[0] <= 0):
        pygame.display.quit()
        sys.exit()
        break
    
    screen.fill(black)
    screen.blit(bg, bgrect)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        reduce1(1)
    
    if keys[pygame.K_LEFT]:
        reduce2(1)
    
    health1 = pygame.transform.scale(health1, bar1)
    health2 = pygame.transform.scale(health2, bar2)
    
    screen.blit(health1, h1rect)
    screen.blit(health2, h2rect)   

    text = text_disp(emotion) # Text emotion  
    text2 = text_disp(ct) # Countdown
    
    coolrect = coolrect.move(speed1)
    if coolrect.left<= w:
        screen.blit(img3,coolrect)
        screen.blit(img4,coolrect2)
        
    screen.blit(text, (w/2 - 30, h/2 - 30))
    
    screen.blit(img1,(0,h-120))
    
    screen.blit(img2,(w-160,h-120))
    
    screen.blit(text2, (w/2 - 15, h/2))
    pygame.display.flip()
