import pygame 
pygame.init

screen = pygame.display.set_mode((600,600))

class Circle ():
    def __init__(self, color, radius, position,width):
        self.color = color
        self.radius = radius
        self.position = position
        self.width = width
    def draw (self):
        pygame.draw.circle (screen,self.color,self.position,self.radius,self.width)

Circle1 = Circle ((255,0,0),40,(300,300),30)
Circle2 = Circle ((100,50,90),50,(150,300),40)

Circle1.draw ()
Circle2.draw ()

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running =  False
            pygame.quit()
            exit(0)
