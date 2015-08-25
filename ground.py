import pygame as pg;
from pygame.locals import *;

class Plain_Ground:
	def __init__(self,x,y,w,h,offset):
		self.rect = Rect(x,y,w,h);
		self.active = False;

	def update(self,delta,camera):
		if(self.rect[0]+self.rect[2] > camera[0]-50 and self.rect[0] < camera[0]+camera[2]+50 and
			self.rect[1]+self.rect[3] > camera[1]-50 and self.rect[1] < camera[1]+camera[3]+50):
			self.active = True;
		else:
			self.active = False;



	def draw(self,display,camera,offset):
		pg.draw.rect(display,(50,20,20),((self.get_rect()[0]-camera[0])*offset[0],
			(self.get_rect()[1]-camera[1])*offset[1],self.get_rect()[2]*offset[0],self.get_rect()[3]*offset[1]));
	

	def hit_test(self,rect):
		return rect.colliderect(self.rect);

	def get_rect(self):
		return self.rect;

