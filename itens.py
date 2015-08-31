import pygame as pg;
from pygame.locals import *;
from animation import Animation;

class Coin:
	def __init__(self,position,sheet1,sheet2):
		self.position = position;
		self.rect = (self.position[0],self.position[1],56,56);
		self.visible  = False;
		self.taken = False;
		self.current_action = 0;

		self.animations = [Animation(sheet1,500,True),Animation(sheet2,500,True)];
		self.animations[1].set_once(True);

	def update(self,delta,player,camera):
		if(self.taken == False):
			self.animations[self.current_action].update(delta);
			if(self.rect[0]+self.rect[2] > camera[0]-1366 and self.rect[0] < camera[0]+1366 and
				self.rect[1]+self.rect[3] > camera[1]-768 and self.rect[1] < camera[1]+768):
				self.visible = True;
			else:
				self.visible = False;

			if(self.current_action == 0 and player.get_rect().colliderect(self.rect)):
				self.change_animation(1);
				player.cash += 1;
			if(self.current_action == 1 and self.animations[1].has_played):
				self.taken = True;

	def draw(self,display,camera,offset):
		if(self.visible and self.taken == False):
			display.blit(self.animations[self.current_action].get_frame(False),((self.rect[0]-camera[0])*offset[0],(self.rect[1]-camera[1])*offset[1]));
			

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self):
		return self.hit_rect;