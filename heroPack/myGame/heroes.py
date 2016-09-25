import pygame

hero1_images = ( "images/actual_heroes/hero_left_walk.png",
                 "images/actual_heroes/hero_left_walk2.png",
                 "images/actual_heroes/hero_right_walk.png",
                 "images/actual_heroes/hero_right_walk2.png",
                 "images/actual_heroes/hero_left.png",
                 "images/actual_heroes/hero_right.png",
    )

hero2_images = ( "images/actual_heroes/Angry_hero_left_walk.png",
                 "images/actual_heroes/Angry_hero_left_walk2.png",
                 "images/actual_heroes/Angry_hero_right_walk.png",
                 "images/actual_heroes/Angry_hero_right_walk2.png",
                 "images/actual_heroes/Angry_hero_left.png",
                 "images/actual_heroes/Angry_hero_right.png",
    )

hero3_images = ( "images/actual_heroes/Silly_hero_left_walk.png",
                 "images/actual_heroes/Silly_hero_left_walk2.png",
                 "images/actual_heroes/Silly_hero_right_walk.png",
                 "images/actual_heroes/Silly_hero_right_walk2.png",
                 "images/actual_heroes/Silly_hero_left.png",
                 "images/actual_heroes/Silly_hero_right.png",
    )

hero4_images = ( "images/actual_heroes/Cool_hero_left_walk.png",
                 "images/actual_heroes/Cool_hero_left_walk2.png",
                 "images/actual_heroes/Cool_hero_right_walk.png",
                 "images/actual_heroes/Cool_hero_right_walk2.png",
                 "images/actual_heroes/Cool_hero_left.png",
                 "images/actual_heroes/Cool_hero_right.png",
    )

bot_images   = ()

hero_image_patterns = ( hero1_images,
                        hero2_images,
                        hero3_images,
                        hero4_images
    )

class hero:
    def __init__(self,x,y,display,hero_number,speed):
        images = hero_image_patterns[hero_number]
        self.left1Img = pygame.image.load(images[0])
        self.left2Img = pygame.image.load(images[1])
        self.right1Img = pygame.image.load(images[2])
        self.right2Img = pygame.image.load(images[3])
        self.leftStayImg = pygame.image.load(images[4])
        self.rightStayImg = pygame.image.load(images[5])
        
        self.x_coordinate = x
        self.y_coordinate = y
        self.orientation = "right"
        self.walkingState = "stay_right"
        self.rightWalkingState = 0
        self.leftWalkingState = 0
        self.speed = speed

        self.left1Img = pygame.transform.scale(self.left1Img,(140,140))
        self.left2Img = pygame.transform.scale(self.left2Img,(140,140))
        self.right1Img = pygame.transform.scale(self.right1Img,(140,140))
        self.right2Img = pygame.transform.scale(self.right2Img,(140,140))
        self.leftStayImg = pygame.transform.scale(self.leftStayImg,(140,140))
        self.rightStayImg = pygame.transform.scale(self.rightStayImg,(140,140))
        self.show(display)

    def show(self,display):
        if self.walkingState == "left1":
            display.blit(self.left1Img,(self.x_coordinate,self.y_coordinate))        
        elif self.walkingState == "left2":
            display.blit(self.left2Img,(self.x_coordinate,self.y_coordinate))
        elif self.walkingState == "right1":
            display.blit(self.right1Img,(self.x_coordinate,self.y_coordinate))
        elif self.walkingState == "right2":
            display.blit(self.right2Img,(self.x_coordinate,self.y_coordinate))
        elif self.walkingState == "stay_right":
            display.blit(self.rightStayImg,(self.x_coordinate,self.y_coordinate))
        else:
            display.blit(self.leftStayImg,(self.x_coordinate,self.y_coordinate))
    
    def walk(self,display,side):
        if side == "left":
            if self.orientation != "left":
                self.orientation = "left"
                self.walkingState = "stay_left"
            else:
                if self.walkingState == "stay_left":
                    self.walkingState = "left1"
                elif self.walkingState == "left1":
                    self.walkingState = "left2"
                else:
                    self.walkingState = "left1"
                    
            self.x_coordinate -= self.speed
            if self.x_coordinate < -46:
                self.x_coordinate = -46
            
        elif side == "up":
            if self.orientation == "left":
                if self.walkingState == "stay_left":
                    self.walkingState = "left1"
                elif self.walkingState == "left1":
                    self.walkingState = "left2"
                else:
                    self.walkingState = "left1"
            elif self.orientation == "right":
                if self.walkingState == "stay_right":
                    self.walkingState = "right1"
                elif self.walkingState == "right1":
                    self.walkingState = "right2"
                else:
                    self.walkingState = "right1"
                
            self.y_coordinate -= self.speed
            if self.y_coordinate < -30:
                self.y_coordinate = -30
            
        elif side == "right":
            if self.orientation != "right":
                self.orientation = "right"
                self.walkingState = "stay_right"
            else:
                if self.walkingState == "stay_right":
                    self.walkingState = "right1"
                elif self.walkingState == "right1":
                    self.walkingState = "right2"
                else:
                    self.walkingState = "right1"
        
            self.x_coordinate += self.speed
            x_,y_ = display.get_size()
            if self.x_coordinate > (x_ - 96):
                self.x_coordinate = x_ - 96
            
        elif side == "down":
            if self.orientation == "left":
                if self.walkingState == "stay_left":
                    self.walkingState = "left1"
                elif self.walkingState == "left1":
                    self.walkingState = "left2"
                else:
                    self.walkingState = "left1"
            elif self.orientation == "right":
                if self.walkingState == "stay_right":
                    self.walkingState = "right1"
                elif self.walkingState == "right1":
                    self.walkingState = "right2"
                else:
                    self.walkingState = "right1"
                
            self.y_coordinate += self.speed
            x_,y_ = display.get_size()
            if self.y_coordinate > (y_ - 115):
                self.y_coordinate = y_ - 115
        
class bot(hero):
    def __init__(self,x,y,display,hero_number,speed):
        pass
