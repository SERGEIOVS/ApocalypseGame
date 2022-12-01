import pygame as pg
class Traps:
    def __init__( self , x , y , image , width , height ) :
        self.x = x
        self.y = y
        self.image= image
        self.width = width
        self.height = height

traps = []

traps_x_filename ='txt/coords/traps/traps_x_file.txt'

traps_x_filemode = 'r'

traps_x_file = open (traps_x_filename , traps_x_filemode)

traps_x_file1 = traps_x_file.readlines()


traps_y_filename ='txt/coords/traps/traps_y_file.txt'

traps_y_filemode = 'r'

traps_y_file = open (traps_y_filename , traps_y_filemode)

traps_y_file1 = traps_y_file.readlines()

traps_images_list = [

pg.image.load( 'ловушки/шипы/шипы.png' ),
pg.image.load( 'ловушки/шипы/шипы.png' )

]

for i in range( len ( traps_x_file1 ) ) :
    i = Traps( traps_x_file1[ i ] , traps_y_file1[ i ] ,traps_images_list[i]  , 5 , 5 )
    traps.append(i)