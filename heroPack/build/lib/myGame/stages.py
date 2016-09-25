import pygame
from myGame import heroes

backgrounds = ( "images/materials/background_level1.png",
          "images/materials/background_level2.jpg",
          "images/materials/background_level3.jpg",
          "images/materials/background_level4.jpg",
          "images/materials/background_level5.jpg",
          "images/materials/background_level6.jpg",
          "images/materials/background_level7.jpg",
          "images/materials/background_level8.jpg",
          "images/materials/background_level9.jpg",
          "images/materials/background_level10.jpg"
    )

rock1 = pygame.image.load("images/materials/rock1.png")
rock2 = pygame.image.load("images/materials/rock2.png")
rock3 = pygame.image.load("images/materials/rock3.png")

rock1 = pygame.transform.scale(rock1,(100,100))
rock2= pygame.transform.scale(rock2,(100,100))
rock3 = pygame.transform.scale(rock3,(100,100))

class rock_map:
    def __init__(self,coordinates_list):
        self.coordinates_list = coordinates_list

    def showRocks(self,display):
        for rock in self.coordinates_list:
            display.blit(rock[2],(rock[0],rock[1]))
            

class screen:
    def __init__(self,rocks,level_number,flag_coordinates):
        self.rocks = rocks
        self.flag_coordinates = flag_coordinates
        x,y = 1200,700
        self.back_image = pygame.image.load(backgrounds[level_number - 1])
        self.back_image = pygame.transform.scale(self.back_image,(x,y))
        self.flag       = pygame.image.load("images/materials/winFlag.png")
        self.flag       = pygame.transform.scale(self.flag,(50,50))

    

    def show(self,display):
        display.blit(self.back_image,(0,0))
        display.blit(self.flag,self.flag_coordinates)
        self.rocks.showRocks(display)
        


class stage:
    def __init__(self,hero,screen_list):
        self.hero = hero
        self.screen_list = screen_list
        self.currentScreen = self.screen_list[0]
    
    def showCurrentScreen(self,display):
        self.currentScreen.show(display)
        self.hero.show(display)


################### Stages ######################


### first        
rList = [[100,100]]
rList[0].append(rock1)
rock_M = rock_map(rList)

myScreen = screen(rock_M,1,(400,500))
myScreenList = []
myScreenList.append(myScreen)


