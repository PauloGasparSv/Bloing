import pygame as pg;
from animation import Animation;
from player import Player;
from pygame.locals import *;
from tools import *;
from ground import *;
from goodog import *;

class Test_State: 
	def __init__(self,display,resolution):
		
		self.offset = (resolution[0]/1366.0,resolution[1]/768.0);
		
		#FONTE
		self.fonte = pg.font.SysFont("Courier",72);
		# IMAGE LOADING

		self.secret_image = load_scaled_image("Assets/Outros/zika.png",self.offset);
		self.show_secret_image = True;
   
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
		animationJUMP = Animation(frames,320,True);
		animationJUMP.set_once(True);

		self.player = Player(animationIDLE,animationWALK,animationJUMP,[10,200]);


		frames = [];
		for current in range(0,20):
			frames.append(load_scaled_image("Assets/Goodog/Andando/"+str(current)+".png",self.offset));
		animationWALK = Animation(frames,150,True);
		frames = [];
		for current in range(0,14):
			frames.append(load_scaled_image("Assets/Goodog/Hit/"+str(current)+".png",self.offset));
		animationDEATH = Animation(frames,120,True);
		animationDEATH.set_once(True);
		
		self.inimigos = []; 
		self.inimigos.append(Goodog(animationWALK,animationDEATH,True,[1000,470],(1800,1100)));
		
		self.pit_image = load_scaled_image("Assets/Outros/alpha_black.png",(self.offset[0]*0.43,self.offset[1]*0.34));


		tiles = [];
		for i in range (0,41):
			tiles.append(load_scaled_image("Assets/Tileset/"+str(i)+".png",self.offset));


		#GAME PLAY STUFF
		self.camera = [0,-200,1366,768];
		self.world_end = [-4900,5000];

		self.walking_areas = [];
		self.walking_areas.append(Plain_Ground(20,580,900,600,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1040,580,900,600,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1520,280,300,160,tiles,self.offset));

		self.mouse_position = [];
		self.hit = False;


		self.secret_combo = KeyCombo("UUDDLRLRBA");


	def update(self,delta,key):
		self.player.update(delta,key);

		if(key[K_s]):
			self.camera[1]+=0.2*delta;
		if(key[K_w]):
			self.camera[1]-=0.2*delta;

		self.mouse_position = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]];
		
		#HIT TEST TESTER
		if(self.player.get_rect().colliderect((self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]))):
			self.hit = True;
		else:
			self.hit = False;

		#PLAYER GROUND COLLISIONS
		self.player.grounded = False;
		for rect in self.walking_areas:
			rect.update(delta,self.player.position,self.camera);
			if(rect.active and self.player.grounded == False and rect.hit_test(self.player.get_rect()) and self.player.position[1] + self.player.size[1]-40 < rect.get_rect()[1] and self.player.speed[1] >= 0):
				self.player.position[1] = rect.get_rect()[1] - self.player.size[1]+5;
				self.player.grounded = True;
				self.player.double_jumps_counter = 0;
				self.player.speed[1] = 0;			
						

		#INIMIGOS
		for inimigo in self.inimigos:
			inimigo.update(delta,self.camera,self.player);


		#CAMERA UPDATE
		if(self.player.get_rect()[0] < -500 and self.player.get_rect()[0] < self.camera[0]+500 and 
		 self.camera[0] > self.world_end[0]+10):
			self.camera[0] -= delta * self.player.speed[0];
			if(self.player.get_rect()[0] < self.camera[0]+ 300):
				self.camera[0] -= 2*delta * self.player.speed[0];

		if(self.camera[0] > 10 and
		 self.player.get_rect()[0] < self.camera[0]+500):
			self.camera[0] -= delta * self.player.speed[0];
			if(self.player.get_rect()[0] < self.camera[0]+ 300):
				self.camera[0] -= 2*delta * self.player.speed[0];

		if(self.camera[0] < self.world_end[1] + 1356 and 
			self.player.position[0] + self.player.get_rect()[2] > self.camera[0]+866):
			self.camera[0] += delta * self.player.speed[0];
			if(self.player.get_rect()[0] > self.camera[0]+self.camera[2]- 300):
				self.camera[0] += 2*delta * self.player.speed[0];

		if(self.camera[1] < 0 and
		 self.player.get_rect()[1] > self.camera[1]+self.camera[3]-200):
			self.camera[1] += delta *(self.player.get_rect()[1] - self.camera[1])*0.001;


		elif(self.player.get_rect()[1] < self.camera[1]+275):
			self.camera[1] -= delta * (self.player.get_rect()[1]-self.camera[1])*0.001;


		# OFF WORLD LIMITS PLAYER
		if(self.player.get_rect()[1] >self.camera[1]+self.camera[3] + 300):
			self.player.speed[1] = 0;	
			self.player.change_animation(0);
			self.player.position = [0,200];
			self.player.double_jumps_counter = 0;
			self.player.grounded = False;


		self.secret_combo.update(delta,key);
		self.show_secret_image = self.secret_combo.activated;

	def draw(self,display):
		display.fill((255,255,255));

		for rect in self.walking_areas:
			rect.draw(display,self.camera,self.offset);

		for inimigo in self.inimigos:
			inimigo.draw(display,self.camera,self.offset);

		if(self.show_secret_image):
			display.blit(pg.transform.scale(self.secret_image,(300,300)),((-4890-self.camera[0])*self.offset[0],(200-self.camera[1])*self.offset[1]));
			display.blit(self.fonte.render("Emma Watson > Emma Stone",False,(0,0,0)),((-4890-self.camera[0])*self.offset[0],(120-self.camera[1])*self.offset[0]));
		
		self.player.draw(display,self.camera,self.offset);

		if(self.hit):
			pg.draw.rect(display,(255,0,0),(self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]));
		else:
			pg.draw.rect(display,(0,255,255),(self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]));

		
		#display.blit(self.pit_image,(820-self.camera[0],560-self.camera[1]));