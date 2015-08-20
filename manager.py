import pygame as pg;
from pygame.locals import *;
from test_state import Test_State;

#-1 TESTE STATE

class Manager:
	def __init__(self,display):
		self.display = display;
		
		self.current_state_index = -1;
		self.current_state = Test_State(self.display);
			

	def update(self,delta):
		key = pg.key.get_pressed();
		self.current_state.update(delta,key);
		



	def draw(self):
		self.current_state.draw(self.display);



	def set_state(self,next_state):
		if(next_state == -1):
			self.current_state_index = next_state;
			self.current_state = Test_State(self.display);
