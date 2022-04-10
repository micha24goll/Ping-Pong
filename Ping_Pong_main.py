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
window = display.set_mode((wind_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
#Create window settings
racket1 = Player('racket.png', 30, 200 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball1 = GameSprite('tennis_ball.png' 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 Lose!', True, (180, 0, 0))
lose2 = font.render('Player 2 Lose!', True, (180, 0, 0))

speed_x = 5
speed_y = 5
#Create players and fonts.
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_1()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or vall.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket1.reset()
        racket2.reset()
        ball.reset()

display.update()
clock.tick(FPS)

#Create end
