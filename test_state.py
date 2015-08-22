import pygame as pg;
from animation import Animation;
from player import Player;
from pygame.locals import *;
from tools import *;
from ground import *;

class Test_State:
	def __init__(self,display,resolution):
		
		self.offset = (resolution[0]/1366.0,resolution[1]/768.0);
		
		# IMAGE LOADING

		frames = [];
		for current in range(0,20):
			frames.append(load_scaled_image("Assets/Bloshi/Parado/"+str(current)+".png",self.offset));
		animationIDLE = Animation(frames,200,True);

		frames = [];
		for current in range(0,20):
			frames.append(load_scaled_image("Assets/Bloshi/Correndo/"+str(current)+".png",self.offset));
		animationWALK = Animation(frames,240,True);

		frames = [];
		for current in range(0,20):
			frames.append(load_scaled_image("Assets/Bloshi/Pulando/"+str(current)+".png",self.offset));
		animationJUMP = Animation(frames,350,True);
		animationJUMP.set_once(True);


		self.player = Player(animationIDLE,animationWALK,animationJUMP,[0,200]);

		#GAME PLAY STUFF
		self.camera = [0,-100,resolution[0],resolution[1]];
		self.world_end = 5000*self.offset[0];	

		self.walking_areas = [];
		self.walking_areas.append(Plain_Ground(20,580,800,200,self.offset));
		self.walking_areas.append(Plain_Ground(1040,580,800,200,self.offset));
		
		for i in range(0,20):
			self.walking_areas.append(Plain_Ground(1840+20*i,580-4*i,20,200,self.offset));


		self.walking_areas.append(Plain_Ground(1000,450,200,50,self.offset));

		self.mouse_position = [];
		self.hit = False;


		self.pressing_right = False;
		self.pressing_left = False;
		self.pressing_z = False;




	def update(self,delta,key):
		self.player.update(delta);

		self.mouse_position = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]];
		
		if(self.player.get_rect().colliderect((self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]))):
			self.hit = True;
		else:
			self.hit = False;


		if(key[K_d]):
			self.camera[0] += delta * self.player.speed[0];
		if(key[K_a]):
			self.camera[0] -= delta * self.player.speed[0];

		#PLAYER CONTROLS
		if(key[K_RIGHT] == False and self.pressing_right == True):
			self.pressing_right = False;
		if(key[K_LEFT] == False and self.pressing_left == True):
			self.pressing_left = False;
		if(key[K_z] == False and self.pressing_z == True):
			self.pressing_z = False;

		if(key[K_RIGHT]):
			self.pressing_right = True;
			self.player.position[0] += delta * self.player.speed[0];
			self.player.facing_right = True;
			if(self.player.current_action != 1 and self.player.grounded == True):
				self.player.change_animation(1);

		elif(key[K_LEFT]):
			self.pressing_left = True;
			self.player.position[0] -= delta * self.player.speed[0];
			self.player.facing_right = False;
			if(self.player.current_action != 1 and self.player.grounded == True):
				self.player.change_animation(1);
		
		else:
			if(self.player.current_action!=0 and self.player.grounded == True):
				self.player.change_animation(0);

	
		if(self.player.grounded and key[K_z] and self.pressing_z == False):
			self.pressing_z = True;
			self.player.position[1] -= 20;
			self.player.speed[1] -= 10;
			self.player.change_animation(2);



		#PLAYER COLLISIONS

		self.player.grounded = False;
		for rect in self.walking_areas:
			if(rect.hit_test(self.player.get_rect()) and self.player.position[1] + self.player.size[1]-20*self.offset[1] < rect.get_rect()[1]):
				self.player.position[1] = rect.get_rect()[1] - self.player.size[1]+6*self.offset[1];
				self.player.grounded = True;
				self.player.speed[1] = 0;
				break;
		
		if(self.player.grounded == False):
			self.player.speed[1] += delta * 0.022*self.offset[1];
			if(self.player.current_action != 2):
				self.player.change_animation(2);
			
		self.player.position[1] += self.player.speed[1];


		#pg.draw.rect(display,(0,255,255),(500,0,366,300));
		#pg.draw.rect(display,(0,255,255),(500,588,366,180));

		#CAMERA UPDATE
		if(self.camera[0] > 10*self.offset[0] and self.player.get_rect()[0] < self.camera[0]+500*self.offset[0]):
			self.camera[0] -= delta * self.player.speed[0];

		if(self.camera[0] < self.world_end + 1356*self.offset[0] and self.player.position[0] + self.player.get_rect()[2] > self.camera[0]+866*self.offset[0]):
			self.camera[0] += delta * self.player.speed[0];

		if(self.camera[1] < 0 and self.player.get_rect()[1]+self.player.get_rect()[3] > self.camera[1]+588*self.offset[1]):
			self.camera[1] += delta *(self.player.get_rect()[1] - self.camera[1])*0.001;

		if(self.player.get_rect()[1] < self.camera[1]+320*self.offset[1]):
			self.camera[1] -= delta * (self.player.get_rect()[1]-self.camera[1])*0.001;


	def mod(self,num):
		if(num < 0):
			num = -num
		return num;

	def draw(self,display):
		display.fill((255,255,255));

		for rect in self.walking_areas:
			pg.draw.rect(display,(20,20,20),(rect.get_rect()[0]-self.camera[0],rect.get_rect()[1]-self.camera[1],rect.get_rect()[2],rect.get_rect()[3]));
			pg.draw.rect(display,(0,255,0),(rect.get_rect()[0]-self.camera[0],rect.get_rect()[1]-self.camera[1],rect.get_rect()[2],20));

		


		self.player.draw(display,self.camera);

		if(self.hit):
			pg.draw.rect(display,(255,0,0),(self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]));
		else:
			pg.draw.rect(display,(0,255,255),(self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]));


		