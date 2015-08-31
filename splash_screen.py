import pygame as pg;
from pygame.locals import *;
from tools import FadeOut;
from tools import FadeIn;

class Splash_Screen:
	def __init__(self,display,resolution):
		self.offset = (resolution[0]/1366.0,resolution[1]/768.0);
		self.fonte = pg.font.SysFont("Courier",72);

		self.fadeIn = FadeIn(12);
		self.fadeOut = FadeOut(20);

		self.fadeIn.start();

		self.next_state = False;

	def update(self,delta,key):
		self.fadeIn.update(delta);
		self.fadeOut.update(delta);
		if(self.fadeIn.isBlack() == False):
			self.fadeOut.start();
		if(self.fadeOut.isBlack()):
			self.next_state = True;

	def draw(self,display):
		display.blit(self.fonte.render("Disclaimer: Made by one guy",False,(255,255,255)),(50*self.offset[0],350*self.offset[1]));
		display.blit(self.fonte.render("And Allan SEU JUDAS",False,(20,20,20)),(150*self.offset[0],450*self.offset[1]));
		self.fadeIn.draw(display);
		self.fadeOut.draw(display);