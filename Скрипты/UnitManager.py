from email.mime import image
import pygame as pg
from settings import *
from Items import *
from PIL import Image
from email.mime import image
import pygame as pg
from settings import *
from Items import *
from PIL import Image

hero_speed = 3
hero_health , hero_max_health = 10 , 10
hero_armor , hero_max_armor = 10 , 10
current_ammo = 10
max_ammo = 30
hero_gender = 'male'
hero_head = 5
hero_body = 1
hero_legs = 0
hero_boots = 0
herolefthand = 'pistol'
herorighthand = '0'
hero_status = 'stay'
hero_turn = 'left'
hero_animation = 1

hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' +'_'+ str(hero_head)  + '_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
# '_0_0_0_0_'


heroimage = Image.open(hero)

hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

hero_image = pg.image.load( hero )


class Units:
    def __init__( self , x , y , category , status , turn , animation , image ) : 
        self.x = x
        self.y = y
        self.category = category
        self.status = status
        self.turn = turn
        self.animation  = animation
        self.image = image
        
        #self.loot = loot
        #self.health = health
        #self.speed = speed
        #self.turn = turn
"""
unitslist = []
units_filename = 'txt/coords/units/units.txt'
unitsfilemode = 'r'
units_file = open (units_filename , unitsfilemode)
units_file1 = units_file.readlines()

units_images_list = [

pg.image.load( 'персонажи/противники/thief_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/thief1_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/mutant1_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/Dogman_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/hazamatunit_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/yeti_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/beast_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/mutantwithblades_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/thiefleader_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_run_right_1.png' ) ,


pg.image.load( 'персонажи/союзники/жители/citizen_1_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_2_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_3_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_4_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_5_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/soldier_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadmanempty_hands_left_1.png' ) ,

pg.image.load( 'персонажи/союзники/рыба/рыба_1.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/MG_man_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien_1_right_1.png' ) ,


pg.image.load( 'персонажи/союзники/нло/alienwithrifle_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadman_left_1.png' )


]

for i in range( len ( units_file1 ) ) :
               #x                             y                              categoty                       status                         turn                           animation               
    i = Units( units_file1[i].split(',')[0] , units_file1[i].split(',')[1] , units_file1[i].split(',')[2] , units_file1[i].split(',')[3] , units_file1[i].split(',')[4] , units_file1[i].split(',')[5] , units_images_list[i] )
    unitslist.append( i )
"""
hero_speed = 3
hero_health , hero_max_health = 10 , 10
hero_armor , hero_max_armor = 10 , 10
current_ammo = 10
max_ammo = 30
hero_gender = 'male'
hero_head = '1'
hero_body = '0'
hero_legs = '0'
hero_boots = '0'
herolefthand = 'pistol'
herorighthand = '0'
hero_status = 'stay'
hero_turn = 'left'
hero_animation = 1

hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' +'_'+ str(hero_head)  + '_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
# '_0_0_0_0_'


heroimage = Image.open(hero)

hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

hero_image = pg.image.load( hero )


class Units:
    def __init__( self , x , y , category , status , turn , animation , image ) : 
        self.x = x
        self.y = y
        self.category = category
        self.status = status
        self.turn = turn
        self.animation  = animation
        self.image = image
        
        #self.loot = loot
        #self.health = health
        #self.speed = speed
        #self.turn = turn
"""
unitslist = []
units_filename = 'txt/coords/units/units.txt'
unitsfilemode = 'r'
units_file = open (units_filename , unitsfilemode)
units_file1 = units_file.readlines()

units_images_list = [

pg.image.load( 'персонажи/противники/thief_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/thief1_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/mutant1_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/Dogman_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/hazamatunit_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/yeti_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/beast_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/mutantwithblades_run_right_1.png' ) ,

pg.image.load( 'персонажи/противники/thiefleader_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_run_right_1.png' ) ,


pg.image.load( 'персонажи/союзники/жители/citizen_1_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_2_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_3_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_4_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_5_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/soldier_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadmanempty_hands_left_1.png' ) ,

pg.image.load( 'персонажи/союзники/рыба/рыба_1.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/MG_man_run_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien_1_right_1.png' ) ,


pg.image.load( 'персонажи/союзники/нло/alienwithrifle_right_1.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadman_left_1.png' )


]

for i in range( len ( units_file1 ) ) :
               #x                             y                              categoty                       status                         turn                           animation               
    i = Units( units_file1[i].split(',')[0] , units_file1[i].split(',')[1] , units_file1[i].split(',')[2] , units_file1[i].split(',')[3] , units_file1[i].split(',')[4] , units_file1[i].split(',')[5] , units_images_list[i] )
    unitslist.append( i )
"""