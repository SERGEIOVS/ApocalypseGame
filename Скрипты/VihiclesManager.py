import pygame as pg

class Vihicles :
    def __init__( self , x , y , width , height , image , speed ) :
        self.x = x
        self.y = y    
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed

vihicles_list = []

x_vihicles_filename ='txt/coords/vihicles/x_vihicles.txt'

y_vihicles_filename ='txt/coords/vihicles/y_vihicles.txt'

vihiclesfilemode = 'r'

vihicles_x_file = open (x_vihicles_filename , vihiclesfilemode)

vihicles_y_file = open (y_vihicles_filename , vihiclesfilemode)

vihicles_x_file1 = vihicles_x_file.readlines()

vihicles_y_file1 = vihicles_y_file.readlines()

for i in range( len ( vihicles_x_file1) ) :

    vihicles_images_list = [

pg.image.load( 'техника/citizen_car.png' ) ,

pg.image.load( 'техника/citizen_car.png' ) ,

pg.image.load( 'техника/citizen_car.png' ) ,

pg.image.load( 'техника/police_car.png' ) ,

pg.image.load( 'техника/citizen_truck.png' ) ,

pg.image.load( 'техника/лодка.png' ) , 

pg.image.load( 'техника/burned_citizen_car.png' ) ,

pg.image.load( 'техника/ufo_ship.png' ) , 

pg.image.load( 'техника/большой корабль.png' ),

pg.image.load( 'техника/tank.png' )



]

for i in range( len ( vihicles_x_file1 ) ) :
    
    i = Vihicles( vihicles_x_file1[ i ] , vihicles_y_file1[ i ] , 5 , 5 , vihicles_images_list[ i ] , 5 )
    vihicles_list.append( i )