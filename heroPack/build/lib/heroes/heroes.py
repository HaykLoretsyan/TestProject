import pygame

class hero:
    def __init__(self,x,y,display,images):
        self.leftImg = pygame.image.load(images[0])
        self.leftImgWalk = pygame.image.load(images[1])
        self.rightImg = pygame.image.load(images[2])
        self.rightImgWalk = pygame.image.load(images[3])
        self.x_coordinate = x
        self.y_coordinate = y
        self.orientation = "right"
        self.rightWalkingState = 0
        self.leftWalkingState = 0
        self.leftImg = pygame.transform.scale(self.leftImg,(140,140))
        self.leftImgWalk = pygame.transform.scale(self.leftImgWalk,(140,140))
        self.rightImg = pygame.transform.scale(self.rightImg,(140,140))
        self.rightImgWalk = pygame.transform.scale(self.rightImgWalk,(140,140))
        self.show(display)

    def show(self,display):
        if self.orientation == "left":
            display.blit(self.leftImg,(self.x_coordinate,self.y_coordinate))        
        elif self.orientation == "leftWalk":
            display.blit(self.leftImgWalk,(self.x_coordinate,self.y_coordinate))
        elif self.orientation == "right":
            display.blit(self.rightImg,(self.x_coordinate,self.y_coordinate))
        elif self.orientation == "rightWalk":
            display.blit(self.rightImgWalk,(self.x_coordinate,self.y_coordinate))
        else:
            display.blit(self.rightImg,(self.x_coordinate,self.y_coordinate))        
    
    def walk(self,display,side):
        if side == "left":
            if self.orientation != "left":
                self.orientation = "left"
            else:
                self.orientation = "leftWalk"

            self.x_coordinate -= 4
            if self.x_coordinate < 0:
                self.x_coordinate = 0
            
        elif side == "up":
            if self.orientation == "left":
                self.orientation = "leftWalk"
            elif self.orientation == "leftWalk":
                self.orientation = "left"
            elif self.orientation == "right":
                self.orientation = "rightWalk"
            elif self.orientation == "rightWalk":
                self.orientation = "right"
                
            self.y_coordinate -= 4
            if self.y_coordinate < 0:
                self.y_coordinate = 0
            
        elif side == "right":
            if self.orientation != "right":
                self.orientation = "right"
            else:
                self.orientation = "rightWalk"

            self.x_coordinate += 4
            x_,y_ = display.get_size()
            if self.y_coordinate > (x_ - 40):
                self.y_coordinate = x_ - 40
            
        elif side == "down":
            if self.orientation == "left":
                self.orientation = "leftWalk"
            elif self.orientation == "leftWalk":
                self.orientation = "left"
            elif self.orientation == "right":
                self.orientation = "rightWalk"
            elif self.orientation == "rightWalk":
                self.orientation = "right"
                
            self.y_coordinate += 4
            x_,y_ = display.get_size()
            if self.y_coordinate > (y_ - 70):
                self.y_coordinate = y_ - 70
        
