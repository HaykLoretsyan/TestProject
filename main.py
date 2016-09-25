import pygame
from myGame import heroes,stages

menuBackground = pygame.image.load("images/materials/Menu.png")
menuBackground = pygame.transform.scale(menuBackground,(1200,700))

questionPanel = pygame.image.load("images/materials/Sure.png")
questionPanel = pygame.transform.scale(questionPanel,(840,250))

startButton = pygame.image.load("images/materials/start.png")
startUnselected = pygame.transform.scale(startButton,(400,100))
startSelected = pygame.transform.scale(startButton,(480,120))

recordsButton = pygame.image.load("images/materials/records.png")
recordsUnselected = pygame.transform.scale(recordsButton,(400,100))
recordsSelected = pygame.transform.scale(recordsButton,(480,120))

settingsButton = pygame.image.load("images/materials/settings.png")
settingsUnselected = pygame.transform.scale(settingsButton,(400,100))
settingsSelected = pygame.transform.scale(settingsButton,(480,120))

quitButton = pygame.image.load("images/materials/quit.png")
quitUnselected = pygame.transform.scale(quitButton,(400,100))
quitSelected = pygame.transform.scale(quitButton,(480,120))

yesButton = pygame.image.load("images/materials/Yes.png")
yesUnselected = pygame.transform.scale(yesButton,(220,150))
yesSelected = pygame.transform.scale(yesButton,(280,190))

noButton = pygame.image.load("images/materials/No.png")
noUnselected = pygame.transform.scale(noButton,(220,150))
noSelected = pygame.transform.scale(noButton,(280,190))

unselected = [startUnselected,recordsUnselected,
              settingsUnselected,quitUnselected]

selected = [startSelected,recordsSelected,
            settingsSelected,quitSelected]

def gameMenu(Display,clock):

    pygame.key.set_repeat(100,100)
    running = 1
    select = 0
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if select == 0:
                        gameLoop(Display,clock,1,2)
                    elif select == 3:
                        running = 0
                elif event.key == pygame.K_UP:
                    select -= 1
                    if select == -1:
                        select = 3 
                elif event.key == pygame.K_DOWN:
                    select += 1
                    if select == 4:
                        select = 0
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                if x > 400 and x < 800:
                    if y > 100 and y < 200:
                        select = 0
                    elif y > 240 and y < 340:
                        select = 1
                    elif y > 380 and y < 480:
                        select = 2
                    elif y > 520 and y < 660:
                        select = 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if x > 400 and x < 800:
                    if y > 100 and y < 200:
                        gameLoop(Display,clock,1,3)
                    elif y > 520 and y < 660:
                        running = 0

        Display.blit(menuBackground,(0,0))
        displayMenuButtons(select,Display)
        pygame.display.update()
        clock.tick(60)

def displayMenuButtons(selection,display):
    display.blit(selected[selection],(360,100 + selection*140))
    number = 0
    for img in unselected:
        if number == selection:
            number += 1
            continue
        display.blit(unselected[number],(400,100 + number*140))
        number += 1

def displayQuestionButtons(selection,display):
    display.blit(questionPanel,(150,130))

    if selection == 0:
        display.blit(noUnselected,(680,400))
        display.blit(yesSelected,(270,380))
    else:
        display.blit(noSelected,(650,380))
        display.blit(yesUnselected,(300,400))
        
def gameLoop(Display,clock,level,hero):

    if hero == 0:
        speed = 4
    elif hero == 1:
        speed = 5
    elif hero == 2:
        speed = 6
    else:
        speed = 7
    
    myHero = heroes.hero(200,200,Display,hero,speed)
    level = stages.stage(myHero,stages.myScreenList)
    currCoordinates = (200,200)

    rocksMap = level.currentScreen.rocks.coordinates_list;
    
    pygame.key.set_repeat(25, 25)   #for smoothness
    running = 1
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = quitLevel(Display,clock,level)
                elif event.key == pygame.K_LEFT:
                    level.hero.walk(Display,"left")
                elif event.key == pygame.K_RIGHT:
                    level.hero.walk(Display,"right")
                elif event.key == pygame.K_DOWN:
                    level.hero.walk(Display,"down")
                elif event.key == pygame.K_UP:
                    level.hero.walk(Display,"up")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    level.hero.walkingState = "stay_left"
                elif event.key == pygame.K_RIGHT:
                    level.hero.walkingState = "stay_right"
                elif event.key == pygame.K_DOWN:
                    if level.hero.orientation == "right":
                        level.hero.walkingState = "stay_right"
                    else:
                        level.hero.walkingState = "stay_left"
                elif event.key == pygame.K_UP:
                    if level.hero.orientation == "right":
                        level.hero.walkingState = "stay_right"
                    else:
                        level.hero.walkingState = "stay_left"

        currCoordinates = checkForRocks(rocksMap,
                                       (level.hero.x_coordinate,level.hero.y_coordinate),
                                        currCoordinates)
        
        level.hero.x_coordinate,level.hero.y_coordinate = currCoordinates

        level.showCurrentScreen(Display)
        pygame.display.update()
        clock.tick(60)
    pygame.key.set_repeat(100,100)

def checkForRocks(rMap,heroCurr,heroPrev):
    for rock in rMap:
        if heroCurr[0] > rock[0] - 30 and heroCurr[0] < rock[0] + 30 and heroCurr[1] > rock[1] - 30 and heroCurr[1] < rock[1] + 30:
            print("ROCKS",rock[0]," ",rock[1])
            return heroPrev
    return heroCurr

def quitLevel(Display,clock,level):
    running  = 1
    status   = 0
    selected = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    status = selected
                    running = 0
                if event.key == pygame.K_RIGHT:
                    selected = 1
                elif event.key == pygame.K_LEFT:
                    selected = 0
            
        level.showCurrentScreen(Display)
        displayQuestionButtons(selected,Display)
        pygame.display.update()
        clock.tick(60)
        
    return status

################################################################

pygame.init()

Display = pygame.display.set_mode((1200,700),pygame.FULLSCREEN)
pygame.display.set_caption('Labirinth')
clock = pygame.time.Clock()
gameMenu(Display,clock)

pygame.quit()
