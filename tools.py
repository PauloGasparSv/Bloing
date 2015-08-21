import pygame as pg;
from pygame.locals import *;

def load_image(path):
	return pg.image.load(path).convert_alpha();
def load_scaled_image(path,offset):
	imagem = pg.image.load(path).convert_alpha();
	return pg.transform.scale(imagem,(int(imagem.get_size()[0]*offset[0]),int(imagem.get_size()[1]*offset[1])));