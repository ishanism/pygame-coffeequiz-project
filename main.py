# 1-Import library
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

global q,score
q = 1
score = 0

def wrongAns():
    Tk().wm_withdraw()
    messagebox.showinfo('WRONG', 'Sad, You got it wrong!!!')

def rightAns():
    Tk().wm_withdraw()
    messagebox.showinfo('Correct', 'Wohooo You got it correct')
    global score
    score += 1

def checkAns(mousePos):
    if (mousePos[0] in range(64, 261)) and (mousePos[1] in range(329, 390)):
        global q
        if q == 1 or q == 3:
            correctAudio.play()
            rightAns()
        else:
            wrongAudio.play()
            wrongAns()
        q+=1
    elif (mousePos[0] in range(380, 577)) and (mousePos[1] in range(329, 390)):
        global q
        if q == 2:
            correctAudio.play()
            rightAns()
        else:
            wrongAudio.play()
            wrongAns()
        q+=1

# 2 – Initialize the game


pygame.init()
pygame.mixer.init()
wrongAudio = pygame.mixer.Sound("resources/wrong.ogg")
correctAudio = pygame.mixer.Sound("resources/correct.ogg")

width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# 3 – Load images
bgImage = pygame.image.load("resources/Coffee.jpg")
question1 = pygame.image.load("resources/question1.png")
question2 = pygame.image.load("resources/question2.png")
question3 = pygame.image.load("resources/question3.png")

screen.blit(bgImage, (0, 0))
pygame.display.flip()
Tk().wm_withdraw()  # to hide the main window
messagebox.showinfo("Coffee Quiz", "Let's Start the Coffee Quiz")

# 4 – Keep looping through
while 1:

    # 5 – Clear the screen before drawing it again
    screen.fill(0)

    # 6 - Draw the screen elements
    if q == 1:
        screen.blit(question1, (0, 0))
    elif q == 2:
        screen.blit(question2, (0, 0))
    elif q == 3:
        screen.blit(question3, (0, 0))
    elif q > 3:
        finalMessage = "Game Over!!!! Your Score is " + str(score) + " out of 3"
        Tk().wm_withdraw()  # to hide the main window
        messagebox.showinfo("Game Over", finalMessage)
        pygame.quit()
        exit(0)

    # 7 – Update the screen
    pygame.display.flip()

    # 8 – Loop through the events
    for event in pygame.event.get():

    # Check if the event is the X button
        if event.type==pygame.QUIT:

    # If it is quit the game
            Tk().wm_withdraw()  # to hide the main window
            messagebox.showinfo('Close Initialized', 'Thank you for Playing the Game. Play again next time!!!')
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            checkAns(mousePos)
            break

exit(0)