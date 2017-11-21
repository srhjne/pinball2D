import pygame
import math
import sys
import random
from pygame.locals import *
import physics
import numpy as np
import time


class PinBall(object):
	screen_width = 400 
	screen_height = 700
	gravity = 10

	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0, 255)

	def __init__(self, lives, level):
		self.lives = lives
		self.level = level
		self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
		self.screen.fill((255,255,255))
		self.background = pygame.image.load('blank_bg.png').convert()
		self.screen.blit(self.background, (0, 30))
		self.score = 0
		pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
		self.myfont = pygame.font.SysFont('sanserif', 30)

		textsurface = self.myfont.render("Lives left "+str(self.lives), False, (0, 0, 0))		
		self.screen.blit(textsurface,(0,0))
		print ("making board")
		self.table = self.get_table(level)
		self.display_table()
		pygame.display.update()

	def get_table(self, level):
		self.table = {"holes": [(200,400),(200,200),(270,500),(130,500)],"hole_size":40}
		return self.table


	def display_table(self):
		for hole in self.table["holes"]:
			pygame.draw.rect(self.screen, self.red, (hole[0], hole[1], self.table["hole_size"], self.table["hole_size"]))
		pygame.draw.rect(self.screen, self.blue, (350,100,20,600))
		pygame.draw.rect(self.screen, self.blue, (30,100,20,600))

	def draw_ball(self):
		pygame.draw.rect(self.screen, self.green, (self.ball.position[0], self.ball.position[1], self.ball.width, self.ball.height))
		pygame.display.update()
		self.screen.blit()

	def play_game(self):
		

		
		self.ball = Ball(380,690)
		self.player = pygame.image.load('ball.png').convert()
		position = self.player.get_rect()
		position.left = 380
		position.top = 690
		#self.draw_ball()
		gtime = 0

		self.ball.velocity[1] = -200
		self.ball.velocity[0] = -50
		gravity = np.ndarray(2)
		gravity[0] = 0
		gravity[1] = 10
		
		while self.lives > 0:
			check = physics.update_velocity_position(self.ball, gtime, gtime+0.1, gravity)
			if not check:
				self.lives -= 1
				self.ball.position[0] = 380
				self.ball.position[1] = 690
			self.screen.blit(self.background, position, position) #erase
			position.left = self.ball.position[0]
			position.top = self.ball.position[1]     #move player
			self.screen.blit(self.player, position)      #draw new player
			pygame.display.update()  
			if physics.handle_holes(self.ball, self.table["holes"], self.table["hole_size"]):
				self.score +=20 
				self.lives -=1  
				self.ball.position[0] = 380
				self.ball.position[1] = 690      
			pygame.time.delay(100)
			print(self.ball.position)
			gtime+=0.1
			print("score", self.score)

			#self.draw_ball()
			


class Ball(object):
	width = 15
	height = 15


	def __init__(self, x, y):
		self.position = np.ndarray(2)
		self.position[0] = x
		self.position[1] = y
		self.velocity = np.zeros(2)
		self.mass = 1

	





game = PinBall(2,0)
game.play_game()

