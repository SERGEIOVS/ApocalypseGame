#system/python modules
from re import M
from tkinter import RADIOBUTTON
import pygame as pg , datetime , time , random , math , sys , pyautogui , pickle ; from PIL import Image ; import os ; import logging ; from cv2 import log

#my custom  files
from settings import * ; from MapController import * ; from BuildingsManager import * ; from UnitManager import * ; from Items import * ; from traps import * ;
from SpawnFile import *  ; from VihiclesManager import * ; from PathManager import * ; from musicManager import * ;


pg.init()
pg.font.init()
pos = pg.mouse.get_pos()

game_states_list = [ 'main_menu' , 'play' , 'screenshots_menu' , 'achievements_menu' , 'mini_map' , 'saving' , 'loading' ]

bg_images = [

pg.image.load( 'wallpapers/wallpaper_1.png' ) , pg.image.load( 'wallpapers/wallpaper_2.png' ) ,

pg.image.load( 'wallpapers/wallpaper_3.png' )

]

map_width , map_height = 30_000 , 30_000
map_scale = 1
map_size = 3
show_map = 0
show_units = 0
show_buildings = 1
show_items = 1
show_interface = 1
open_backpack = 1
game_state = game_states_list[0]
bg_num = 2
wallpapers_dir = os.listdir('wallpapers/')
wallpaper = wallpapers_dir[bg_num]

show_hero_stats = 1

mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

def make_screenshot() :
    screenshot = pyautogui.screenshot()
    screenshot.save( 'скриншоты/screenshot' + '.png' )

def start():
    if game_state == 'main_menu':
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )

        screen.blit( button.image , ( int(screen_width) / 2  , 50 ) )
        screen.blit( button.image , ( int(screen_width) / 2  , 100 ) )
        screen.blit( button.image , ( int(screen_width) / 2  , 150 ) )
        screen.blit( button.image , ( int(screen_width) / 2  , 200 ) )
        screen.blit( button.image , ( int(screen_width) / 2  , 250 ) )

    if game_state == 'play':
        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )

        for i in range( len ( islands_file1 ) ) :
            screen.blit( Island_images[ i ] , ( -camera.rect[ 0 ] + int(islands_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(islands_file1[i].split(',')[1] ) ) )

        for i in range( len ( vihicles_x_file1 ) ) :
            screen.blit( vihicles_images_list[ i ] , ( -camera.rect[ 0 ] + int(vihicles_x_file1[ i ]) , -camera.rect[ 1 ] + int(vihicles_y_file1[ i ]) ) ) 

        for i in range( len ( buildings_x_file1 ) ) :
            screen.blit( buildings_images_list[ i ] , ( -camera.rect[ 0 ] + int(buildings_x_file1[ i ]) , -camera.rect[ 1 ] + int(buildings_y_file1[ i ] ) ))

        for i in range(len(items_x_file1 ) ) :
            screen.blit(items_images_list[ i ] , ( -camera.rect[ 0 ] + int(items_x_file1[ i ]) , -camera.rect[ 1 ] + int(items_y_file1[ i ] ) ) ) 

        for i in range( len ( traps_x_file1 ) ) :
            screen.blit( traps_images_list[i] , ( -camera.rect[ 0 ] + int(traps_x_file1[ i ] ) , -camera.rect[ 1 ] + int(traps_x_file1[ i ] )  ) )  


        if open_backpack == 1:
            for i in range( len ( hero_belt_inventory_cells_x_list ) ) : 
                screen.blit ( hero_belt_inventory_cells_images[ i ] , ( hero_belt_inventory_cells_x_list[ i ] ,  hero_belt_inventory_cells_y_list[ i ] ) )

            for i in range( len ( hero_belt_inventory_items_x_list ) ) :
                screen.blit ( hero_belt_inventory_images[ i ] , ( hero_belt_inventory_items_x_list[ i ] ,  hero_belt_inventory_items_y_list[ i ] ) )

            for i in range( len ( hero_backpack_inventory_cells_x_list ) ) :
                screen.blit ( hero_backpack_inventory_cells_images[ i ] , ( hero_backpack_inventory_cells_x_list[ i ] ,  hero_backpack_inventory_cells_y_list[ i ] ) )

            for i in range( len( hero_backpack_inventory_items_x_list ) ) :
                screen.blit ( hero_backpack_inventory_images[ i ] , ( hero_backpack_inventory_items_x_list[ i ] ,  hero_backpack_inventory_items_y_list[ i ] ) )

        if show_interface == 1:
                for i in Icons_list:
                    if show_hero_stats == 1:
                        screen.blit( i.image , ( i.x , i.y ) )
                    
        screen.blit( hero_image , ( hero_x , hero_y ) )

        if show_map == 1:
            mini_map_surf.fill((minimapBGcolor))

            mini_map_surf.blit(cancel_icon.image , ( int(screen_width) / 3 - 25 , 0 ) )
            
            for i in range( len ( items_x_file1 ) ) :
                if show_items == 1:
                    pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_x_file1[ i ]) / (100 * map_scale) , int(items_y_file1[ i ]) / (100 * map_scale) , 1 , 1 ))

            for i in range( len ( buildings_x_file1 ) ) :
                if show_buildings == 1:
                    pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_x_file1[ i ]) / (100 * map_scale) , int(buildings_y_file1[ i ]) / (100 * map_scale) ,  5 , 5  ))

            pg.draw.circle(mini_map_surf , ( 255 , 0 , 0 ) , (100   , 100 ) , 4 , 2)
            pg.draw.circle(mini_map_surf , ( 0 , 255 , 0 ) , (114  , 30  ) , 4 , 1)

            hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , (camera.rect[0] / (100 * map_scale) , camera.rect[1] / (100 * map_scale)) , 1)

            pg.draw.rect(mini_map_surf , ( 255 , 0 , 0 ) , (0 , 0 , int(screen_width) / 3 , int(screen_height) / 3  ) , 1)
            
            screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )
        
