import pygame
import random
from particles import ParticleEmitter
pygame.init
from globals import RED, ORANGE, GREEN, SCREEN_SIZE, FPS
from plant import Plant
from inheritedPlants import Flower, Bush
from pygame import Vector2
				  
# creation of an object variable or an instance
f1 = Flower(Vector2(200, 400), "daisy")
b1 = Bush(Vector2(400, 600), "bush")
mouseEmitter = ParticleEmitter(
	pos = Vector2(SCREEN_SIZE)//2,
	updateAttributes = [["colorOverDistance", [250, [(255, 255, 0), (255, 150, 100)]]]],
	initAttributes = [["randAngle"], ["moveOnAngle", 20]],
	maxParticles=1000,
	ppf=10,
	particleLifetime=250,
	size = 1,
)

#creates game screen and caption
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("inheritance demo")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed


#BEGIN GAME LOOP######################################################
while not doExit:
   
	delta = clock.tick(FPS)/1000 #FPS (frames per second)
	  
	#pygame's way of listening for events (key presses, mouse clicks, etc)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		   doExit = True #lets you quit program

	#keyboard input-----------------------------------
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[2]: # RIGHT click
				season = random.randint(0, 3)
				f1.changeSeason(season)
				b1.changeSeason(season)
			elif pygame.mouse.get_pressed()[0]: # LEFT click
				f1.getWatered()
				b1.getWatered()
				print("watering plant!")
	
	#render section-----------------------------------
	screen.fill((0, 0, 0))

	#draw class objects
	f1.grow()
	f1.draw(screen)
	b1.grow()
	b1.draw(screen)

	mouseEmitter.update(screen, delta, pos = pygame.mouse.get_pos(), velo = -Vector2(pygame.mouse.get_rel())/7.5)

  

	pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()