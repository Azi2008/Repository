from pygame import *
import classes
import pygame

pygame.font.init()


class GameSprite(sprite.Sprite):
    def __init__(self,picture,x,y,width,height,speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width,height))
        self.speed = speed
        self.height = height
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image , (self.rect.x, self.rect.y))


ball = GameSprite('floppa.png',310,210,70,100,4)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -90:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        self.rect.y = ball.rect.y
score = 0

speed_x = 8
speed_y = 8

angle = 5

win_width = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption('da')
FPS = 60
clock = time.Clock()

player = Player('shlopanci.png', 40,200, 70,100,8)
player2 = Player2('shlopanci.png', 600,200, 70,100,6)
background = transform.scale(image.load('космос.jpg'),(700,500))

f1 = pygame.font.Font(None, 36)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if not finish:

        window.blit(background,(0,0))

        ball.reset()
        
        player.update()
        player.reset()
        player2.update()
        player2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

                
        text = f1.render("Шлепков: " + str(score),True,(255,160,0))
        window.blit(text,(10,20))

        text = f1.render("Не дай Шлёпе уйти!",True,(255,160,0))
        window.blit(text,(250,20))
        
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player,ball) or sprite.collide_rect(player2,ball):
            speed_x *= -1
        if sprite.collide_rect(player,ball):
            score += 1
        
        if ball.rect.x < 0 or ball.rect.x > 650:
            finish = True
            text = f1.render("Шлёпа поглотил Планету и пельмени!",True,(255,0,0))
            window.blit(text,(130,250))


    
        display.update()
        clock.tick(60)
