import pygame as pg;
from pygame.locals import *;
import random;
import math;

class Ramp_45:
	def __init__(self,x,y,tiles,tipo,offset):
		self.rect = Rect(x,y,150,150);

		self.rects = [];
		self.hit_rect = Rect(0,0,0,0);

		self.active = False;
		self.visible = False;
		self.tipo = tipo;

		if(self.tipo == 0):
			self.texture = tiles[33];
			for i in range(0,50):
				self.rects.append(Rect(x+i*3,y+145-i*2.9,3,i*3));

		else:
			self.texture = tiles[34];
			for i in range(0,50):
				self.rects.append(Rect(x+150-i*3,y+145-i*2.9,3,i*3));

				

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
			display.blit(self.texture,((self.rect[0]-camera[0])*offset[0],(self.rect[1]-camera[1])*offset[1]));
			

	def hit_test(self,player):
		if(self.tipo == 0  and (player.facing_right == False and player.position[1]+player.get_rect()[2]>self.rect[1]+120)):
			return False;
		if(self.tipo == 1  and (player.facing_right == True and player.position[1]+player.get_rect()[2]>self.rect[1]+120)):
			return False;
		if(player.get_rect().colliderect(self.rect)):
			for r in self.rects:
				if(r.colliderect(player.get_rect())):
					self.hit_rect = r;
					return True;
		return False;

	def get_rect(self):
		return self.hit_rect;

class Plain_Ground:
	def __init__(self,x,y,w,h,tiles,offset):
		self.rect = Rect(x,y,w,h);
		self.active = False;
		self.visible = False;

		lines = h/150;
		columns = w/150;

		self.texture = [pg.Surface((w,h),pg.SRCALPHA)];
		#self.texture = pg.Surface((w,h));

		if(lines == 1):
			self.texture[0].blit(tiles[26],(0,0));
			self.texture[0].blit(tiles[27],((w-150)*offset[0],0));
			for c in range (1,columns-1):
				self.texture[0].blit(tiles[random.randint(28,29)],(c*150*offset[0],0));

		if(lines > 1):
			for l in range (0,lines):
				if(l == 0):
					self.texture[0].blit(tiles[0],(0,0));
					self.texture[0].blit(tiles[1],((w-150)*offset[0],0));
				elif(l == 1):
					self.texture[0].blit(tiles[12],(0,(150)*offset[1]));
					self.texture[0].blit(tiles[random.randint(14,15)],((w-150)*offset[0],150*offset[1]));
				else:
					self.texture[0].blit(tiles[random.randint(19,20)],(0,150*l));
					self.texture[0].blit(tiles[random.randint(21,22)],((w-150)*offset[0],150*l*offset[1]));
			for l in range(0,lines):
				for c in range(1,columns-1):
					if(l == 0):
						self.texture[0].blit(tiles[random.randint(2,5)],(c*150*offset[0],0));
					elif(l == 1):
						self.texture[0].blit(tiles[18],(c*150*offset[0],150*offset[1]));
					else:
						self.texture[0].blit(tiles[23],(c*150*offset[0],150*l*offset[1]));

		self.size = 1;
		if(w>1200):
			temp = self.texture[0];
			self.texture = [];
			div = w/150;
			while(div > 0):
				if(div>=10):
					self.texture.append(temp.subsurface(((self.size-1)*1500*offset[0],0,1500*offset[0],h)));
				else:	
					self.texture.append(temp.subsurface(((self.size-1)*150*div*offset[0],0,150*div*offset[0],h)));
				self.size+=1;
				div-=10;

		self.start = 0;
		self.end = 1;


	def update(self,delta,player_pos,camera):
		if(self.rect[0]+self.rect[2] > player_pos[0]-1366 and self.rect[0] < player_pos[0]+1366 and
			self.rect[1]+self.rect[3] > player_pos[1]-768 and self.rect[1] < player_pos[1]+768):
			self.active = True;
			if(self.size!=1):
				self.start = (int)(math.floor(camera[0]-self.rect[0])/(1500));
				self.end = self.start+3;
				if(self.end > self.size-1):
					self.end = self.size-1;
				if(self.start > self.size-1):
					self.start = self.size-1;
				if(self.start < 0):
					self.start = 0;
				if(self.end < 0):
					self.end = 0;
				
		else:
			self.active = False;

		if(self.rect[0]+self.rect[2] > camera[0]-1366 and self.rect[0] < camera[0]+1366 and
			self.rect[1]+self.rect[3] > camera[1]-768 and self.rect[1] < camera[1]+768):
			self.visible = True;
		else:
			self.visible = False;


	def draw(self,display,camera,offset):
		if(self.visible):
			if(self.size == 1):
				display.blit(self.texture[0],((self.get_rect()[0]-camera[0])*offset[0],(self.get_rect()[1]-camera[1])*offset[1]));
			else:
				for i in range(self.start,self.end):
					display.blit(self.texture[i],((self.get_rect()[0]-camera[0]+i*1500)*offset[0],(self.get_rect()[1]-camera[1])*offset[1]));

	def hit_test(self,player):
		return player.get_rect().colliderect(self.rect);

	def get_rect(self):
		return self.rect;


class Single_Tile:
	def __init__(self,x,y,tile,tiles,offset):
		self.rect = Rect(x,y,150,150);
		self.active = False;
		self.visible = False;


		self.texture = tiles[tile];

			

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
			

	def hit_test(self,player):
		return player.get_rect().colliderect(self.rect);

	def get_rect(self):
		return self.rect;

