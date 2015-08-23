import pygame as pg;
from pygame.locals import *;

class Plain_Ground:
	def __init__(self,x,y,w,h,offset):
		self.rect = Rect(x*offset[0],y*offset[1],w*offset[0],h*offset[1]);
		self.active = False;

	def update(self,delta,camera,offset):
		if(self.rect[0]+self.rect[2] > camera[0]-50*offset[0] and self.rect[0] < camera[0]+camera[2]+50*offset[0] and
			self.rect[1]+self.rect[3] > camera[1]-50*offset[1] and self.rect[1] < camera[1]+camera[3]+50*offset[1]):
			self.active = True;



	def draw(self,display,camera):
		pg.draw.rect(display,(50,20,20),(self.get_rect()[0]-camera[0],
			self.get_rect()[1]-camera[1],self.get_rect()[2],self.get_rect()[3]));
		pg.draw.rect(display,(0,255,0),(self.get_rect()[0]-camera[0],
			self.get_rect()[1]-camera[1],self.get_rect()[2],20));

	def hit_test(self,rect):
		return rect.colliderect(self.rect);

	def get_rect(self):
		return self.rect;

