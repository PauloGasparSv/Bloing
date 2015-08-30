import pygame as pg;
from pygame.locals import *;

class Player:
	def __init__(self,idle_animation,walking_animation,jumping_animation,death_animation,attack_animation,pos):
		self.current_action = 0;
		self.initial_position = (pos[0],pos[1]);
		self.position = pos;
		self.facing_right = True;
		self.animations = [idle_animation,walking_animation,jumping_animation,death_animation,attack_animation];
		self.size = [100,84];
		self.grounded = False;
		self.speed = [0.25,0];
		self.double_jumps_counter = 0;
		self.pressing_right = False;
		self.pressing_left = False;
		self.pressing_z = False;
		self.pressing_x = False;


	def update(self,delta,key,camera,walking_areas):
		print(self.position);
		if(self.current_action == 3 and self.animations[self.current_action].has_played):
			self.position[0] = self.initial_position[0];
			self.position[1] = self.initial_position[1];			
			self.change_animation(0);
			if(self.position[0] - camera[0] > 2500):
				camera[0] += self.position[0]- camera[0];
			elif(self.position[0] - camera[0] < -2500):
				camera[0] -= camera[0]-self.position[0];
			if(self.position[1] - camera[1] > 1500):
			 	camera[1] += 1500;
			elif(self.position[1] - camera[1] < -1500):
				camera[1] -= 1500;

		if(key[K_LSHIFT] and self.speed[0] == 0.25):
			self.speed[0] = 0.3;
			self.animations[1].set_speed(1200);
		if(self.speed[0] == 0.3 and key[K_LSHIFT] == False):
			self.speed[0] = 0.25;
			self.animations[1].set_speed(960);

		if(key[K_RIGHT] == False and self.pressing_right == True):
			self.pressing_right = False;
			if(self.current_action != 4):
				self.speed[0] = 0;
		if(key[K_LEFT] == False and self.pressing_left == True):
			self.pressing_left = False;
			if(self.current_action != 4):
				self.speed[0] = 0;
		if(key[K_z] == False and self.pressing_z == True):
			self.pressing_z = False;

		#WALKING
		if(key[K_RIGHT] and self.current_action < 3):
			self.pressing_right = True;
			self.facing_right = True;
			if(self.speed[0] != 0.3):
				self.speed[0] = 0.25;
			if(self.current_action != 1 and self.grounded == True ):
				self.change_animation(1);


		elif(key[K_LEFT] and self.current_action < 3):
			self.pressing_left = True;
			self.facing_right = False;
			if(self.speed[0] != 0.3):
				self.speed[0] = 0.25;
			if(self.current_action != 1 and self.grounded == True  and self.current_action < 3):
				self.change_animation(1);		
		else:
			if(self.current_action!=0 and self.grounded == True and self.current_action < 3):
				self.change_animation(0);
				self.speed[0] = 0;


		if(self.grounded and key[K_z] and self.pressing_z == False and self.current_action != 3):
			self.pressing_z = True;
			self.position[1] -= 20;
			self.speed[1] = -12;
			self.change_animation(2);

		if(self.grounded == False and key[K_z] and self.pressing_z == False and self.double_jumps_counter == 0 and self.current_action != 3):
			self.double_jumps_counter += 1;
			self.pressing_z = True;
			self.position[1] -= 15;
			self.speed[1] = -7;
			self.change_animation(2);

		if(key[K_x] == False and self.pressing_x):
			self.pressing_x = False;

		if(key[K_x] and self.pressing_x == False and self.current_action < 3):
			self.pressing_x = True;
			self.change_animation(4);

		if(self.current_action == 4 and self.animations[4].has_played):
			self.change_animation(0);

		self.grounded = False;
		for rect in walking_areas:
			rect.update(delta,self.position,camera);
			if(rect.active and self.grounded == False and rect.hit_test(self) and self.position[1] + self.size[1]-40 < rect.get_rect()[1] and self.speed[1] >= 0):
				self.position[1] = rect.get_rect()[1] - self.size[1]+15;
				self.grounded = True;
				self.double_jumps_counter = 0;
				self.speed[1] = 0;			

		if(self.grounded == False):
			self.speed[1] += delta * 0.025;
			if(self.current_action < 2):
				self.change_animation(2);
		else:
			if(self.current_action == 4):
				self.speed[0] = 0;
		

		self.position[1] += self.speed[1]*delta * 0.058;
		if(self.speed[0] != 0 and self.facing_right and self.current_action != 3):
			self.position[0] += delta * self.speed[0];
		elif(self.speed[0] != 0 and self.facing_right == False and self.current_action != 3):
			self.position[0] -= delta * self.speed[0];

		self.animations[self.current_action].update(delta);
		if(self.speed[1] > 10):
			self.speed[1] = 10;
		if(self.speed[1] < -10):
			self.speed[1] = -10;

	def draw(self,display,camera,offset):
		display.blit(self.animations[self.current_action].get_frame(not self.facing_right),((self.position[0]-camera[0])*offset[0],(self.position[1]-camera[1])*offset[1]));
		#pg.draw.rect(display,(0,255,255),(offset[0]*(self.get_attack_rect()[0]-camera[0]),offset[1]*(self.get_attack_rect()[1]-camera[1]),offset[0]*self.get_attack_rect()[2],offset[1]*self.get_attack_rect()[3]))

	def change_animation(self,action):
		self.animations[self.current_action].stop();
		self.current_action = action;
		self.animations[self.current_action].play();

	def get_rect(self):
		if(self.facing_right):
			return Rect(self.position[0]+0.3*self.size[0],self.position[1]+10,self.size[0]-0.6*self.size[0],self.size[1]-10);
		return Rect(self.position[0]+0.3*self.size[0],self.position[1]+10,self.size[0]-0.6*self.size[0],self.size[1]-10);

	def get_attack_rect(self):
		if(self.current_action == 4 and self.animations[self.current_action].curr_frame > 8 and self.animations[self.current_action].curr_frame < 16):
			if(self.facing_right):
				return Rect(self.position[0]+self.size[0]-45,self.position[1]+15,40,60);
			return Rect(self.position[0]-5,self.position[1]+15,40,60);
		return Rect(0,0,0,0);
