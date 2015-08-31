import pygame as pg;
from pygame.locals import *;

def load_image(path):
	return pg.image.load(path).convert_alpha();
def load_scaled_image(path,offset):
	imagem = pg.image.load(path).convert_alpha();
	return pg.transform.scale(imagem,(int(imagem.get_size()[0]*offset[0]),int(imagem.get_size()[1]*offset[1])));
def load_scaled_image_no_alpha(path,offset):
	imagem = pg.image.load(path).convert();
	return pg.transform.scale(imagem,(int(imagem.get_size()[0]*offset[0]),int(imagem.get_size()[1]*offset[1])));

class KeyCombo:
	def __init__(self,combo):
		self.combo = combo;
		self.timer = 0;
		self.temp = "";
		self.kr = False;
		self.kl = False;
		self.ku = False;
		self.kd = False;
		self.kb = False;
		self.ka = False;
		self.activated = False;

	def update(self,delta,key):
		if(self.activated == False):
			if(key[K_RIGHT] == False and self.kr):
				self.kr = False;
			if(key[K_LEFT] == False and self.kl):
				self.kl = False;
			if(key[K_UP] == False and self.ku):
				self.ku = False;
			if(key[K_DOWN] == False and self.kd):
				self.kd = False;
			if(key[K_a] == False and self.ka):
				self.ka = False;
			if(key[K_b] == False and self.kb):
				self.kb = False;

			if(key[K_RIGHT] and self.kr == False):
				self.timer = 0;
				self.temp += "R";
				self.kr = True;
			elif(key[K_LEFT]  and self.kl == False):
				self.timer = 0;
				self.temp += "L";
				self.kl = True;
			elif(key[K_UP] and self.ku == False):
				self.timer = 0;
				self.temp += "U";
				self.ku = True;
			elif(key[K_DOWN] and self.kd == False):
				self.timer = 0;
				self.temp += "D";
				self.kd = True;
			elif(key[K_a] and self.ka == False):
				self.timer = 0;
				self.temp += "A";
				self.ka = True;
			elif(key[K_b] and self.kb == False):
				self.timer = 0;
				self.temp += "B";
				self.kb = True;

			self.timer += delta;
			if(self.timer > 800):
				self.timer = 0;
				self.temp = "";

			if(self.temp == self.combo):
				self.activated = True;

class FadeOut:	
	def __init__(self,speed):
		self.black = pg.Surface([1400,1400],pg.SRCALPHA,32).convert();
		self.alpha = 0;#TRANSPARENTE
		self.black.fill((0,0,0));
		self.black.set_alpha(0);
		self.speed = speed;
		self.activated = False;

	def isBlack(self):
		if(self.alpha == 255):
			return True;
		else:
			return False;


	def start(self):
		self.activated = True;

	def update(self,delta):
		if(self.activated):
			self.alpha += (self.speed * delta)/100.0;
			if(self.alpha > 255):
				self.alpha = 255;
			self.black.set_alpha(self.alpha);

	def draw(self,display):
		if(self.activated):
			display.blit(self.black,(0,0));

	def stop(self):
		self.activated = False;

class FadeIn:
	def __init__(self,speed):
		self.black = pg.Surface([1400,1400],pg.SRCALPHA,32).convert();
		self.alpha = 255;#OPACO
		self.black.fill((0,0,0));
		self.black.set_alpha(255);
		self.speed = speed;
		self.activated = False;

	def isBlack(self):
		if(self.alpha != 0):
			return True;
		else:
			return False;
 
	def start(self):
		self.activated = True;

	def update(self,delta):
		if(self.activated):
			self.alpha -= (self.speed * delta)/100.0;
			if(self.alpha < 0):
				self.alpha = 0;
			self.black.set_alpha(self.alpha);

	def draw(self,display):
		if(self.activated):
			display.blit(self.black,(0,0));

	def stop(self):
		self.activated = False;