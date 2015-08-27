import pygame as pg;
from pygame.locals import *;
import random;

class Plain_Ground:
	def __init__(self,x,y,w,h,tiles,offset):
		self.rect = Rect(x,y,w,h);
		self.active = False;
		self.visible = False;

		lines = h/150;
		columns = w/150;

		self.texture = pg.Surface((w,h),pg.SRCALPHA);
		#self.texture = pg.Surface((w,h));

		if(lines == 1):
			self.texture.blit(tiles[26],(0,0));
			self.texture.blit(tiles[27],((w-150)*offset[0],0));
			for c in range (1,columns-1):
				self.texture.blit(tiles[random.randint(28,29)],(c*150*offset[0],0));

		if(lines > 1):
			for l in range (0,lines):
				if(l == 0):
					self.texture.blit(tiles[0],(0,0));
					self.texture.blit(tiles[1],((w-150)*offset[0],0));
				elif(l == 1):
					self.texture.blit(tiles[12],(0,(150)*offset[1]));
					self.texture.blit(tiles[random.randint(14,15)],((w-150)*offset[0],150*offset[1]));
				else:
					self.texture.blit(tiles[random.randint(19,20)],(0,150*l));
					self.texture.blit(tiles[random.randint(21,22)],((w-150)*offset[0],150*l*offset[1]));
			for l in range(0,lines):
				for c in range(1,columns-1):
					if(l == 0):
						self.texture.blit(tiles[random.randint(2,5)],(c*150*offset[0],0));
					elif(l == 1):
						self.texture.blit(tiles[18],(c*150*offset[0],150*offset[1]));
					else:
						self.texture.blit(tiles[23],(c*150*offset[0],150*l*offset[1]));

	def update(self,delta,player_pos,camera):
		if(self.rect[0]+self.rect[2] > player_pos[0]-1366 and self.rect[0] < player_pos[0]+1366 and
			self.rect[1]+self.rect[3] > player_pos[1]-768 and self.rect[1] < player_pos[1]+768):
			self.active = True;
		else:
			self.active = False;

		if(self.rect[0]+self.rect[2] > camera[0]-1366 and self.rect[0] < camera[0]+1366 and
			self.rect[1]+self.rect[3] > camera[1]-768 and self.rect[1] < camera[1]+768):
			self.visible = True;
		else:
			self.visible = False;


	def draw(self,display,camera,offset):
		if(self.visible):
			display.blit(self.texture,((self.get_rect()[0]-camera[0])*offset[0],(self.get_rect()[1]-camera[1])*offset[1]));
			

	def hit_test(self,rect):
		return rect.colliderect(self.rect);

	def get_rect(self):
		return self.rect;

