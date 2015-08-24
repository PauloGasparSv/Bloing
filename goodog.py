import pygame as pg;
from pygame.locals import *;

class Goodog:
	def __init__(self,walking_animation,death_animation,facing_right,pos,destination):
		self.current_action = 0;
		self.position = pos;
		self.facing_right = facing_right;

		self.animations = [walking_animation,death_animation];
		
		self.size = [80,115];
		self.grounded = False;

		self.speed = [0.2,0];

		self.destination = destination;

	def set_routina(self,dest1,dest2):
		self.destination = [dest1,dest2];

	def update(self,delta,player):
		self.animations[self.current_action].update(delta);
		if(self.speed[1] > 10):
			self.speed[1] = 10;
		if(self.speed[1] < -10):
			self.speed[1] = -10;

		if(self.current_action == 0):
			if(self.facing_right):
				self.position[0] += self.speed[0] * delta;
				if(self.position[0] + self.speed[0]*delta > self.destination[0]):
					self.facing_right = False;
			if(self.facing_right == False):
				self.position[0] -= self.speed[0] * delta;
				if(self.position[0] + self.speed[0]*delta < self.destination[1]):
					self.facing_right = True;

			if(player.get_rect().colliderect(self.get_rect()) and player.get_rect()[1]+player.get_rect()[3] > self.get_rect()[1]+30 and player.speed[1] > 0):
				self.change_animation(1);
				player.change_animation(2);
				player.position[1] -= 20;
				player.speed[1] = -10;
				player.double_jumps_counter = 0;


	def draw(self,display,camera,offset):
		display.blit(self.animations[self.current_action].get_frame(self.facing_right),((self.position[0]-camera[0])*offset[0],(self.position[1]-camera[1])*offset[1]));

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self):
		return Rect(self.position[0],self.position[1],self.size[0],self.size[1]);
		