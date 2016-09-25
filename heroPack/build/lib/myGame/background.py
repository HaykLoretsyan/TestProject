import pygame

level = ( "images/materials/background_level1.jpg",
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

def set_image(display,level_number):
    x,y = display.get_size()
    back_img = pygame.image.load(level[level_number - 1])
    back_img = pygame.transform.scale(back_img,(x,y))

    return back_img

def show(display,image):
    display.blit(image,(0,0))
    
