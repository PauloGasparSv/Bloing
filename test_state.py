import pygame as pg;
from animation import Animation;
from player import Player;
from pygame.locals import *;
from tools import *;
from ground import *;
from goodog import *;
from smart_background import *;
from itens import *;
from bg_element import *;

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

		self.player = Player(animationIDLE,animationWALK,animationJUMP,animationDEATH,animationATTACK,[20,50]);
		
		

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


		coin_idle = [];
		for current in range(0,16):
			coin_idle.append(load_scaled_image("Assets/Itens/Moeda_Parada/"+str(current)+".png",self.offset));
		coin_taken = [];
		for current in range(0,20):
			coin_taken.append(load_scaled_image("Assets/Itens/Moeda_Pega/"+str(current)+".png",self.offset));
	
		self.itens = [];
		for i in range(0,4):
			self.itens.append(Coin((660+i*60,560),coin_idle,coin_taken));
			self.itens.append(Coin((1555+i*60,250),coin_idle,coin_taken));
			self.itens.append(Coin((2400+i*60,360),coin_idle,coin_taken));

		for i in range(0,15):
			self.itens.append(Coin((1960+i*60,130),coin_idle,coin_taken));
			self.itens.append(Coin((1960+i*60,80),coin_idle,coin_taken));
			self.itens.append(Coin((-1800+i*60,570),coin_idle,coin_taken));
			self.itens.append(Coin((-1800+i*60,530),coin_idle,coin_taken));

		walk_frames = [];
		for current in range(0,20):
			walk_frames.append(load_scaled_image("Assets/Goodog/Andando/"+str(current)+".png",self.offset));
		
		death_frames = [];
		for current in range(0,14):
			death_frames.append(load_scaled_image("Assets/Goodog/Hit/"+str(current)+".png",self.offset));
		
		
		self.inimigos = []; 
		self.inimigos.append(Goodog(walk_frames,death_frames,False,[1200,520],(1800,1100)));
		self.inimigos.append(Goodog(walk_frames,death_frames,True,[1900,520],(1800,1100)));

		self.inimigos.append(Goodog(walk_frames,death_frames,True,[3000,520],(4200,2900)));

		self.inimigos.append(Goodog(walk_frames,death_frames,False,[3600,520],(4200,3000)));
		self.inimigos.append(Goodog(walk_frames,death_frames,False,[4200,520],(5000,3600)));
		
		self.inimigos.append(Goodog(walk_frames,death_frames,True,[2500,520],(3200,2400)));
		self.inimigos.append(Goodog(walk_frames,death_frames,False,[2900,520],(3000,2300)));
		
		self.pit_image = load_scaled_image("Assets/Outros/alpha_black.png",(self.offset[0]*0.43,self.offset[1]*0.34));


		tiles = [];
		for i in range (0,41):
			tiles.append(load_scaled_image("Assets/Tileset/"+str(i)+".png",self.offset));


		self.background = [];
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada4.png",self.offset),[-1600,220],4,1015,0.05));
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada3.png",self.offset),[-900,210],4,1015,0.1));
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada2.png",self.offset),[-1000,200],4,1015,0.15));
		self.background.append(Smart_Background(load_scaled_image("Assets/Cenario/camada1.png",self.offset),[-1010,230],4,1015,0.2));
		

		self.village_image = load_scaled_image("Assets/Cenario/vilarejo.png",self.offset);
		self.village_position = (5200,-100);

		flower_images = [pg.transform.scale(load_scaled_image("Assets/Cenario/arvore1.png",self.offset),(425,591)),
			pg.transform.scale(load_scaled_image("Assets/Cenario/arvore2.png",self.offset),(523,569)),
			pg.transform.scale(load_scaled_image("Assets/Cenario/arvore3.png",self.offset),(539,636)),
			pg.transform.scale(load_scaled_image("Assets/Cenario/arvore4.png",self.offset),(425,591)),
			pg.transform.scale(load_scaled_image("Assets/Cenario/arbusto1.png",self.offset),(293,112)),
			pg.transform.scale(load_scaled_image("Assets/Cenario/arbusto2.png",self.offset),(222,155)),
			pg.transform.scale(load_scaled_image("Assets/Cenario/arbusto3.png",self.offset),(247,119))];

		self.bg_elements = [Bg_Element(420,32,flower_images[0]),Bg_Element(1100,52,flower_images[1]),
		Bg_Element(4000,32,flower_images[0]),Bg_Element(4100,-12,flower_images[2]),
		Bg_Element(3600,52,flower_images[1]),Bg_Element(3900,32,flower_images[3]),
		Bg_Element(4200,50,flower_images[1]),Bg_Element(4420,32,flower_images[0]),
		Bg_Element(1700,520,flower_images[4]),Bg_Element(2200,475,flower_images[5]),
		Bg_Element(2600,475,flower_images[5]),Bg_Element(100,510,flower_images[6]),
		Bg_Element(3000,510,flower_images[6]),Bg_Element(2000,510,flower_images[6]),
		Bg_Element(2400,520,flower_images[4])];


		#GAME PLAY STUFF
		self.camera = [0,0,1366,768];
		self.world_end = [-4900,7000];
		self.walking_areas = []; 

		self.walking_areas.append(Ramp_45(5030,470,tiles,1,self.offset));
		self.walking_areas.append(Ramp_45(4730,470,tiles,0,self.offset));
		#self.walking_areas.append(Ramp_45(400,470,tiles,0,self.offset));
		#self.walking_areas.append(Ramp_45(400,470,tiles,0,self.offset));


		self.walking_areas.append(Single_Tile(4880,470,3,tiles,self.offset));

		self.walking_areas.append(Plain_Ground(20,620,900,600,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1040,620,9600,600,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1520,320,300,160,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(1950,180,900,160,tiles,self.offset));
		self.walking_areas.append(Plain_Ground(-1900,620,1650,300,tiles,self.offset));
		self.walking_areas.append(Single_Tile(-250,620,1,tiles,self.offset));





		self.mouse_position = [];
		self.hit = False;


		self.pressing_c = False;
		self.curr_c = 0;



		self.secret_combo = KeyCombo("UUDDLRLRBA");
		self.next_state = False;

	def update(self,delta,key):
		self.player.update(delta,key,self.camera,self.walking_areas);
				
		if(self.pressing_c and key[K_c] == False):
			self.pressing_c = False;
		if(key[K_c] and self.pressing_c == False):
			self.pressing_c = True;
			self.curr_c += 1;	
			self.player.curr_c = self.curr_c;
			if(self.curr_c > 2):
				self.curr_c = 0;
			for i in range(0,5):
				self.player.animations[i].change_sprites(self.sprites[self.curr_c][i]);
				if(self.player.current_action == 4 and self.player.animations[4].curr_frame>15):
					self.player.change_animation(0);

		self.mouse_position = [pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]];
		
		
		#PLAYER GROUND COLLISIONS
		

		#INIMIGOS
		for inimigo in self.inimigos:
			inimigo.update(delta,self.camera,self.player);

		for item in self.itens:
			item.update(delta,self.player,self.camera);

		for e in self.bg_elements:
			e.update(delta,self.player,self.camera);

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

		if(self.camera[0] > self.world_end[1]):
			self.camera[0] = self.world_end[1];

		for bg in self.background:
			bg.update(delta,self.camera);

		# OFF WORLD LIMITS PLAYER
		if(self.player.get_rect()[1] > self.camera[1]+self.camera[3] + 300):
			self.player.speed[1] = 0;
			if(self.player.current_action != 3):
				self.player.change_animation(3)
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
		display.fill((170,250,250));

		for bg in self.background:
			bg.draw(display,self.camera,self.offset);

		if(self.camera[0] > 3600):
			display.blit(self.village_image,((self.village_position[0]-self.camera[0])*self.offset[0],(self.village_position[1]-self.camera[1])*self.offset[1]));


		for e in self.bg_elements:
			e.draw(display,self.camera,self.offset);

		for rect in self.walking_areas:
			rect.draw(display,self.camera,self.offset);

		for item in self.itens:
			item.draw(display,self.camera,self.offset);

		for inimigo in self.inimigos:
			inimigo.draw(display,self.camera,self.offset);

		if(self.show_secret_image):
			display.blit(pg.transform.scale(self.secret_image,(300,300)),((-2000-self.camera[0])*self.offset[0],(200-self.camera[1])*self.offset[1]));
			display.blit(self.fonte.render("Emma Watson > Emma Stone",False,(0,0,0)),((-2000-self.camera[0])*self.offset[0],(120-self.camera[1])*self.offset[0]));
		
		self.player.draw(display,self.camera,self.offset);

		display.blit(self.fonte.render("Coins: "+str(self.player.cash),False,(0,0,0)),(0,0));
		
		if(self.curr_c == 0):
			display.blit(self.sprites[2][1][8],(1060*self.offset[0],15*self.offset[1]));
			display.blit(self.sprites[1][1][8],(1090*self.offset[0],15*self.offset[1]));
			display.blit(self.sprites[0][1][8],(1150*self.offset[0],20*self.offset[1]));
		if(self.curr_c == 1):
			display.blit(self.sprites[0][1][8],(1050*self.offset[0],20*self.offset[1]));
			display.blit(self.sprites[2][1][8],(1110*self.offset[0],15*self.offset[1]));
			display.blit(self.sprites[1][1][8],(1140*self.offset[0],15*self.offset[1]));
		if(self.curr_c == 2):
			display.blit(self.sprites[1][1][8],(1060*self.offset[0],15*self.offset[1]));
			display.blit(self.sprites[0][1][8],(1105*self.offset[0],20*self.offset[1]));
			display.blit(self.sprites[2][1][8],(1160*self.offset[0],15*self.offset[1]));

		#display.blit(self.pit_image,(820-self.camera[0],560-self.camera[1]));