import pygame as pg;
from animation import Animation;
from player import Player;
from pygame.locals import *;
from tools import *;
from ground import *;
from goodog import *;
from smart_background import *;

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
		animationIDLE = Animation(frames,800,True);
		frames = [];
		for current in range(0,20):
			frames.append(load_scaled_image("Assets/Bloshi/Correndo/"+str(current)+".png",self.offset));
		animationWALK = Animation(frames,960,True);
		frames = [];
		for current in range(0,20):  
			frames.append(load_scaled_image("Assets/Bloshi/Pulando/"+str(current)+".png",self.offset));
		animationJUMP = Animation(frames,1280,True);
		animationJUMP.set_once(True);
		frames = [];
		for current in range(0,20):  
			frames.append(load_scaled_image("Assets/Bloshi/Morrendo/"+str(current)+".png",self.offset));
		animationDEATH = Animation(frames,900,True);
		animationDEATH.set_once(True);
		frames = [];
		for current in range(0,20):  
			frames.append(load_scaled_image("Assets/Bloshi/Atacando/"+str(current)+".png",self.offset));
		animationATTACK = Animation(frames,900,True);
		animationATTACK.set_once(True);

		self.player = Player(animationIDLE,animationWALK,animationJUMP,animationDEATH,animationATTACK,[20,-200]);
		
		



		self.sprites = [[],[],[]];
		self.sprites[0].append(animationIDLE.frame);
		self.sprites[0].append(animationWALK.frame);
		self.sprites[0].append(animationJUMP.frame);
		self.sprites[0].append(animationDEATH.frame);
		self.sprites[0].append(animationATTACK.frame);

		idle = [];
		for current in range(0,20):
			idle.append(load_scaled_image("Assets/Grace/Parado/"+str(current)+".png",self.offset));
		walk = [];
		for current in range(0,20):
			walk.append(load_scaled_image("Assets/Grace/Correndo/"+str(current)+".png",self.offset));
		jump = [];
		for current in range(0,20):  
			jump.append(load_scaled_image("Assets/Grace/Pulando/"+str(current)+".png",self.offset));
		death = [];
		for current in range(0,20):  
			death.append(load_scaled_image("Assets/Grace/Morrendo/"+str(current)+".png",self.offset));
		atk = [];
		for current in range(0,16):  
			atk.append(load_scaled_image("Assets/Grace/Atacando/"+str(current)+".png",self.offset));
		self.sprites[1].append(idle);
		self.sprites[1].append(walk);
		self.sprites[1].append(jump);
		self.sprites[1].append(death);
		self.sprites[1].append(atk);

		idle = [];
		for current in range(0,20):
			idle.append(load_scaled_image("Assets/Sparklez/Parado/"+str(current)+".png",self.offset));
		walk = [];
		for current in range(0,20):
			walk.append(load_scaled_image("Assets/Sparklez/Correndo/"+str(current)+".png",self.offset));
		jump = [];
		for current in range(0,20):  
			jump.append(load_scaled_image("Assets/Sparklez/Pulando/"+str(current)+".png",self.offset));
		death = [];
		for current in range(0,20):  
			death.append(load_scaled_image("Assets/Sparklez/Morrendo/"+str(current)+".png",self.offset));
		atk = [];
		for current in range(0,16):  
			atk.append(load_scaled_image("Assets/Sparklez/Atacando/"+str(current)+".png",self.offset));
		self.sprites[2].append(idle);
		self.sprites[2].append(walk);
		self.sprites[2].append(jump);
		self.sprites[2].append(death);
		self.sprites[2].append(atk);







		walk_frames = [];
		for current in range(0,20):
			walk_frames.append(load_scaled_image("Assets/Goodog/Andando/"+str(current)+".png",self.offset));
		
		death_frames = [];
		for current in range(0,14):
			death_frames.append(load_scaled_image("Assets/Goodog/Hit/"+str(current)+".png",self.offset));
		
		
		self.inimigos = []; 
		self.inimigos.append(Goodog(walk_frames,death_frames,True,[1000,520],(1800,1100)));
		self.inimigos.append(Goodog(walk_frames,death_frames,True,[1900,520],(1800,1100)));
		
		self.pit_image = load_scaled_image("Assets/Outros/alpha_black.png",(self.offset[0]*0.43,self.offset[1]*0.34));


		tiles = [];
		for i in range (0,41):
			tiles.append(load_scaled_image("Assets/Tileset/"+str(i)+".png",self.offset));


		self.background = [];
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada4.png",self.offset),[-600,220],4,1015,0.1));
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada3.png",self.offset),[100,210],4,1015,0.2));
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada2.png",self.offset),[0,200],4,1015,0.3));
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada1.png",self.offset),[-10,230],4,1015,0.4));
		


		#GAME PLAY STUFF
		self.camera = [0,-600,1366,768];
		self.world_end = [-4900,5000];

		self.walking_areas = []; 
		self.walking_areas.append(Plain_Ground(20,620,900,600,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1040,620,4500,600,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1520,320,300,160,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1950,180,900,160,tiles,self.offset));

		self.mouse_position = [];
		self.hit = False;


		self.pressing_c = False;
		self.curr_c = 0;

		self.secret_combo = KeyCombo("UUDDLRLRBA");


	def update(self,delta,key):
		self.player.update(delta,key,self.camera,self.walking_areas);

		if(self.pressing_c and key[K_c] == False):
			self.pressing_c = False;
		if(key[K_c] and self.pressing_c == False):
			self.pressing_c = True;
			self.curr_c += 1;
			if(self.curr_c > 2):
				self.curr_c = 0;
			for i in range(0,5):
				self.player.animations[i].change_sprites(self.sprites[self.curr_c][i]);

		self.mouse_position = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]];
		
		#HIT TEST TESTER
		if(self.player.get_rect().colliderect((self.mouse_position[0],self.mouse_position[1],30*self.offset[0],30*self.offset[1]))):
			self.hit = True;
		else:
			self.hit = False;

		#PLAYER GROUND COLLISIONS
		

		#INIMIGOS
		for inimigo in self.inimigos:
			inimigo.update(delta,self.camera,self.player);


		#CAMERA UPDATE
		if(self.player.get_rect()[0] < -500 and self.player.get_rect()[0] < self.camera[0]+500 and 
		 self.camera[0] > self.world_end[0]+10):
			if(self.player.speed[0] == 0.3):
				self.camera[0] -= delta * 0.3;
			else:
				self.camera[0] -= delta * 0.25;
			if(self.player.get_rect()[0] < self.camera[0]+ 300):
				self.camera[0] -= 2*delta * 0.25;

		if(self.camera[0] > 10 and
		 self.player.get_rect()[0] < self.camera[0]+500):
			if(self.player.speed[0] == 0.3):
				self.camera[0] -= delta * 0.3;
			else:
				self.camera[0] -= delta * 0.25;
			if(self.player.get_rect()[0] < self.camera[0]+ 300):
				self.camera[0] -= 2*delta * 0.25;

		if(self.camera[0] < self.world_end[1] + 1356 and 
			self.player.position[0] + self.player.get_rect()[2] > self.camera[0]+866):
			if(self.player.speed[0] == 0.3):
				self.camera[0] += delta * 0.3;
			else:
				self.camera[0] += delta * 0.25;
			if(self.player.get_rect()[0] > self.camera[0]+self.camera[2]- 300):
				self.camera[0] += 2*delta * 0.25;

		if(self.camera[1] < 0 and
		 self.player.get_rect()[1] > self.camera[1]+self.camera[3]-230):
			self.camera[1] += delta *0.45;


		elif(self.player.get_rect()[1] < self.camera[1]+320):
			self.camera[1] -= delta *0.45;

		for bg in self.background:
			bg.update(delta,self.camera);


		# OFF WORLD LIMITS PLAYER
		if(self.player.get_rect()[1] >self.camera[1]+self.camera[3] + 300):
			self.player.speed[1] = 0;	
			self.player.change_animation(0);
			self.player.position = [20,-200];
			if(self.player.position[0] - self.camera[0] > 2500):
				self.camera[0] += self.player.position[0]-self.camera[0];
			elif(self.player.position[0] - self.camera[0] < -2500):
				self.camera[0] -= self.camera[0]-self.player.position[0];
			if(self.player.position[1] - self.camera[1] > 1500):
			 	self.camera[1] += 1500;
			elif(self.player.position[1] - self.camera[1] < -1500):
				self.camera[1] -= 1500;
			self.player.double_jumps_counter = 0;
			self.player.grounded = False;


		self.secret_combo.update(delta,key);
		self.show_secret_image = self.secret_combo.activated;

	def draw(self,display):
		display.fill((185,235,250));

		for bg in self.background:
			bg.draw(display,self.camera,self.offset);

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