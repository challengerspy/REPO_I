#import psutil
import os
import sys
import shutil

def diplicate_file(filename):
    if os.path.isfile(filename):
        newfile=filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print('Файл ', newfile, ' был успешно создан')
            return True
        else:
            print('Возникли проблемы копирования')
            return False
def del_duplicats(dirname):
    print('Удаление дубликатов в директории ')
    file_list=os.listdir(dirname)
    double_count=0
    for f in file_list:
        fullname=os.path.join(dirname,f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                double_count+=1
                print('Файл', fullname, 'был успешно удален')
    return double_count

def sys_info():
    print(os.cpu_count())
    print(sys.stdout.encoding)
    print(sys.getfilesystemencoding())
    print(os.getlogin())
    print(os.getcwd())
    print(sys.platform)			
	
print('Привет, junior!')
print('Будем делать?')
answer = input('Y/N ')
while answer!='q':
    if answer=='y':
        print(" ")
        print('1 - Список файлов ')
        print('2 - Вывод данных о системе ')
        print('3 - Удаление дубликатов в директории')
        print('4 - дублирование файлов')
        print('5 - Копирование указанного файла')		
        print('6 - Удаление указанного файла')
        print('7 - Удаление дубликатов')		
        do=int(input('выберите действие '))
        if do == 2:
            sys_info()    
        elif do == 1:
            print(os.listdir())
        elif do == 4: #ОШИБКА НА ДИРЕКТОРИЮ
            file_list=[]
            print('Дублирование в текущей директории= ')
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                #if os.path.isfile(file_list):
                newfile = file_list[i] + '.dupl'
                shutil.copy(file_list[i], newfile)
                i=i+1
               # else:
                #    pass
        elif do==3: # ОШИБКА
            del_list=[]
            print('Удаление дубликатов ')
            del_list=(os.listdir())
            print(del_list)
            y=0
            while y < len(del_list):
                if str(del_list[y]) != str(del_list[y]) + '.dupl':
                    continue
                os.remove(del_list[y])
                print(del_list[y])
                y=y+1
        elif do == 5:
            print('Дублирование указанного файла ')
            filename=input('Укажите имя файла ')
            diplicate_file(filename)
        elif do == 6:
            print('Удаление указанного файла')
            filename=input('Укажите имя файла')
            if os.path.isfile(filename):
                os.remove(filename)
        elif do == 7: # удаление дубликатов в директории
            dirname = input('Введите имя директории ')
            count=del_duplicats(dirname)
            print('-- удалено файлов: ', count)
        elif do == 8:
            pass		
        else:
            pass
    else:
        pass