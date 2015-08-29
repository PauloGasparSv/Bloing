import pygame as pg;
from pygame.locals import *;

class Smart_Background:
	def __init__(self,image,position,subd,sub_width,speed):
		self.width = image.get_width()/subd;
		height = image.get_height();
		self.speed = speed;
		self.frames = [];
		
		self.sub_div = subd;

		for i in range(0,subd):
			self.frames.append(image.subsurface((i*self.width,0,self.width,height)));

		self.start = 0;
		self.end = subd;
   
		self.width = sub_width;

		self.initial_position = position
		self.position = [position[0],position[1]];

	def update(self,delta,camera):
		self.position[0] = self.initial_position[0] - camera[0] * self.speed;
		self.position[1] = self.initial_position[1] - camera[1] * self.speed;
		self.start = (int)(-self.position[0]/1015);
		if(self.start < 0):
			self.start = 0;
		self.end = (int)(-self.position[0]+camera[2])/1015 + 1;
		if(self.end > self.sub_div):
			self.end = self.sub_div;

	def draw(self,display,camera,offset):
		for i in range(self.start,self.end):
			display.blit(self.frames[i],((self.position[0]+i*self.width)*offset[0],(self.position[1])*offset[1]));