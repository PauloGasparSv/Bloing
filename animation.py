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
		self.play_once = False;
		self.has_played = False;
	
	def update(self,delta):
		if(self.playing and (self.play_once == True and self.has_played == False or self.play_once == False)):
			self.timer += self.speed * delta;
			if(self.timer > 20000):
				self.timer = 0;
				if (self.curr_frame == self.length -1):
					if(self.play_once == False):
						self.curr_frame = 0; 
					self.has_played = True;
				else:
					self.curr_frame += 1;

	def get_frame(self,inverted):
		return self.frame[self.curr_frame] if inverted == False else pg.transform.flip(self.frame[self.curr_frame],True,False);

	def set_once(self,play_once):
		self.play_once = play_once;

	def get_speed(self):
		return self.speed;
	def set_speed(self,speed):
		self.speed = speed;

	def play(self):
		self.curr_frame = 0;
		self.timer = 0;
		self.playing = True;

	def stop(self):
		self.curr_frame = 0;
		self.timer = 0;
		self.has_played = False;
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