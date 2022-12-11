import pygame as pg

class Buildings :
    def __init__( self , x , y , image ) :
        self.x = x
        self.y = y    
        self.image = image

buildings_list = []
buildings_filename ='txt/coords/buildings/buildings.txt'
buildings_filemode = 'r'
buildings_file = open (buildings_filename , buildings_filemode)
buildings_file1 = buildings_file.readlines()

buildings_images_list = [

pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) , 
pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) ,
pg.image.load( 'постройки/кирпичный дом/bedroom.png' ) ,
pg.image.load( 'постройки/база/база.png' ) ,
pg.image.load( 'постройки/дом пришельцев/дом пришельцев.png' ) ,
pg.image.load( 'постройки/полицейский участок/полицейский участок.png' ) ,
pg.image.load( 'задний фон/bridge_road.png' )
]

for i in range( len ( buildings_file1 ) ) :
    i =Buildings( buildings_file1[i].split(',')[0] , buildings_file1[i].split(',')[1] ,buildings_images_list[i] )

    #i = Buildings( buildings_x_file1,buildings_x_file1 , buildings_images_list[ i ] , 5 , 5 )
    buildings_list.append( i )

#pg.image.load( 'постройки/парковки/парковка.png' ) ,
#pg.image.load( 'декорации/фонарные столбы/фонарный столб.png' ) ,
#pg.image.load( 'задний фон/cave.png' ) ,
#pg.image.load( 'задний фон/lake.png' ) ,
#pg.image.load( 'постройки/палатка/открытая_палатка.png' ) ,
#pg.image.load( 'задний фон/rails.png' ) ,
#pg.image.load( 'декорации/Могилы/могила.png' ) , 
#pg.image.load( 'декорации/деревья/tree.png' ) ,
#pg.image.load( 'декорации/capsules/Test_unit-Dogman.png' ) ,
#pg.image.load( 'декорации/capsules/Test_unit-mutant1.png' ) ,
#pg.image.load( 'задний фон/vertical_cave_hole.png' ) ,
#pg.image.load( 'задний фон/vertical_cave_stairs.png' ) ,
#pg.image.load( 'задний фон/vertical_cave_stairs+big_stone.png' ),
#pg.image.load( 'задний фон/длинные острые камни.png' ) ,
#pg.image.load( 'мебель/диван.png' ) ,
#pg.image.load( 'мебель/шкаф.png' ) , 
#pg.image.load( 'мебель/холодильник.png' ) , 
#pg.image.load( 'мебель/электроплита.png' ) , 
#pg.image.load( 'мебель/лампа.png' ) ,
#pg.image.load( 'мебель/стол и шкафчики.png' ) , 
#pg.image.load( 'мебель/стол.png ' ) , 
#pg.image.load( 'мебель/шкаф с полкой.png' ) , 
#pg.image.load( 'декорации/помойки/помойка.png' ) , 
#pg.image.load( 'декорации/помойки/горящая_помойка.png' ) ,
#pg.image.load( 'мебель/стиральная машина.png' ) 
"""class Furniture :
    def __init__( self , x , y , image , width , height ) :
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height

furniture= []"""