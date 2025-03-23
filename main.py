




class Player(GameSprite):
    def update1(self):
        keypressed = key.get_pressed()
        if keypressed[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keypressed[K_s] and self.rect.y < 700-15-65:










window = display.set_mode((700,700))
display.set_caption('pingPong')
background = transform.scale(image.load('bg.jpg'), (700,700))

game = True
clock = time.Clock()
fps = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))
    clock.tick(fps)from pygame import *
    display.update()