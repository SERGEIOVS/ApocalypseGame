import pygame as pg

class Items:
    def __init__( self , x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image= image

items_list = []

x_items_filename ='txt/coords/items/x_items.txt'

y_items_filename ='txt/coords/items/y_items.txt'

itemsfilemode = 'r'

items_x_file = open (x_items_filename , itemsfilemode)

items_y_file = open (y_items_filename , itemsfilemode)

items_x_file1 = items_x_file.readlines()

items_y_file1 = items_y_file.readlines()

items_images_list = [

pg.image.load( 'предметы/оружие/патроны/pistol_ammo.png' ) ,

pg.image.load( 'предметы/оружие/патроны/rifle_ammo.png' ) ,

pg.image.load( 'предметы/инструменты/ящики для инструментов/ящик для инструментов.png' ) ,

pg.image.load( 'предметы/аккумуляторы/аккумулятор_авто.png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) ,

pg.image.load( 'еда/консервы/консервы(рыба).png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) ,

pg.image.load( 'еда/сухпай_походный.png' ) ,

pg.image.load( 'напитки/бутылка_воды.png' ) ,

pg.image.load( 'предметы/фонарики/flashlight_turned_right.png' ) ,


pg.image.load( 'предметы/инструменты/топор/axe_turned_right.png' ) ,

pg.image.load( 'предметы/оружие/sniper_rifle.png' ) ,

pg.image.load( 'предметы/оружие/пулемет.png' ),

pg.image.load( 'предметы/оружие/патроны/pistol_ammo.png' ) ,

pg.image.load( 'предметы/оружие/патроны/rifle_ammo.png' ) ,

pg.image.load( 'предметы/инструменты/ящики для инструментов/ящик для инструментов.png' ) ,

pg.image.load( 'предметы/аккумуляторы/аккумулятор_авто.png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) ,

pg.image.load( 'еда/консервы/консервы(рыба).png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) ,


pg.image.load( 'еда/сухпай_походный.png' ) ,

pg.image.load( 'напитки/бутылка_воды.png' ) ,

pg.image.load( 'предметы/фонарики/flashlight_turned_right.png' ) ,

pg.image.load( 'предметы/инструменты/топор/axe_turned_right.png' ) ,

pg.image.load( 'предметы/оружие/sniper_rifle.png' ) ,

pg.image.load( 'предметы/оружие/пулемет.png' )

]

for i in range( len ( items_x_file1 ) ) :
    i = Items( items_x_file1[ i ] , items_y_file1[ i ] , 5 , 5 , items_images_list[ i ] ) 
    items_list.append( i )