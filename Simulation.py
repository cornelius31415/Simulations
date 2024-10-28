import pygame
import random
import math

# parameters for the simulation window
width = 800
height = 600
white = (255,255,255)   # RGB value for white
black = (0,0,0)         # RGB value for black

# parameters for the particles
num_particles = 1
radius = 10
speed = 2

# defining a class for the particle
# the particle has a random start position
# and a random direction of movement
# the velocity components are given by the direction
class Particle:
    
    def __init__(self):
        # random start positions
        # taking care that it cannot leave the window
        # no part of the circle can cross the window border
        # so it has to start at radius not at zero
        self.x = random.randint(radius,width-radius) 
        self.y = random.randint(radius,height-radius)
        
        # set the direction of movement at the start randomly
        # by choosing a random angle in the range 0 to 2*pi
        self.angle = random.uniform(0, 2*math.pi)
        
        # the velocity has an x- and a y-component
        # x-component is the cosin of the angle times the 
        # absolute value of velocity (speed)
        # for the y-component its sine
        self.vx = speed*math.cos(self.angle)
        self.vy = speed*math.sin(self.angle)
        
    def move(self):
        # distance moved = velocity * time
        # we can set the time unit to 1
        self.x += self.vx
        self.y += self.vy
        
        # reflecting on the wall behavior depends on which wall
        # if it reflects from a vertical wall, the x-component
        # of the velocity inverts
        # for a horizontal wall it is the y-component 
        
        if self.x < radius or self.x > width-radius:
            self.vx = -self.vx
        if self.y < radius or self.y > height-radius:
            self.vy = -self.vy
            
        
    
    def draw(self,screen):
        pygame.draw.circle(screen, white, (int(self.x),int(self.y)), radius)
        
        
def main():
    
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    
    running = True
    
    particle = Particle()
    
    while running:
        screen.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        particle.move()
        particle.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)          # frames per second


if __name__ == "__main__":
    main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        