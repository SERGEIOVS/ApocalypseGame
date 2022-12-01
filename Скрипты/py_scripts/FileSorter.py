import os,shutil,sys

mydir1 = os.listdir('C:\\123456789\\videos\Myfoto1/')

FileTypes=[
[],
[]
]
run = True
while run:

            menupointslist = [
' - Создать  папку / несколько папок' ,
' - Выбрать нужную папку' ,
' - Удалить нужную папку / несколько папок' ,
' - Переименовать нужную папку / несколько папок' ,
' - Создать файл / несколько файлов' ,
' - Показать содержимое  нужной папки' ,
' - Показать содержимое нужного файла']

            print()
            print('----')
            print()
            print( 'МЕНЮ' )
            print()
            print('----')

            for i in range( len( menupointslist ) ) :
                print( i + 1 , menupointslist[i]  )

            print('-------------------------------------------------------------------')
            print()
            action = input('Enter an action : ')
            if action == 'count':
                directory1 = input('Enter a directory old name:')
                filetype1 = input('Enter a file type:')

                print()
            
                for i in range(len(mydir1)):
                        if filetype1 in mydir1[i] and filetype1 == 'Screenshot':
                            i = os.path.basename(mydir1[i])
                            FileTypes[0].append(i)
                            #print(screenshotlist)
                            #print('name = ' , i )

                        print('Elements total : ' , len(mydir1))
                        print(filetype1 , "'s : " , len(FileTypes[0]))

                        if filetype1 in mydir1[i] and filetype1 == 'IMG':
                            i = os.path.basename(mydir1[i])
                            FileTypes[1].append(i)
                            #print(screenshotlist)
                            #print('name = ' , i )

                        print('Elements total : ' , len(mydir1))
                        print(filetype1 , "'s : " , len(FileTypes[1]))

print()
print()

print('----------------------------------------------------------------------------------------------------------')