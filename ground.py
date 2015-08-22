import pygame as pg;
from pygame.locals import *;

class Plain_Ground:
	def __init__(self,x,y,w,h,offset):
		self.rect = Rect(x*offset[0],y*offset[1],w*offset[0],h*offset[1]);

	def hit_test(self,rect):
		return rect.colliderect(self.rect);

	def get_rect(self):
		return self.rect;