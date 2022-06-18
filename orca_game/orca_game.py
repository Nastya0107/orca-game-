import pygame
from for_orca_game import Orca, Food_1, Food_2, Food_3, Food_4, Food_5, Food_6, Enemy , Enemy2
from time import sleep
pygame.init()
width = 1200
height = 700
fps = 30
game_name = "Orca-game"
img_dir = "media/img/"
enemy_dir = img_dir + "enemy/"
food_dir = img_dir + "food/"
snd_dir = "media/snd/"

def draw_text(screen,text,size,x,y,color):
    font_name = pygame.font.match_font('arial')    # Выбираем тип шрифта для текста
    font = pygame.font.Font(font_name, size)       # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)    # Превращаем текст в картинку
    text_rect = text_image.get_rect()              # Задаем рамку картинки с текстом
    text_rect.center = (x,y)                       # Переносим текст в координаты
    screen.blit(text_image, text_rect)             # Рисуем текст на экране


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

pygame.mixer.music.load(snd_dir+"main.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

eat = pygame.mixer.Sound(snd_dir + "eat.mp3")
lose = pygame.mixer.Sound(snd_dir + "lose.mp3")


bg = pygame.image.load(img_dir + "bg.jpg")
bg = pygame.transform.scale(bg,(width, height))

first = pygame.image.load(img_dir + "first.png")
first = pygame.transform.scale(first,(width, height))

won_pic = pygame.image.load(img_dir + "won.png")
won_pic = pygame.transform.scale(won_pic,(width, height))

all_sp = pygame.sprite.Group()
food = pygame.sprite.Group()
enemy = pygame.sprite.Group()
food_1 = Food_1()
player = Orca()
food_2 = Food_2()
food_3 = Food_3()
food_4 = Food_4()
food_5 = Food_5()
food_6 = Food_6()
all_sp.add(player, food_1, food_2, food_3, food_4, food_5, food_6)
food.add(food_1, food_2, food_3, food_4, food_5, food_6)
player_sp = pygame.sprite.Group()
player_sp.add(player)

timer = pygame.time.Clock()
count = 0
fish = 0
chance = 0
begin = True

run = True
while run:
    if begin == True:
        screen.blit(first,(0, 0))
        pygame.display.update()
        sleep(5)
        begin = False
    timer.tick(fps)
    all_sp.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    got_food = pygame.sprite.groupcollide(food, player_sp, True, False)
    if got_food:
        eat.play()
        fish += 1
        count += 1
        if fish == 4:
            food_1 = Food_1()
            food_2 = Food_2()
            food_3 = Food_3()
            food_4 = Food_4()
            food_5 = Food_5()
            food_6 = Food_6()
            food.add(food_1, food_2, food_3, food_4, food_5, food_6)
            all_sp.add(food_1, food_2, food_3, food_4, food_5, food_6)
            chance += 1
            if chance == 2:
                enemy1 = Enemy()
                enemy2 = Enemy2()
                enemy.add(enemy1, enemy2)
                all_sp.add(enemy1, enemy2)
                chance -= 2
            fish = 0
    if count == 80:
        screen.blit(won_pic, (0, 0))
        pygame.display.update()
        pygame.mixer.music.load(snd_dir + "won.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
        sleep(20)
        run = False
    bad_fish = pygame.sprite.groupcollide(enemy, player_sp, True, False)
    if bad_fish:
        lose.play()
        sleep(0.5)
        count -= 2
    screen.blit(bg, (0, 0))
    draw_text(screen, "Вы поймали " + str(count) + " рыб(ы)", 50 , width/2, 50, 'black')
    all_sp.draw(screen)
    pygame.display.update()