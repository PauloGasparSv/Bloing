import pygame as pg;
from pygame.locals import *;
from animation import Animation;

class Goodog:
	def __init__(self,walk_frames,death_frames,facing_right,pos,destination):
		self.current_action = 0;
		self.position = pos;
		self.facing_right = facing_right;

		self.animations = [Animation(walk_frames,600,True),Animation(death_frames,480,True)];
		self.animations[1].set_once(True);
		
		self.size = [80,115];
		self.grounded = False;

		self.speed = [0.12,0];

		self.destination = destination;
		self.active = False;

	def set_routina(self,dest1,dest2):
		self.destination = [dest1,dest2];

	def update(self,delta,camera,player):
		if(self.get_rect()[0]+self.get_rect()[2] > camera[0]-100 and self.get_rect()[0] < camera[0]+camera[2]+100 and
			self.get_rect()[1]+self.get_rect()[3] > camera[1]-100 and self.get_rect()[1] < camera[1]+camera[3]+100):
			self.active = True;
		else:
			self.active = False;

		if((self.current_action == 1 and self.animations[self.current_action].has_played == True) == False):
			self.animations[self.current_action].update(delta);
			if(self.speed[1] > 10):
				self.speed[1] = 10;
			if(self.speed[1] < -10):
				self.speed[1] = -10;

			if(self.current_action == 0):
				if(self.facing_right):
					self.position[0] += self.speed[0] * delta;
					if(self.position[0] + self.speed[0]*delta > self.destination[0]):
						self.facing_right = False;
				if(self.facing_right == False):
					self.position[0] -= self.speed[0] * delta;
					if(self.position[0] + self.speed[0]*delta < self.destination[1]):
						self.facing_right = True;
				if(self.get_rect().colliderect(player.get_attack_rect())):
						if(player.facing_right):
							self.position[0] += 25;
						else:
							self.position[0] -= 25;
						self.change_animation(1);

				if(self.current_action != 1 and player.get_rect().colliderect(self.get_rect())):
					if(player.get_rect()[1]+player.get_rect()[3] < self.get_rect()[1]+25 and player.speed[1] > 0):
						self.change_animation(1);
						player.change_animation(2);
						player.position[1] -= 21;
						player.speed[1] = -12;
						player.double_jumps_counter = 0;
					elif(player.current_action != 3):
						player.change_animation(3);

	def draw(self,display,camera,offset):
		if(self.active):
			display.blit(self.animations[self.current_action].get_frame(self.facing_right),((self.position[0]-camera[0])*offset[0],(self.position[1]-camera[1])*offset[1]));
		

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self):
		return Rect(self.position[0],self.position[1],self.size[0],self.size[1]);
		