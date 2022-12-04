import pgzrun

from random import randint


WIDTH = 800
HEIGHT = 800


#Các biến: 
score = 0
gameover = 0

bowl = Actor ('bowl')
bowl.x = 350
bowl.y = 350

apple = Actor ('apple')
apple.x = 400
apple.y = 0



def on_mouse_move (pos,rel,buttons):
    bowl.x = pos[0]
    bowl.y = pos[1]

def update():
    global score, gameover
    apple.y = apple.y + score/10
    if apple.colliderect(bowl):
        apple.x = randint(0 , 800)
        apple.y = 0
        score = score + 10
        sounds.killsound.play()
    if (apple.y > 800):
        gameover = gameover + 1
    else:
        gameover = 0

def draw():
    if gameover == 1:
        screen.draw.text('Quá Non!',(300,300), color = (255,0,0) , fontsize = 60)
        screen.draw.text('Your Score: '+str(score), (290,400) ,color = (255,0,0), fontsize = 50)
    elif gameover == 0:
        screen.fill((0,255,255))
        bowl.draw()
        apple.draw()       
        screen.draw.text('Score: '+str(score), (0,0) , color = (255,0,0), fontsize = 50)




pgzrun.go()