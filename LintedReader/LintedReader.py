import cv2, sys, os
import pytesseract
from os import path

pytesseract.pytesseract.tesseract_cmd = r'ВСТАВЬТЕ ПУТЬ К tesseract.exe'

array_name_picture=[]

for root, dirs, files in os.walk(str(sys.path[0])):
    for filename in files:
        if path.splitext(filename)[1] =='.png':
            name_files_png=path.splitext(filename)[0]
            array_name_picture.append(name_files_png)
           
if len(array_name_picture) > 1:
    print('было обнаружено несколько фоток. По умолчанию будет выбрана:' + array_name_picture[0]+'.png')
    PictureName=array_name_picture[0] + ".png"
if len(array_name_picture)==1:
    print('ФОТКА ЗАГРУЖЕНА')
    PictureName=array_name_picture[0] + ".png"
else:
    print('не найдено изображений с расширением .png')
    
       
try:
    img = cv2.imread(sys.path[0]+"\\"+PictureName) 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    config= r'--oem 3 --psm 6'
    #print(str(pytesseract.image_to_string(img,config=config)))                         #вывод полученного текста в консоль

    text_file = open(sys.path[0] + "\\text.txt", "w",encoding = 'utf-8-sig')
    text_file.write(str(pytesseract.image_to_string(img,config=config)))
    text_file.close()
    print("Программа выполнилась успешно")
except Exception as e:
    print('ERROR!!!', e)

