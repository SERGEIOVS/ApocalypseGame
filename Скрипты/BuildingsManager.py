import pygame as pg

class Buildings :
    def __init__( self , x , y , image , width , height ) :
        self.x = x
        self.y = y    
        self.image = image
        self.width = width
        self.height = height

buildings_list = []

x_buildings_filename ='txt/coords/buildings/x_buildings.txt'
y_buildings_filename ='txt/coords/buildings/y_buildings.txt'

buildings_x_filemode = 'r'
buildings_y_filemode = 'r'

buildings_x_file = open (x_buildings_filename , buildings_x_filemode)
buildings_y_file = open (y_buildings_filename , buildings_y_filemode)

buildings_x_file1 = buildings_x_file.readlines()
buildings_y_file1 = buildings_y_file.readlines()

buildings_images_list = [

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) , 

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) ,

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) ,

pg.image.load( 'постройки/база/база.png' ) ,

pg.image.load( 'постройки/дом пришельцев/дом пришельцев.png' ) ,

pg.image.load( 'постройки/полицейский участок/полицейский участок.png' ) ,

pg.image.load( 'задний фон/bridge_road.png' ) , 

pg.image.load( 'постройки/парковки/парковка.png' ) ,

pg.image.load( 'декорации/фонарные столбы/фонарный столб.png' ) ,

pg.image.load( 'задний фон/cave.png' ) ,


pg.image.load( 'задний фон/lake.png' ) ,

pg.image.load( 'постройки/палатка/открытая_палатка.png' ) ,

pg.image.load( 'задний фон/rails.png' ) ,

pg.image.load( 'декорации/Могилы/могила.png' ) , 

pg.image.load( 'декорации/деревья/tree.png' ) ,

pg.image.load( 'декорации/capsules/Test_unit-Dogman.png' ) ,

pg.image.load( 'декорации/capsules/Test_unit-mutant1.png' ) ,

pg.image.load( 'задний фон/vertical_cave_hole.png' ) ,

pg.image.load( 'задний фон/vertical_cave_stairs.png' ) ,

pg.image.load( 'задний фон/vertical_cave_stairs+big_stone.png' ) ,


pg.image.load( 'задний фон/длинные острые камни.png' ) ,

pg.image.load( 'мебель/диван.png' ) ,

pg.image.load( 'мебель/шкаф.png' ) , 

pg.image.load( 'мебель/холодильник.png' ) , 

pg.image.load( 'мебель/электроплита.png' ) , 

pg.image.load( 'мебель/лампа.png' ) ,

pg.image.load( 'мебель/стол и шкафчики.png' ) , 

pg.image.load( 'мебель/стол.png ' ) , 

pg.image.load( 'мебель/шкаф с полкой.png' ) , 

pg.image.load( 'декорации/помойки/помойка.png' ) , 


pg.image.load( 'декорации/помойки/горящая_помойка.png' ) ,

pg.image.load( 'мебель/стиральная машина.png' ) 

]

for i in range( len ( buildings_x_file1 ) ) :
    i = Buildings( buildings_x_file1,buildings_y_file1 , buildings_images_list[ i ] , 5 , 5 )
    buildings_list.append( i )

"""class Furniture :
    def __init__( self , x , y , image , width , height ) :
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height

furniture= []"""