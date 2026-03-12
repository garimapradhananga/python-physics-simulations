import pygame, sys, random, imageio
import numpy as np

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Particle class
class Particle:
    def __init__(self):
        self.radius = random.randint(5, 15)
        self.x = random.randint(self.radius, WIDTH-self.radius)
        self.y = random.randint(self.radius, HEIGHT-self.radius)
        self.vx = random.uniform(-4,4)
        self.vy = random.uniform(-4,4)
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x<=self.radius or self.x>=WIDTH-self.radius: self.vx*=-1
        if self.y<=self.radius or self.y>=HEIGHT-self.radius: self.vy*=-1
    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.radius)

particles = [Particle() for _ in range(20)]

# For saving GIF
frames = []

for frame_num in range(100):  # save 100 frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))
    for p in particles:
        p.move()
        p.draw(screen)
    
    # Capture frame (single statement!)
    frames.append(pygame.surfarray.array3d(screen).swapaxes(0,1))
    
    pygame.display.flip()
    clock.tick(60)

# Save GIF (single statement!)
imageio.mimsave('particle_sim.gif', frames, fps=30)

pygame.quit()
