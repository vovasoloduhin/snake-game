#Імпортуємо Pygame
import pygame
import random

#інацілізуємо Pygame і його шрифтів
pygame.init()
pygame.font.init()

#Зміні для розміра вікна
WIDTH = 500
HEIGHT = 500

#Кольори
RED = (255, 0, 0)
GREEN = (16, 99, 40)
SNOW = (255,250,250)

#Створення ігрового вікна
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('RealisGame')
pygame.mouse.set_visible(True)


class Area:
    def __init__(self, x, y, width, heght, color):
        self.rect = pygame.Rect(x, y, width, heght)
        self.fill_color = color

    def fill(self):
        pygame.draw.rect(sc, self.fill_color, self.rect)

class Label(Area):
    def set_text(self, text, height, color=(0, 0, 0)):
        self.font = pygame.font.SysFont(None, height)
        self.image = self.font.render(str(text), True, color)

    def draw(self, x, y):
        self.fill()
        sc.blit(self.image, (self.rect.x + x, self.rect.y + y))

score = 1
lider_score = 1

#Створення х у
x = WIDTH / 2
y = HEIGHT / 2

#Кординати руху
dx = 0
dy = 0

#Характеристики змійкі
snake_block = 10
snake_list = []
snake_length = 1

#Розброз для яблука змійкі
applex = round(random.randrange(0, WIDTH - snake_block) / 10) * 10
appley = round(random.randrange(70, HEIGHT - snake_block) / 10) * 10

#Функція для відмальвкі заднього фону

image = pygame.image.load('background.png')

def draw_background(image):
    size = pygame.transform.scale(image, (WIDTH, HEIGHT))
    sc.blit(size, (0, 0))

#Функція для відмальвкі змійкі
def snake_draw(snake_block, snake_list):
    for element in snake_list:
        pygame.draw.rect(sc, GREEN, (element[0], element[1], snake_block, snake_block), 0)



clock = pygame.time.Clock()
fps = 10

#Ігровий цикл
run = True
finish = False
while run:
    for event in pygame.event.get():
        #Якщо користувач нажав кнопку вийти то програма виходе без глюків
        if event.type == pygame.QUIT:
            run = False

    if not finish:
        #Управління змійкі
        keys = pygame.key.get_pressed()

        #Якщо нажати esc то вийти з прогрми
        if keys[pygame.K_ESCAPE]:
            run = False

        #Якщо нажати LEFT то змійка піде вліво
        if keys[pygame.K_LEFT]:
            dx = -10
            dy = 0

        #Якщо нажати RIGHT то змійка піде вправо
        if keys[pygame.K_RIGHT]:
            dx = 10
            dy = 0

        #Якщо нажати UP то змійка піде в верх
        if keys[pygame.K_UP]:
            dx = 0
            dy = -10

        #Якщо нажати DOWN то змійка піде в низ
        if keys[pygame.K_DOWN]:
            dx = 0
            dy = 10

            # Умова програша і виграша коли змійка вишла за поле
        if x >= 499 or x < 1 or y >= 499 or y < 69:
            finish = True
            x = 250
            y = 250

        for coordinate in snake_list[:-1]:
            if coordinate[0] == x and coordinate[1] == y:
                finish = True



        # Відображення заднього фону
        draw_background(image)

        # Відмальовка яблока
        pygame.draw.rect(sc, RED, [applex, appley, snake_block, snake_block])

        # Відмальовка змійкі і рух її
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        snake_draw(snake_block, snake_list)
        pygame.draw.rect(sc, GREEN, [x, y, snake_block, snake_block])

        # Умови поїдання яблока змійкою
        if x == applex and y == appley:
            applex = round(random.randrange(0, WIDTH - snake_block) / 10) * 10
            appley = round(random.randrange(70, HEIGHT - snake_block) / 10) * 10
            snake_length += 1
            score += 1

        #умови найвищого рекорду змійкі
        if score > lider_score:
            lider_score = score

        score_text = Label(65, 25, 0, 0, SNOW)
        score_text.set_text(f'{int(score)}', 25)
        score_text.draw(35, 1)

        score_text = Label(10, 15, 0, 0, SNOW)
        score_text.set_text('Рахунок:', 25)
        score_text.draw(10, 10)

        game_over_text = Label(290, 10,0,10,GREEN)
        game_over_text.set_text('Якщо ви програли ', 25)
        game_over_text.draw(35, 1)

        game_over_text = Label(300, 25, 0, 10, GREEN)
        game_over_text.set_text(' нажміть Q щоб ', 25)
        game_over_text.draw(35, 1)

        game_over_text = Label(285, 40, 0, 10, GREEN)
        game_over_text.set_text(' почати грати заново', 25)
        game_over_text.draw(35, 1)

        lider_score_text = Label(195, 26.5, 0, 0, GREEN)
        lider_score_text.set_text(f'{int(lider_score)}', 25)
        lider_score_text.draw(35, 1)

        lider_score_text = Label(120, 25, 0, 0, GREEN)
        lider_score_text.set_text('Рекорд:', 25)
        lider_score_text.draw(35, 1)

    #Бескінечний рух змійкі
    x += dx
    y += dy

    if finish:
        snake_length = 1
        score = 1
        snake_list = []
        snake_head = []
        applex = round(random.randrange(0, WIDTH - snake_block) / 10) * 10
        appley = round(random.randrange(70, HEIGHT - snake_block) / 10) * 10
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            finish = False

    #Оновлення екрана
    pygame.display.update()
    clock.tick(fps)
