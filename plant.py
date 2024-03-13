from pygame import Vector2
from globals import SCOLORS
import random
# parent class
class Plant( object ):    
		  
		def __init__(self, pos : Vector2 = Vector2(0, 0)):   
			self.pos = pos
			self.size = 10
			self.water = 0
			self.colors = (255, 255, 255)
			
		def grow(self):
			if self.water>10:
				self.water-=10
				self.size +=20
				print("growing!")
				
		def getWatered(self):
			self.water+=5
		def changeSeason(self, season = random.randint(0, 3)):
			seasonNames = ['SPRING', 'SUMMER', 'AUTUMN', 'WINTER']
			self.colors = SCOLORS[seasonNames[season]]
			print(f"season changed to {seasonNames[season]}")