import pygame
from random import randint
width = 1200
height = 700
fps = 30
game_name = "Orca-game"
img_dir = "media/img/"
enemy_dir = img_dir + "enemy/"
food_dir = img_dir + "food/"

class Orca(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "player.png")
        self.image = pygame.transform.scale(self.image,(317,197))
        self.rect = self.image.get_rect()
        self.rect.center = [height/2, width/2]
        self.speedx = 10
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speedx
        if key[pygame.K_RIGHT] and self.rect.x < width-317:
            self.rect.x += self.speedx

class Food_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_1.png")
        self.image = pygame.transform.scale(self.image,(180, 160))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Food_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_2.png")
        self.image = pygame.transform.scale(self.image,(180, 129))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Food_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_2.png")
        self.image = pygame.transform.scale(self.image,(180, 129))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Food_3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_3.png")
        self.image = pygame.transform.scale(self.image,(226, 158))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Food_4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_4.png")
        self.image = pygame.transform.scale(self.image,(195, 152))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Food_5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_5.png")
        self.image = pygame.transform.scale(self.image,(189, 157))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Food_6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(food_dir + "food_6.png")
        self.image = pygame.transform.scale(self.image,(179, 158))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.rect.y = -300
            self.rect.x = randint(20, width)
            self.speedy = randint(5, 10)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_dir + "enemy.png")
        self.image = pygame.transform.scale(self.image,(205, 160))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.kill()
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(enemy_dir + "enemy_2.png")
        self.image = pygame.transform.scale(self.image,(221, 158))
        self.rect = self.image.get_rect()
        self.rect.y = -300
        self.rect.x = randint(20, width)
        self.speedy = randint(5, 10)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > height:
            self.kill()