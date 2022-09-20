from ast import Pass
from pickle import TRUE
import pygame as pg,datetime

pg.init()
pg.font.init()

d1 = datetime.datetime.today()

d1 += datetime.timedelta( hours = 0 )

time_units = [ d1.hour , d1.minute ]

current_time_unit = time_units[1] 

screenfilename ='txt/screen.txt'
screenfilemode = 'r'
screenfile = open (screenfilename , screenfilemode)
screenfile1 =screenfile.readlines()

for i in screenfile1:
    screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]
    
screen = pg.display.set_mode( (int( screen_width) , int(screen_height ) ) )

colors = [ ( 0 , 0 , 255 ) , ( 0 , 0 , 0 ) , (250 , 0 , 0)  , (255 , 255 , 255) , (45 , 45 , 45 ) ]

BGcolor = colors[0]

minimapBGcolor = colors[0]

screen.fill(BGcolor)

Captions = ['Welcome to the Crystal city!']

pg.display.set_caption(Captions[0] )



class interface :
    def __init__( self, x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

cells_num = 10

radiation_level = 0

max_radiation_level = 100

beltinventorycell = interface( int(screen_width  )/ 2 - cells_num * 50 / 2, int(screen_height  )- 50, 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )

backpackinventorycell = interface( 710 , 300 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )

currentinventorycell = interface( int(screen_width) / 2 -cells_num * 25 , beltinventorycell.y , 50 , 50 , pg.image.load( 'интерфейс/иконки/current_inventory_cell.png' ) )

cursor_icon = interface( 0 , 0 , 10 , 10 , pg.image.load( 'интерфейс/иконки/crosshair.png' ) )

clock_icon = interface( 900 , 0 , 30 , 30 , pg.image.load( 'интерфейс/иконки/clock_icon.png' ) )

achievements_icon = interface( 3000 , 125 , 30 , 30 , pg.image.load( 'интерфейс/иконки/achievements_icon.png' ) )

health_icon = interface( 0 , int(screen_height) - 50 , 25 , 25 , pg.image.load( 'интерфейс/иконки/health_icon.png' ) )

armor_icon = interface( 0 , int(screen_height) - 25 , 25 , 25 , pg.image.load( 'интерфейс/иконки/armor_icon.png' ) )

current_ammo_icon = interface(0 , int(screen_height) - 75 , 34 , 50 , pg.image.load( 'интерфейс/иконки/pistol_ammo_icon.png' ) )

button = interface(2100 , 210 , 200 , 50 , pg.image.load( 'интерфейс/иконки/button.png' ) )

MusicIcon = interface(0 , 100 , 30 , 30 , pg.image.load( 'интерфейс/иконки/MusicIcon.png' ) )
 
craft_icon = interface( 2100 , 125 , 20 , 30 , pg.image.load( 'интерфейс/иконки/craft_icon.png' ) )

energy_icon = interface( 200 , beltinventorycell.y , 11 , 26 , pg.image.load( 'интерфейс/иконки/energy_icon.png' ) )

#left_pointer = interface( achievements_menu.x + 50 , achievements_menu.y + 100 ,20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_left.png' ) )

#right_pointer = interface(achievements_menu.x + 200 , achievements_menu.y + 100 , 20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_right.png' ) )

cancel_icon = interface(0 , 25 , 20 , 20 , pg.image.load( 'интерфейс/иконки/cancel_icon.png' ) )

#cancel_icon1 = interface( achievements_menu.x + achievements_menu.width - 20 , minimap_menu.y + 25 , 20 , 20 , pg.image.load( 'интерфейс/иконки/cancel_icon.png' ) )

minimap_icon = interface( int(screen_width) - 710 , 1030 , 50 , 50 , pg.image.load( 'интерфейс/иконки/minimap_icon.png' ) )

radiation_icon = interface(0 , 1030 , 50 , 50 , pg.image.load( 'интерфейс/иконки/bio_danger_icon_green.png' ) )

Icons_list = [ 

'beltinventorycell.image' , 'backpackinventorycell.image' , 'currentinventorycell.image' , 'achievements_menu.image' , 'minimap_menu.image' , 'cursor_icon.image' , 'clock_icon.image' , 

'achievements_icon.image' , 'health_icon.image' , 'armor_icon.image' , 'current_ammo_icon.image' , 'button.image' , 'MusicIcon.image' , 'craft_icon.image' , 'energy_icon.image' , 'left_pointer.image' ,

'right_pointer.image' , 'cancel_icon.image'  , 'minimap_icon.image'

]

pg.display.set_icon(pg.image.load('интерфейс/иконки/Game_icon.png') )

d1 = datetime.datetime.today()

d1 += datetime.timedelta( hours = 0 )

minimap_location = 'right_up'
minimap_x = 0
minimap_y = 0


if minimap_location == 'left_up':
    minimap_x = 0
    minimap_y = 0

class cam :

    def __init__( self , x , y ) :
        self.rect = pg.Rect( int(camera_x) , int(camera_y) , int(screen_width) / 3 , int(screen_height) / 3 )

    def move( self , vector ) :
        self.rect[ 0 ] += vector[ 0 ]
        self.rect[ 1 ] += vector[ 1 ]

camera = cam( 0 , 0 )
vector = [ 0 , 0 ]

pistolmagazine_capacity = 30
pistolmax_magazine_capacity = 300

hero_belt_inventory_cells = []

hero_belt_inventory_cells_x_list = [

int(screen_width) / 2 -cells_num * 50 / 2 + 10  , int(screen_width) / 2 -cells_num * 50 / 2 + 60  , int(screen_width) / 2 -cells_num * 50 / 2 + 110 ,
int(screen_width)/ 2 -cells_num * 50 / 2 + 160 , int(screen_width) / 2 -cells_num * 50 / 2 + 210 , int(screen_width) / 2 -cells_num * 50 / 2 + 260 , 
int(screen_width) / 2 -cells_num * 50 / 2 + 310 , int(screen_width) / 2 -cells_num * 50 / 2 + 360 , int(screen_width) / 2 -cells_num * 50 / 2 + 410 , 
int(screen_width) / 2 -cells_num * 50 / 2 + 460]

hero_belt_inventory_cells_y_list = []
hero_belt_inventory_cells_images = []

for i in range( len ( hero_belt_inventory_cells_x_list ) ) :
    hero_belt_inventory_cells_y_list.append(int(screen_height) - 50)
    hero_belt_inventory_cells_images.append(pg.image.load( 'интерфейс/иконки/inventory_cell.png' ))
    i = interface( hero_belt_inventory_cells_x_list[ i ] , hero_belt_inventory_cells_y_list[ i ] , 5 , 5 ,hero_belt_inventory_cells_images[ i ] )
    hero_belt_inventory_cells.append( i )

hero_belt_inventory = []

hero_belt_inventory_items_x_list = [

int(screen_width) / 2 -cells_num * 50 / 2 + 20,
int(screen_width) / 2 -cells_num * 50 / 2 + 60,
int(screen_width) / 2 -cells_num * 50 / 2 + 110

]

hero_belt_inventory_items_y_list = []

hero_belt_inventory_images = [
    
pg.image.load( 'предметы/оружие/пистолеты/pistol_turned_right.png' ),
pg.image.load( 'предметы/оружие/пистолеты/pistol_turned_right.png' ),
pg.image.load( 'предметы/оружие/пистолеты/pistol_turned_right.png' ),
pg.image.load( 'предметы/оружие/пистолеты/pistol_turned_right.png' )
]

for i in range( len ( hero_belt_inventory_items_x_list ) ) :
    hero_belt_inventory_items_y_list.append( int(screen_height) - 40 )
    i = interface( hero_belt_inventory_items_x_list[ i ] , hero_belt_inventory_items_y_list[ i ] , 5  , 5 , hero_belt_inventory_images[ i ] )
    hero_belt_inventory.append( i )



hero_backpack_inventory_cells = []

hero_backpack_inventory_cells_x_list = [

int(screen_width) / 2 -cells_num * 50 / 2 + 10  , 

int(screen_width) / 2 -cells_num * 50 / 2 + 110 , 

int(screen_width) / 2 -cells_num * 50 / 2 + 210 , 

int(screen_width) / 2 -cells_num * 50 / 2 + 310 , 

int(screen_width) / 2 -cells_num * 50 / 2 + 410  ]

hero_backpack_inventory_cells_y_list = []

hero_backpack_inventory_cells_images = []

for i in range( len ( hero_backpack_inventory_cells_x_list ) ) :
    hero_backpack_inventory_cells_y_list.append( int(screen_height) / 2 +100 )
    hero_backpack_inventory_cells_images.append( pg.image.load( 'интерфейс/иконки/big_inventory_cell.png' ) )
    i = interface( hero_backpack_inventory_cells_x_list[ i ] , hero_backpack_inventory_cells_y_list[ i ] , 5 , 5 , hero_backpack_inventory_cells_images[ i ] )
    hero_backpack_inventory_cells.append( i )

hero_backpack_inventory = []

hero_backpack_inventory_items_x_list = [

hero_backpack_inventory_cells_x_list[ 0 ] + 20 ,

hero_backpack_inventory_cells_x_list[ 0 ] + 120,

hero_backpack_inventory_cells_x_list[ 0 ] + 220 ,

hero_backpack_inventory_cells_x_list[ 0 ] + 320 ,

hero_backpack_inventory_cells_x_list[ 0 ] + 420
]

hero_backpack_inventory_items_y_list = []

hero_backpack_inventory_images = [

pg.image.load('интерфейс/иконки/cancel_icon.png') ,

pg.image.load( 'предметы/оружие/machete/machete_turned_right.png' ) ,

pg.image.load( 'предметы/инструменты/топор/axe_turned_right.png' ) ,

pg.image.load( 'предметы/зажигалки/газовая_зажигалка.png' ) , 

pg.image.load( 'предметы/фонарики/flashlight_turned_right.png' )

]

for i in range( len ( hero_backpack_inventory_items_x_list ) ) :
    hero_backpack_inventory_items_y_list.append(hero_backpack_inventory_cells_y_list[ 1 ] + 20)
    hero_backpack_inventory.append(hero_backpack_inventory_cells_y_list[ 1 ] + 20)
    
    i = interface( hero_backpack_inventory_items_x_list[ i ] , hero_backpack_inventory_items_y_list[ i ] , 5 , 5 , hero_backpack_inventory_images[ i ] )
    hero_backpack_inventory.append( i )

import pygame as pg

hero_belt_inventory_cells = []

hero_belt_inventory_cells_x_list = [

int(screen_width) / 2 -cells_num * 50 / 2 + 10  , int(screen_width) / 2 -cells_num * 50 / 2 + 60  , int(screen_width) / 2 -cells_num * 50 / 2 + 110 ,
int(screen_width) / 2 -cells_num * 50 / 2 + 160 , int(screen_width) / 2 -cells_num * 50 / 2 + 210 ,int(screen_width) / 2 -cells_num * 50 / 2 + 260 , 
int(screen_width) / 2 -cells_num * 50 / 2 + 310 , int(screen_width) / 2 -cells_num * 50 / 2 + 360 , int(screen_width) / 2 -cells_num * 50 / 2 + 410 , 
int(screen_width) / 2 -cells_num * 50 / 2 + 460]

hero_belt_inventory_cells_y_list = []
hero_belt_inventory_cells_images = []

for i in range( len ( hero_belt_inventory_cells_x_list ) ) :
    hero_belt_inventory_cells_y_list.append(int(screen_height) - 50)
    hero_belt_inventory_cells_images.append(pg.image.load( 'интерфейс/иконки/inventory_cell.png' ))
    i = interface( hero_belt_inventory_cells_x_list[ i ] , hero_belt_inventory_cells_y_list[ i ] , 5 , 5 ,hero_belt_inventory_cells_images[ i ] )
    hero_belt_inventory_cells.append( i )

hero_belt_inventory = []
hero_belt_inventory_items_x_list = [
int(screen_width) / 2 -cells_num * 50 / 2 + 20]
hero_belt_inventory_items_y_list = []
hero_belt_inventory_images = [ pg.image.load( 'предметы/оружие/пистолеты/pistol_turned_right.png' ) ]

for i in range( len ( hero_belt_inventory_items_x_list ) ) :
    hero_belt_inventory_items_y_list.append( int(screen_height) - 40 )
    i = interface( hero_belt_inventory_items_x_list[ i ] , hero_belt_inventory_items_y_list[ i ] , 5  , 5 , hero_belt_inventory_images[ i ] )
    hero_belt_inventory.append( i )