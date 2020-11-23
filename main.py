import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
red = (255,0,0)

x = 25
y = 25

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    
    def __init__(self, filename):
        """Constructor function"""
        
        super().__init__()

        
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)

        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

      

        self.change_x = 0
        self.change_y = 0


    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y


    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y



pygame.init()




     
screen = pygame.display.set_mode([800, 500])


pygame.display.set_caption('Test')
bg = pygame.image.load("bg.jpg").convert()
bg_position = [0,0]

player = Player("player.png")
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    
    player.update()

   

    screen.blit(bg, bg_position)


    all_sprites_list.draw(screen)


    pygame.display.flip()


    clock.tick(60)

pygame.quit()