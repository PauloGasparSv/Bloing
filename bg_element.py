import pygame as pg;
from pygame.locals import *;
from animation import Animation;

class Bg_Element:
	def __init__(self,x,y,sprite):
		self.position = [x,y];
		self.rect = (self.position[0],self.position[1],56,56);
		self.visible  = False;
		self.image = sprite;

	def update(self,delta,player,camera):
		if(self.rect[0]+self.rect[2] > camera[0]-1366 and self.rect[0] < camera[0]+1366 and
			self.rect[1]+self.rect[3] > camera[1]-768 and self.rect[1] < camera[1]+768):
			self.visible = True;
		else:
			self.visible = False;

	def draw(self,display,camera,offset):
		if(self.visible):
			display.blit(self.image,((self.rect[0]-camera[0])*offset[0],(self.rect[1]-camera[1])*offset[1]));
			
	def get_rect(self):
		return self.hit_rect;