herojump , herojumpcounter = False , 10 # запрет на прыжок , высота прыжка

run = True

logging.info( msg = 'GAME STARTED!' )

while run :

    vector = [ 0 , 0 ]
    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION :
            pos = pg.mouse.get_pos()

            if game_state == 'play':
                mouse_visible = TRUE
                cursor_icon.image = pg.image.load( 'интерфейс/иконки/crosshair.png' ) 
                screen.blit( cursor_icon.image , ( pos[ 0 ] , pos[ 1 ] ) )
            
            if game_state == 'main_menu':
                cursor_icon.image = pg.image.load( 'интерфейс/иконки/курсор/press_icon.png' ) 
                mouse_visible = TRUE
                screen.blit( cursor_icon.image , ( pos[ 0 ] , pos[ 1 ] ) )

            if  pos[ 0 ] >= hero_x and game_state == 'play':
                hero_status = 'stay' ; hero_turn = 'right'
                hero_image = pg.image.load( hero)
                heroimage = Image.open(hero)
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
            
            if  pos[ 0 ] <= hero_x  and game_state == 'play':
                hero_status = 'stay' ; hero_turn = 'left'
                hero_image = pg.image.load( hero )
                heroimage = Image.open(hero)
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

            pg.display.update()
            pressed = pg.mouse.get_pressed()
            pos = pg.mouse.get_pos()
        
        if event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1 and int(current_ammo) > 0 and game_state == 'play' and pos[0] >= int(screen_width) / 2:
                current_ammo-=1 ; gun_shot = pg.mixer.Sound( 'Звуки/pistol_shot.wav' ) ; gun_shot.play()
                show_health = big_font.render( str( hero_health )  + "/" + str( hero_max_health ) , False , colors[2] )
                show_hero_armor = big_font.render( str( hero_armor ) + "/" +  str( hero_max_armor ) , False , colors[2] )
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_ammo ) , False , colors[2] )
                hero_status = 'attack' ; hero_turn = 'right'
                #hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + '_0_0_0_0_' + str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
                hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + '_' + str(hero_head)  + '_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
                hero_image =  pg.image.load( 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + '_' + str(hero_head)  +'_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png' )
                heroimage = Image.open('персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + str(hero_head)  +'_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
            
            if event.button == 1 and int(current_ammo) > 0 and game_state == 'play' and pos[0] <= int(screen_width) / 2:
                current_ammo-=1 ; gun_shot = pg.mixer.Sound( 'Звуки/pistol_shot.wav' ) ; gun_shot.play()
                show_health = big_font.render( str( hero_health )  + "/" + str( hero_max_health ) , False , colors[2] )
                show_hero_armor = big_font.render( str( hero_armor ) + "/" +  str( hero_max_armor ) , False , colors[2] )
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_ammo ) , False , colors[2] )
                hero_status = 'attack' ; hero_turn = 'left'
                #hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + '_0_0_0_0_' + str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
                hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + str(hero_head)  +'_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
                hero_image =  pg.image.load('персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' +'_' + str(hero_head)  +'_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png' )
                heroimage = Image.open('персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' +'_' + str(hero_head)  +'_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png')
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

            if event.button == 1 and int(current_ammo) <= 0 and game_state == 'play':
                current_ammo = 0 ; current_ammo_counter = big_font.render( str( current_ammo ) + '/' + str( max_ammo ) , False , colors[2] ) 
                no_ammo = pg.mixer.Sound( 'Звуки/no_ammo.wav' )
                no_ammo.play()

        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()

    if keys[pg.K_a] and game_state == 'play' and camera.rect[0] >= 0:
        hero_status = 'run'
        hero_turn = 'left'
        #hero = 'персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + '_0_0_0_0_' + str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png'
        hero = hero
        vector[ 0 ] -= hero_speed
        hero_image =  pg.image.load( hero )
        heroimage = Image.open(hero)
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

    if keys[pg.K_a] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[0] >= 0 :
        hero_status = 'run'
        hero_turn = 'left'
        
        vector[ 0 ] -= hero_speed
        hero_image =  pg.image.load( hero )
        heroimage = Image.open(hero)
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

    if keys[pg.K_w] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[1] >= 0:
        vector[ 1 ] -= hero_speed
        hero_image =  pg.image.load( hero )
        heroimage = Image.open( hero )
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

    if keys[pg.K_s] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[1] >= 0 :
        vector[ 1 ] += hero_speed
        hero_image =  pg.image.load( hero )
        heroimage = Image.open(hero)
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

    if keys[pg.K_d] and game_state == 'play' and camera.rect[0] <= 12_000:
        hero_status = 'run'
        hero_turn = 'right'
        hero = hero
        vector[ 0 ] += hero_speed
        hero_image =  pg.image.load( hero )
        heroimage = Image.open(hero)
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

    if keys[pg.K_d] and keys[pg.K_LSHIFT] and game_state == 'play' and camera.rect[0] <= 12_000 :
        hero_status = 'run'
        hero_turn = 'right'
        vector[ 0 ] += hero_speed
        hero = hero
        hero_image =  pg.image.load( hero )
        heroimage = Image.open(hero)
        hero_x , hero_y = int(screen_width) / 2  - heroimage.width /2 , int(screen_height)  / 2 - heroimage.height / 2

    if not( herojump ) :
        if keys[pg.K_w] and game_state == 'play' and camera.rect[1] >= 0:
            vector[ 1 ] -= hero_speed
            hero_image =  pg.image.load( hero )
            heroimage = Image.open(hero)
            hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
  

        if keys[pg.K_s] and game_state == 'play' and camera.rect[1] >= 0:
            vector[ 1 ] += hero_speed
            #heroimage = Image.open('персонажи/герой/'+ str(hero_gender) + '/' + 'hero_' + 'no' + '_' + str(hero_head)  + '_' + str(hero_body) + '_' + str(hero_legs) + '_' + str(hero_boots) +'_' +  str(herolefthand) + '_' + str(herorighthand) + '_' + str(hero_status) + '_' + str(hero_turn) + '_' + str(hero_animation) + '.png')
            hero_image =  pg.image.load( hero )
            heroimage = Image.open(hero)
            hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

        if keys[pg.K_SPACE] and game_state == 'play':
            herojump = True #можно прыгать


        ##  Если игрок ходил
        if vector != [ 0 , 0 ] and game_state == 'play':
            camera.move( vector )

    else:
        if herojumpcounter >= -10 :

            if herojumpcounter < 0 :
                hero_y += ( herojumpcounter ** 2 ) / 2

            else:
                hero_y-= ( herojumpcounter ** 2 ) / 2
            herojumpcounter -= 1

        else:
            herojump = False
            herojumpcounter = 10

    if keys [pg.K_r]and game_state == 'play':
        hero_status = 'reload'
        if hero_status =='reload':
            reloadsound = pg.mixer.Sound( 'Звуки/reload.wav' ) ; reloadsound.play()
            current_ammo = 10 ; current_ammo_counter = big_font.render( str( current_ammo ) + '/' + str( max_ammo ) , False , colors[2] )

    if keys [pg.K_F5] :
        make_screenshot() ; logging.info( msg = 'SCREENSHOT SAVED!')

    if keys [pg.K_F12] :
        camerafilemode = 'w'
        camera_file = open (screenfilename , camerafilemode)
        camera_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  )
        camera_file.close()
        logging.info(msg = 'GAME SAVED!' ) ; pg.quit() ; logging.info(msg = 'QUIT GAME!' )
    
    if keys [pg.K_F9] :
        screenfilemode = 'w' ; screenfile = open (screenfilename , screenfilemode)
        screenfile.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  )
        camera_file.close() ; logging.info(msg = 'GAME SAVED!' )

    if keys [pg.K_p] :
        game_state = 'play'

    if keys [pg.K_b] :
        open_backpack = 1

    if keys [pg.K_b]  and keys[pg.K_LSHIFT] :
        open_backpack = 0
    
    if keys [pg.K_ESCAPE] :
        bg_images[ random.randint( 0 , len(bg_images) - 1 ) ]
        game_state = 'main_menu'

    if keys [pg.K_UP] :
        show_map = 1
    
    if keys [pg.K_DOWN] :
        show_map = 0

    if keys [pg.K_KP_7] :
        minimap_location = 'left_up'
        if minimap_location == 'left_up':
            minimap_x = 0
            minimap_y = 0
        
    if keys [pg.K_KP_9] :
        minimap_location = 'right_up'
        if minimap_location == 'right_up':
            minimap_x = int(screen_width) - int(screen_width) / 3
            minimap_y = 0
    
    if keys [pg.K_KP_3] :
        minimap_location = 'right_down'
        if minimap_location == 'right_down':
            minimap_x = int(screen_width) - int(screen_width) / 3
            minimap_y = int(screen_height) - int(screen_height) / 3
    
    if keys [pg.K_KP_1] :
        minimap_location = 'left_down'
        if minimap_location == 'left_down':
            minimap_x = 0
            minimap_y = int(screen_height) - int(screen_height) / 3

    if keys [pg.K_KP_PLUS]:
        mini_map_surf.fill((minimapBGcolor))
        map_scale -= 0.1
        mini_map_surf.blit(cancel_icon.image , ( int(screen_width) / 3 - 25 , 0 ) )
            
        for i in range( len ( items_x_file1 ) ) :
            if show_items == 1:
                pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_x_file1[ i ]) / (100 * map_scale) , int(items_y_file1[ i ]) / (100 * map_scale) , 1 , 1 ))

        for i in range( len ( buildings_x_file1 ) ) :
            if show_buildings == 1:
                pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_x_file1[ i ]) / (100 * map_scale) , int(buildings_y_file1[ i ]) / (100 * map_scale) ,  5 , 5  ))

        hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , (camera.rect[0] / (100 * map_scale) , camera.rect[1] / (100 * map_scale)) , 2)
        pg.draw.rect(mini_map_surf , ( 255 , 0 , 0 ) , (0 , 0 , int(screen_width) / 3 , int(screen_height) / 3  ) , 1)


    if keys [pg.K_KP_MINUS]:
        mini_map_surf.fill((minimapBGcolor))
        map_scale += 0.1
        mini_map_surf.blit(cancel_icon.image , ( int(screen_width) / 3 - 25 , 0 ) )
        
        for i in range( len ( items_x_file1 ) ) :
            if show_items == 1:
                pg.draw.rect(mini_map_surf , (0 , 255 , 0) , (int(items_x_file1[ i ]) / (100 * map_scale) , int(items_y_file1[ i ]) / (100 * map_scale) , 1 , 1 ))

        for i in range( len ( buildings_x_file1 ) ) :
            if show_buildings == 1:
                pg.draw.rect(mini_map_surf , colors[4] , (int(buildings_x_file1[ i ]) / (100 * map_scale) , int(buildings_y_file1[ i ]) / (100 * map_scale) ,  5 , 5  ))
        
        hero_marker = pg.draw.circle(mini_map_surf , ( 255 , 100 , 0 ) , (camera.rect[0] / (100 * map_scale) , camera.rect[1] / (100 * map_scale)) , 2)
        
        pg.draw.rect(mini_map_surf , ( 255 , 0 , 0 ) , (0 , 0 , int(screen_width) / 3 , int(screen_height) / 3  ) , int(map_scale))




        

    if keys [pg.K_ESCAPE]  and open_backpack == 1:
        open_backpack  = 0
    
    if keys [pg.K_0] :
        pg.mixer.music.play()

    screen.fill( BGcolor )

    start()

    pg.display.update()

        #game_status = 'main_menu'
        #for i in range( len ( f_creatures_x_file1 ) ) :
        # screen.blit( friendly_creatures_images_list[i] , ( -camera.rect[ 0 ] + int(f_creatures_x_file1[ i ] ) , -camera.rect[ 1 ] + int(f_creatures_y_file1[ i ] ) ) )   

        #for i in range( len ( enemies_x_file1 ) ) :
                #if int(enemies_x_file1[ i ])  >= camera.rect[0]  and int(enemies_x_file1[ i ]) <= camera.rect[0] + int(screen_width)  and \
                #int(enemies_y_file1[ i ])  >= camera.rect[1]  and int(enemies_y_file1[ i ]) <= camera.rect[1] + int(screen_height) :
                    #screen.blit( enemies_images_list[ i ] , ( -camera.rect[ 0 ] + int(enemies_x_file1[ i ]) , -camera.rect[ 1 ] + int(enemies_y_file1[ i ] ) ) )
        
        #for i in range( len ( furniture ) ) :
            #screen.blit( furniture_images_list[ i ] , ( -camera.rect[ 0 ] + furniture_x_list  [ i ]  , -camera.rect[ 1 ] + furniture_y_list[ i ] ) ) 