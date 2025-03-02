import pygame
pygame.init ()

screen=pygame.display.set_mode((600,600))

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(white)
pygame.display.update()

#Creating rectangle class

class Rect ():
    def __init__ (self, color, dimentions) :
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimentions = dimentions

    def draw (self) :
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimentions) 

#Creating instances
green_rect = Rect(green, (50, 20, 100, 60))
red_rect = Rect(red, (150, 200, 150, 100))
blue_rect = Rect(blue, (300, 400, 200, 150))

#accessing methods
green_rect.draw()
blue_rect.draw()
red_rect.draw()

pygame.display.update() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)