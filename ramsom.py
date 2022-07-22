#!/usr/bin/env python
#_*_coding: utf8_*_

import os

user = os.environ['USERNAME']
# home = "C:/Users/jhong/OneDrive/Escritorio/appspy/curso/app por mi/Introduccion al hacking/carpeta"
home = "C:/Users/" + user
os.chdir(home)
carpetas = os.listdir()
carpetas = [x for x in carpetas if not x.startswith(".")]

# for c in carpetas:
#     print(c)
#print(carpetas)

extInput = input("Extension: ")

extensiones = ["." + extInput]

# extensiones = [".img", ".jpg", ".jpeg", ".png"]

def discover():
    file_list = open('file_list','w')
    for carpeta in carpetas:
        ruta = home+'/'+carpeta
        for extension in extensiones:
            for rutabs, directorio, archivo in os.walk(ruta):
                for file in archivo:
                    if file.endswith(extension):
                        file_list.write(os.path.join(rutabs, file)+"\n")
    file_list.close()

def main():
    discover()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
