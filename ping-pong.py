from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, img, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (100,100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(Gamesprite):
    def __init__(self, img, speed, x, y):
        super().__init__(img, speed, x, y)
    def moving(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_a] and self.rect.y > 630:
            self.rect.x += self.speed

window = display.set_mode((700, 500))
class Player2(Gamesprite):
    def __init__(self, img, speed, x, y):
        super().__init__(img, speed, x, y)
    def moving(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_a] and self.rect.y > 630:
            self.rect.x += self.speed
class Ball(Gamesprite):
    def __init__(self, img, speed, x, y):
        super().__init__(img, speed, x, y)
    def moving(self):
        speed_x = 3
        speed_y = 3
background = transform.scale(image.load("sobaka-i-kega-mem-768x560.png"), (700,500))
player = Player1("собака.jpg", 40, 10, 10)
player2 = Player2("собака.jpg", 40, 20, 20)
ball = Ball("кега.jpg", 3, 50, 50)
game = True
def finish():
    game = False
while game:

    window.blit(background,(0,0))

    if finish != True:
        rect.x += speed_x
        rect.y += speed_y
        
        if sprite.collide_rect(Player1, Ball):
            if sprite.collide_rect(Player2, Ball):

                speed_x += -1

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()