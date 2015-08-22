import pygame as pg;
from pygame.locals import *;

class Player:
	def __init__(self,idle_animation,walking_animation,pos):
		self.current_action = 0;

		self.position = pos;

		self.facing_right = True;

		self.animations = [];
		self.animations.append(idle_animation);
		self.animations.append(walking_animation);
		
		self.size = [self.animations[0].get_frame(False).get_size()[0],self.animations[0].get_frame(False).get_size()[1]];
		self.grounded = False;

		self.speed = [0.25*self.size[0]/100.0,0];


	def update(self,delta):
		self.animations[self.current_action].update(delta);
		off = self.size[1]*10/84;
		if(self.speed[1] > off):
			self.speed[1] = off;
		if(self.speed[1] < -off):
			self.speed[1] = -off;

	def draw(self,display,camera):
		display.blit(self.animations[self.current_action].get_frame(not self.facing_right),(self.position[0]-camera[0],self.position[1]-camera[1]));
		#pg.draw.rect(display,(255,0,0),self.get_rect());

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self):
		if(self.facing_right):
			return Rect(self.position[0]+(0.3*self.size[0]),self.position[1]+(10*self.size[1]/84),self.size[0]-(0.6*self.size[0]),self.size[1]-(10*self.size[1]/84));
		return Rect(self.position[0]+(0.3*self.size[0]),self.position[1]+(10*self.size[1]/84),self.size[0]-(0.6*self.size[0]),self.size[1]-(10*self.size[1]/84));