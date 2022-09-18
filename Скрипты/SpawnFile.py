from MapController import *
from UnitManager import *
from Items import*
from traps import *

big_font = pg.font.Font( None , Fontsizes[0])

small_font = pg.font.Font( None , Fontsizes[1] )

show_health = big_font.render( str( hero_health )  + "/" + str( hero_max_health ) , False , ( 255 , 0 , 0 ) )

show_hero_armor = big_font.render( str( hero_armor ) + "/" +  str( hero_max_armor ) , False , ( 250 , 0, 0 ) )

current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_ammo ) , False , ( 250 , 0 , 0 ) )

show_time = big_font.render( ' Время : ' + str( d1.hour ) + " : " + str( d1.minute ) + " : " + str( d1.second ) , False , ( 250 , 0 , 0 ) )



