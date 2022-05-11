from pygame import * 
from random import *

win_width = 700
win_height = 500
window = display.set_mode((700,500))
display.set_caption('E') 

lost = 0
score = 0
max_lost = 5
max_score = 50

bullets = sprite.Group()

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


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed