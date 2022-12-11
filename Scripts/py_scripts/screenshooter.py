import pyautogui , datetime , time ; from log_manager import * ; from logging import *

minutes = []

for i in  range(60):
    i += 1
    minutes.append(i)

start = True

while start:

            d1 = datetime.datetime.today()
            d1 += datetime.timedelta(hours = 0)

            time_units = [d1.hour , d1.minute , d1.second]
            current_time_unit = time_units[1]

            print('Welcome!')
            print()
            print('MENU')
            print()
            print('1 - Make screenshot/s without interval')
            print()
            print('2 - Make screenshot/s with interval')
            print()

            screenshots_num = int(input('screenshots ? (number)  : '))

            for i in range(screenshots_num):

                print()

                x1 , y1 = int(input('x1 : ')) , int(input('y1 : '))
                
                x2 , y2 = int(input('x2 : ')) , int(input('y2 : '))

                print()


                #making a screenshot without name
                screenshot = pyautogui.screenshot()


                #making a screenshot name , path and format

                print()

                screenshot_name = input('name : ')

                print()

                screenshot_path = input('path : ')

                print()

                screenshot_format = input('format : ')

                print()

                #saving the  screnshot/s
                screenshot.save(str(screenshot_path) + str(screenshot_name) + str(screenshot_format) )

            #for i in minutes:
            #if current_time_unit == i:
                    #time.sleep(d1.second)
                    #screenshot = pyautogui.screenshot(str(screenshot_path)  + '_' + str(screenshot_name) + '_' + str(screenshot_format) , region = (x1 , y2, x2 , y2))