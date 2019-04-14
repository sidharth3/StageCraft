from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import random
import pygame
import numpy as np
import time
import sys
from pygame.locals import*
pygame.font.init()
font = pygame.font.SysFont('Ariel', 30)
def text_disp(x):
    return font.render(x, False, (0, 0, 0))


def loops():
    
    pygame.init()

# Load backgroung, bullet, player images
    
    bg = pygame.image.load("bg.jpg")
    
    bg = pygame.transform.scale(bg, (640, 480))
    
    # Make BG-object 
    bgrect = bg.get_rect()
    
    # Load left, right bullet 
    bullet_right = pygame.image.load('bullet.png')
    bullet_right = pygame.transform.scale(bullet_right, (60, 60))
    
    bullet_left = pygame.transform.flip(bullet_right, True, False)
    player_right = pygame.image.load("player.png")
    
    player_right = pygame.transform.scale(player_right, (160, 120))
    player_left = pygame.transform.flip(player_right, True, False)
    
    health1 = pygame.image.load('health.png')
    health2 = pygame.image.load('health1.png')
    
    h1rect = health1.get_rect()
    h2rect = health2.get_rect()
    
    w = 640
    h = 480
    
    h2rect = h2rect.move(w-200, 0)
    
    bar1 = [200, 20] # Dimensions of healthbars
    bar2 = [200, 20]
    
    
    coolrect = bullet_right.get_rect()
    coolrect2 = bullet_left.get_rect()
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
        bullet_to_left()
        
    def reduce2(x):
        h2rect.move_ip(1, 0)
        bar2[0] -= x
        bullet_to_right()
        
    def bullet_to_right():
        speed1[0] = 200
            
    def bullet_to_left():
        speed2[0] = -200
    
    emotion = "Test" # Any emotion
    ct = "3"

    # parameters for loading data and images
    detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
    emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'
    
    # hyper-parameters for bounding boxes shape
    # loading models
    face_detection = cv2.CascadeClassifier(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
     "neutral"]
    
    EMOTIONSS = ["angry" , "happy" , "sad" , "neutral"]
    #feelings_faces = []
    #for index, emotion in enumerate(EMOTIONS):
       # feelings_faces.append(cv2.imread('emojis/' + emotion + '.png', -1))
    
    # starting video streaming
    cv2.namedWindow('your_face')
    starttime = time.time()
    elapsedtime = random.randint(1,3)
    emote = random.choice(EMOTIONSS)
    camera = cv2.VideoCapture(0)
    enemyhealth = 700
    playerhealth = 700
    score = 0
    text = text_disp(emote)
    
    # player_rect
    
    pl_left_rect = player_left.get_rect()
    pl_left_rect = pl_left_rect.move(465, 355)
    
    # text_rect
    
    fake = health1
    fake = pygame.transform.scale(fake, (0, 0))
    fake_rect = fake.get_rect()
    fake_rect = fake_rect.move(w/2, h/2)
    fake_rect2 = fake_rect
    fake_rect2 = fake_rect2.move(10, 25)
    
    
    while 1:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            """if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bullet_to_right()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    bullet_to_left()"""
        
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
            
        if coolrect.left >= w:
            speed1[0] = 0
            coolrect = coolrect.move(-580, 0)
            
        if coolrect2.right <= 0:
            speed2[0] = 0
            coolrect2 = coolrect2.move(580, 0)
        
        #bullet_to_right()
        #bullet_to_left()
        
        health1 = pygame.transform.scale(health1, bar1)
        health2 = pygame.transform.scale(health2, bar2)
        
        screen.blit(health1, h1rect)
        screen.blit(health2, h2rect)   
    
        text = text_disp(emote) # Text emotion  
        text2 = text_disp(str(int(elapsedtime +starttime - time.time()))) # Countdown
        
        coolrect = coolrect.move(speed1)
        coolrect2 = coolrect2.move(speed2)
        
        screen.blit(bullet_right, coolrect)
        screen.blit(bullet_left, coolrect2)
        
        screen.blit(text, fake_rect)
        
        screen.blit(player_right,(0,h-120))
        
        screen.blit(player_left,pl_left_rect)
        
        screen.blit(text2, fake_rect2)
        pygame.display.flip()

        
    
    
        ret, frame = camera.read()
        #reading the frame
        if ret:
            frame = imutils.resize(frame,width=300)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
            
            if(time.time() - starttime <elapsedtime):
                print("show "+emote+"for " + str(elapsedtime)+"seconds")
            else:
                starttime = time.time()
                emote = random.choice(EMOTIONSS)
                elapsedtime = random.randint(1,3)
                pygame.mixer.music.load(str(elapsedtime)+".mpeg")
                pygame.mixer.music.play()
            
            canvas = np.zeros((250, 300, 3), dtype="uint8")
            frameClone = frame.copy()
            if len(faces) > 0:
                faces = sorted(faces, reverse=True,
                key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
                (fX, fY, fW, fH) = faces
                            # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
                    # the ROI for classification via the CNN
                roi = gray[fY:fY + fH, fX:fX + fW]
                roi = cv2.resize(roi, (64, 64))
                roi = roi.astype("float") / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                
                
                preds = emotion_classifier.predict(roi)[0]
                emotion_probability = np.max(preds)
                label = EMOTIONS[preds.argmax()]
                
                
                print(label)
                print(playerhealth)
                print(enemyhealth)
                if(label == emote):
                    reduce2(3)
                    enemyhealth = enemyhealth - 10
                else:
                    if(label == "sad" and (emote =="scared" or emote =="disgusted")):
                        enemyhealth = enemyhealth -10
                        reduce2(3)
                    else:
                        playerhealth -=10
                        reduce1(3)
                if playerhealth <0:
                    break
                
            else:
                
                break
        
         
            for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                        # construct the label text
                        text = "{}: {:.2f}%".format(emotion, prob * 100)
        
                        # draw the label + probability bar on the canvas
                       # emoji_face = feelings_faces[np.argmax(preds)]
        
                        
                        w = int(prob * 300)
                        cv2.rectangle(canvas, (7, (i * 35) + 5),
                        (w, (i * 35) + 35), (0, 0, 255), -1)
                        cv2.putText(canvas, text, (10, (i * 35) + 23),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                        (255, 255, 255), 2)
                        cv2.putText(frameClone, label, (fX, fY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                        
                        cv2.putText(canvas, "Score : " + str(score), (fX, fY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                        cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                                      (0, 0, 255), 2)
                        cv2.imshow('your_face', frameClone)
                        cv2.imshow("Probabilities", canvas)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    
        #    for c in range(0, 3):
        #        frame[200:320, 10:130, c] = emoji_face[:, :, c] * \
        #        (emoji_face[:, :, 3] / 255.0) + frame[200:320,
        #        10:130, c] * (1.0 - emoji_face[:, :, 3] / 255.0)
        
        else:
            print("no cam")
            continue
        
    
    camera.release()
    cv2.destroyAllWindows()
    pygame.quit()
