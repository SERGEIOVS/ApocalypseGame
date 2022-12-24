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

pg.image.load( 'Objects\Items/weapons/ammo/pistol_ammo.png' ) ,

pg.image.load( 'Objects/Items/weapons/ammo/rifle_ammo.png' ) ,

pg.image.load( 'Objects/Items/tools/toolboxes/ящик для инструментов.png' ) ,

pg.image.load( 'Objects/Items/аккумуляторы/аккумулятор_авто.png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,

pg.image.load( 'Objects\Items/food/консервы/консервы(рыба).png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,

pg.image.load( 'Objects\Items/food/сухпай_походный.png' ) ,

pg.image.load( 'Objects/Items/drinks/бутылка_воды.png' ) ,

pg.image.load( 'Objects/Items/фонарики/flashlight_turned_right.png' ) ,


pg.image.load( 'Objects/Items/tools/топор/axe_turned_right.png' ) ,

pg.image.load( 'Objects/Items/weapons/sniper_rifle.png' ) ,

pg.image.load( 'Objects/Items/weapons/пулемет.png' ),

pg.image.load( 'Objects/Items/weapons/ammo/pistol_ammo.png' ) ,

pg.image.load( 'Objects/Items/weapons/ammo/rifle_ammo.png' ) ,

pg.image.load( 'Objects/Items/tools/toolboxes/ящик для инструментов.png' ) ,

pg.image.load( 'Objects/Items/аккумуляторы/аккумулятор_авто.png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,

pg.image.load( 'Objects\Items/food/консервы/консервы(рыба).png' ) ,

pg.image.load( 'Objects/Items/lighting/lighters//gas_lighter.png' ) ,


pg.image.load( 'Objects/Items/food/сухпай_походный.png' ) ,

pg.image.load( 'Objects/Items/drinks/бутылка_воды.png' ) ,

pg.image.load( 'Objects/Items/фонарики/flashlight_turned_right.png' ) ,

pg.image.load( 'Objects/Items/tools/топор/axe_turned_right.png' ) ,

pg.image.load( 'Objects/Items/weapons/sniper_rifle.png' ) ,

pg.image.load( 'Objects/Items/weapons/mg/пулемет.png' )

]

for i in range( len ( items_x_file1 ) ) :
    i = Items( items_x_file1[ i ] , items_y_file1[ i ] , 5 , 5 , items_images_list[ i ] ) 
    items_list.append( i )