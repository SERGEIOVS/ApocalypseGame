import pygame as pg
islands_list = []
islands_filename ='txt/coords/islands/islands.txt'
islands_filemode = 'r'
islands_file = open (islands_filename , islands_filemode)
islands_file1 = islands_file.readlines()

Island_images = [ pg.image.load( 'задний фон/локации/island4.png' ) , pg.image.load( 'задний фон/локации/island5.png')]

class Background :
    def __init__(self , x , y , image) :
        self.x = x
        self.y = y
        self.image = image

for i in range( len ( islands_file1) ) :
    i =Background( islands_file1[i].split(',')[0] , islands_file1[i].split(',')[1] ,Island_images[i] )
    islands_list.append( i )