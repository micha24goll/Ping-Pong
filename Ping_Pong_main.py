from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, weidht, height):

        self.image = transform.scale(image.load(player_image), (weidht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
  #Create class 'GameSprite'.
class Player(GameSparite):
    def update_r(self):
        keys = key.got_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height = 80:
            self.rect.y += self.speed
        
   def update_r(self):
        keys = key.got_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height = 80:
            self.rect.y += self.speed
            
     #Create class 'Player'
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set.made((wind_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
#Create window settings
