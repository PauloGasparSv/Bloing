import pygame as pg;
from pygame.locals import *;

class Player:
	def __init__(self,idle_animation,walking_animation,jumping_animation,pos):
		self.current_action = 0;
		self.position = pos;
		self.facing_right = True;
		self.animations = [idle_animation,walking_animation,jumping_animation];
		self.size = [100,84];
		self.grounded = False;
		self.speed = [0.25,0];
		self.double_jumps_counter = 0;
		self.pressing_right = False;
		self.pressing_left = False;
		self.pressing_z = False;


	def update(self,delta,key):
		if(key[K_RIGHT] == False and self.pressing_right == True):
			self.pressing_right = False;
		if(key[K_LEFT] == False and self.pressing_left == True):
			self.pressing_left = False;
		if(key[K_z] == False and self.pressing_z == True):
			self.pressing_z = False;

		#WALKING
		if(key[K_RIGHT]):
			self.pressing_right = True;
			self.position[0] += delta * self.speed[0];
			self.facing_right = True;
			if(self.current_action != 1 and self.grounded == True):
				self.change_animation(1);

		elif(key[K_LEFT]):
			self.pressing_left = True;
			self.position[0] -= delta * self.speed[0];
			self.facing_right = False;
			if(self.current_action != 1 and self.grounded == True):
				self.change_animation(1);
		
		else:
			if(self.current_action!=0 and self.grounded == True):
				self.change_animation(0);

		if(self.grounded and key[K_z] and self.pressing_z == False):
			self.pressing_z = True;
			self.position[1] -= 20;
			self.speed[1] = -12;
			self.change_animation(2);

		if(self.grounded == False and key[K_z] and self.pressing_z == False and self.double_jumps_counter == 0):
			self.double_jumps_counter += 1;
			self.pressing_z = True;
			self.position[1] -= 15;
			self.speed[1] = -7;
			self.change_animation(2);

			
		if(self.grounded == False):
			self.speed[1] += delta * 0.025;
			if(self.current_action != 2):
				self.change_animation(2);
		

		self.position[1] += self.speed[1]*delta * 0.058;


		self.animations[self.current_action].update(delta);
		if(self.speed[1] > 10):
			self.speed[1] = 10;
		if(self.speed[1] < -10):
			self.speed[1] = -10;

	def draw(self,display,camera,offset):
		for i in range(-20,20):
			display.blit(self.animations[self.current_action].get_frame(not self.facing_right),((self.position[0]-camera[0])*offset[0],(self.position[1]-camera[1]+84*i)*offset[1]));

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self):
		if(self.facing_right):
			return Rect(self.position[0]+0.3*self.size[0],self.position[1]+10,self.size[0]-0.6*self.size[0],self.size[1]-10);
		return Rect(self.position[0]+0.3*self.size[0],self.position[1]+10,self.size[0]-0.6*self.size[0],self.size[1]-10);