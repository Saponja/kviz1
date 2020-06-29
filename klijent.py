import pygame
import math
from random import *
from pymongo import MongoClient
import pprint


client = MongoClient('mongodb://localhost:27017/')
db = client["quiz_datebase"]
history_questions = db["history_questions"]




pygame.init()

width = 1000
height = 600
offset_x = (width / 5 - 128) / 2
offset_y = (height / 4 - 128) / 2
black = (255, 255, 255)

i2 = pygame.image.load("img/h2.png")
i3 = pygame.image.load("img/globe.png")
i4 = pygame.image.load("img/cinema.png")
i5 = pygame.image.load("img/basketball.png")
i6 = pygame.image.load("img/science.png")
i7 = pygame.image.load("img/quiz.png")
i8 = pygame.image.load("img/cross.png")

history_true = True
geography_true = True
cinema_true = True
sport_true = True
science_true = True
trivia_true = True

#rect = pygame.Rect((0, 40), (width, 100))


def readFromMongo():
    rnd = randint(1,3)
    result = history_questions.find_one({"_id": rnd})
    questFont = pygame.font.SysFont("comicsansms", 40)
    ansFont = pygame.font.SysFont("comicsansms", 25)
    quest = questFont.render(result["quest"], True, (0,0,0))
    ans1 = ansFont.render(result["ans1"], True, (0,0,0))
    ans2 = ansFont.render(result["ans2"], True, (0,0,0))
    ans3 = ansFont.render(result["ans3"], True, (0,0,0))
    crt = result["crt"];

    return (quest,ans1,ans2,ans3)




def gameWindow():
    running2 = True
    active = False
    while running2:
        win2 = pygame.display.set_mode((width, height))
        win2.fill((119, 136, 153))
        text = readFromMongo()
        if active:
            win2.blit(text[0], (100, 50))
            rect = pygame.draw.rect(win2, (255, 160, 255, 50), (0, 170, width, 100))
            win2.blit(text[1], (100, 200))
            rect = pygame.draw.rect(win2, (255, 160, 255), (0, 320, width, 100))
            win2.blit(text[2], (100, 350))
            rect = pygame.draw.rect(win2, (255, 160, 255), (0, 470, width, 100))
            win2.blit(text[3], (100, 500))
            pygame.time.wait(3000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
        active = True
        pygame.display.update()




running = True

while running:
    win = pygame.display.set_mode((width, height))
    win.fill((119, 136, 153))
    if history_true:
        win.blit(i2, (int(width / 5 + offset_x), int(height / 4 + offset_y)))
    else:
        win.blit(i2, (int(width / 5 + offset_x), int(height / 4 + offset_y)))
        win.blit(i8, (int(width / 5 + offset_x), int(height / 4 + offset_y)))

    if geography_true:
        win.blit(i3, (int(width / 5 * 2 + offset_x), int(height / 4 + offset_y)))
    else:
        win.blit(i3, (int(width / 5 * 2 + offset_x), int(height / 4 + offset_y)))
        win.blit(i8, (int(width / 5 * 2 + offset_x), int(height / 4 + offset_y)))

    if cinema_true:
        win.blit(i4, (int(width / 5 * 3 + offset_x), int(height / 4 + offset_y)))
    else:
        win.blit(i4, (int(width / 5 * 3 + offset_x), int(height / 4 + offset_y)))
        win.blit(i8, (int(width / 5 * 3 + offset_x), int(height / 4 + offset_y)))

    if sport_true:
        win.blit(i5, (int(width / 5 + offset_x), int(height / 2 + offset_y)))
    else:
        win.blit(i5, (int(width / 5 + offset_x), int(height / 2 + offset_y)))
        win.blit(i8, (int(width / 5 + offset_x), int(height / 2 + offset_y)))

    if science_true:
        win.blit(i6, (int(width / 5 * 2 + offset_x), int(height / 2 + offset_y)))
    else:
        win.blit(i6, (int(width / 5 * 2 + offset_x), int(height / 2 + offset_y)))
        win.blit(i8, (int(width / 5 * 2 + offset_x), int(height / 2 + offset_y)))

    if trivia_true:
        win.blit(i7, (int(width / 5 * 3 + offset_x), int(height / 2 + offset_y)))
    else:
        win.blit(i7, (int(width / 5 * 3 + offset_x), int(height / 2 + offset_y)))
        win.blit(i8, (int(width / 5 * 3 + offset_x), int(height / 2 + offset_y)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            if pos_x < width / 5 + offset_x + 128 and pos_x > width / 5 + offset_x and pos_y > height / 4 + offset_y and pos_y < height / 4 + offset_y + 128 and history_true:
                gameWindow()
                history_true = False

            if pos_x < width / 5 * 2 + offset_x + 128 and pos_x > width / 5 * 2 + offset_x and pos_y > height / 4 + offset_y and pos_y < height / 4 + offset_y + 128 and geography_true:
                print("geografija")
                geography_true = False

            if pos_x < width / 5 * 3 + offset_x + 128 and pos_x > width / 5 * 3 + offset_x and pos_y > height / 4 + offset_y and pos_y < height / 4 + offset_y + 128 and cinema_true:
                print("film")
                cinema_true = False

            if pos_x < width / 5 + offset_x + 128 and pos_x > width / 5 + offset_x and pos_y > height / 2 + offset_y and pos_y < height / 2 + offset_y + 128 and sport_true:
                print("sport")
                sport_true = False

            if pos_x < width / 5 * 2 + offset_x + 128 and pos_x > width / 5 * 2 + offset_x and pos_y > height / 2 + offset_y and pos_y < height / 2 + offset_y + 128 and science_true:
                print("nauka")
                science_true = False

            if pos_x < width / 5 * 3 + offset_x + 128 and pos_x > width / 5 * 3 + offset_x and pos_y > height / 2 + offset_y and pos_y < height / 2 + offset_y + 128 and trivia_true:
                print("trivia")
                trivia_true = False

    pygame.display.update()
