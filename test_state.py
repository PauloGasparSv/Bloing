import pygame as pg;
from animation import Animation;
from player import Player;
from pygame.locals import *;

class Test_State:
	def __init__(self,display):
		
		# IMAGE LOADING

		frames = [];
		imagem = pg.image.load("Assets/Bloshi/parado.png").convert_alpha();
		w = imagem.get_size()[0]/10;
		h = imagem.get_size()[1]/2;
		for linha in range(0,2):
			for coluna in range(0,10):
				frames.append(imagem.subsurface(coluna*w,linha*h,w,h));
		animationIDLE = Animation(frames,200,True);

		frames = [];
		imagem = pg.image.load("Assets/Bloshi/correndo.png").convert_alpha();
		w = imagem.get_size()[0]/10;
		h = imagem.get_size()[1]/2;
		for linha in range(0,2):
			for coluna in range(0,10):
				frames.append(imagem.subsurface(coluna*w,linha*h,w,h));
		animationWALK = Animation(frames,240,True);


		self.player = Player(animationIDLE,animationWALK,[0,0]);

		# GAME PLAY STUFF

		self.walking_areas = [];
		self.walking_areas.append(Rect(100,580,400,200));

		for i in range(0,10):
			self.walking_areas.append(Rect(560+i*50,600-i*2,50,200));
		for i in range(0,10):
			self.walking_areas.append(Rect(1080+i*50,600-i*10,50,200));
	



	def update(self,delta,key):
		self.player.update(delta);

		if(key[K_RIGHT]):
			self.player.position[0] += delta * self.player.speed[0];
			self.player.facing_right = True;
			if(self.player.current_action != 1):
				self.player.change_animation(1);


		elif(key[K_LEFT]):
			self.player.position[0] -= delta * self.player.speed[0];
			self.player.facing_right = False;
			if(self.player.current_action != 1):
				self.player.change_animation(1);

		else:
			if(self.player.current_action!=0):
				self.player.change_animation(0);

		self.player.grounded = False;
		for rect in self.walking_areas:
			if(rect.colliderect(self.player.get_rect()) and self.player.position[1] + self.player.size[1]-20 < rect[1]):
				self.player.position[1] = rect[1] - self.player.size[1]+6;
				self.player.grounded = True;
				self.player.speed[1] = 0;
				break;
		
		if(self.player.grounded == False):
			self.player.speed[1] += delta * 0.022;
			
		self.player.position[1] += self.player.speed[1];

	def draw(self,display):
		display.fill((255,255,255));

		for rect in self.walking_areas:
			pg.draw.rect(display,(20,20,20),rect);
			pg.draw.rect(display,(0,255,0),(rect[0],rect[1],rect[2],20));

		self.player.draw(display);