import pygame as pg;
from pygame.locals import *;

class Player:
	def __init__(self,idle_animation,walking_animation,jumping_animation,pos):
		self.current_action = 0;

		self.position = pos;

		self.facing_right = True;

		self.animations = [idle_animation,walking_animation,jumping_animation];
		
		self.size = [self.animations[0].get_frame(False).get_size()[0],self.animations[0].get_frame(False).get_size()[1]];
		self.grounded = False;

		self.speed = [0.25*self.size[0]/100.0,0];

		self.double_jumps_counter = 0;


	def update(self,delta,offset):
		self.animations[self.current_action].update(delta);
		if(self.speed[1] > offset[1]*10):
			self.speed[1] = offset[1]*10;
		if(self.speed[1] < -offset[1]*10):
			self.speed[1] = -offset[1]*10;

	def draw(self,display,camera):
		display.blit(self.animations[self.current_action].get_frame(not self.facing_right),(self.position[0]-camera[0],self.position[1]-camera[1]));
		#pg.draw.rect(display,(255,0,0),self.get_rect());

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self,offset):
		if(self.facing_right):
			return Rect(self.position[0]+(0.3*self.size[0]),self.position[1]+(10*offset[1]),self.size[0]-(0.6*self.size[0]),self.size[1]-(10*offset[1]));
		return Rect(self.position[0]+(0.3*self.size[0]),self.position[1]+(10*offset[1]),self.size[0]-(0.6*self.size[0]),self.size[1]-(10*offset[1]));