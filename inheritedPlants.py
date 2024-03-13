from plant import Plant
from pygame import Vector2
import pygame
from globals import GREEN, ORANGE, RED
pygame.init

# child class
class Flower( Plant ):           
	def __init__(self, pos, type):
		# invoking the __init__ of the parent class 
		super().__init__(pos)
		self.type = type
	
	def draw(self, screen):
		
		pygame.draw.rect(screen, (GREEN), (self.pos.x-10, self.pos.y+20, 20, 100+self.size*10)) 
		pygame.draw.circle(screen, (self.colors), self.pos + Vector2(-(2*self.size), (2*self.size)), 2 * self.size) 
		pygame.draw.circle(screen, (self.colors), self.pos + Vector2(-(2*self.size), -(2*self.size)), 2 * self.size) 
		#add missing petals here
		pygame.draw.circle(screen, (255,255,0), self.pos, 2 * self.size)

class Bush( Plant ):
	def __init__(self, pos, type):
		super().__init__(pos)
		self.type = type

	def draw(self, screen):
		pygame.draw.circle(screen, self.colors, self.pos + Vector2(0, -(1*self.size)), 2 * self.size)
		pygame.draw.circle(screen, self.colors, self.pos + Vector2((1.75*self.size), 0), 2 * self.size)
		pygame.draw.circle(screen, self.colors, self.pos + Vector2(-(1.75*self.size), 0), 2 * self.size)
