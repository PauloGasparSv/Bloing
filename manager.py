import pygame as pg;
from pygame.locals import *;
from test_state import Test_State;

#-1 TESTE STATE

class Manager:
	def __init__(self):
		#RESOLTUIONS ISSUES
		self.RESOLUTIONS = [(1366,768),(683,384),(1024,768),(800,600)];
		self.FULL_SCREEN = False;

		self.WIDTH = pg.display.Info().current_w;
		self.HEIGHT = pg.display.Info().current_h;

		self.resolution = 3;
		for i in range(0,4):
			if(self.RESOLUTIONS[i][0] == self.WIDTH and self.RESOLUTIONS[i][1] == self.HEIGHT):
				self.resolution = i;

		if(self.FULL_SCREEN == False):
			self.display = pg.display.set_mode(self.RESOLUTIONS[self.resolution]);
		else:
			self.display = pg.display.set_mode(self.RESOLUTIONS[self.resolution],pg.FULLSCREEN);


		#TAKE OFF IF RELEASE
		self.change_resolution(1);

		#GAME STATES
		self.current_state_index = -1;
		self.current_state = Test_State(self.display,self.RESOLUTIONS[self.resolution]);
			

	def update(self,delta):
		key = pg.key.get_pressed();
		self.current_state.update(delta,key);
		



	def draw(self):
		self.current_state.draw(self.display);



	def set_state(self,next_state):
		if(next_state == -1):
			self.current_state_index = next_state;
			self.current_state = Test_State(self.display,self.RESOLUTIONS[self.resolution]);

	def change_resolution(self,res):
		self.resolution = res;	
		if(self.FULL_SCREEN == False):
			self.display = pg.display.set_mode(self.RESOLUTIONS[self.resolution]);
		else:
			self.display = pg.display.set_mode(self.RESOLUTIONS[self.resolution],pg.FULLSCREEN);