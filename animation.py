import pygame as pg;

class Animation:
	def __init__(self,images,speed,playing):
		self.frame = images;
		self.visible = True;
		self.speed = speed;
		self.curr_frame = 0;
		self.playing = playing;
		self.timer = 0;
		self.length = len(images);
	
	def update(self,delta):
		if(self.playing):
			self.timer += self.speed * delta;
			if(self.timer > 5000):
				self.timer = 0;
				if (self.curr_frame == self.length -1):
					self.curr_frame = 0; 
				else:
					self.curr_frame += 1;

	def get_frame(self,inverted):
		return self.frame[self.curr_frame] if inverted == False else pg.transform.flip(self.frame[self.curr_frame],True,False);


	def play(self):
		self.curr_frame = 0;
		self.timer = 0;
		self.playing = True;

	def stop(self):
		self.curr_frame = 0;
		self.timer = 0;
		self.playing = False;

	def pause(self):
		self.timer = 0;
		self.playing = False;

	def resume(self):
		self.playing = True;

	def hide(self):
		self.visible = False;

	def show(self):
		self.visible = True;

	def isPlaying(self):
		return self.playing;