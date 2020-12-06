import os, shutil

path = 'C:/Users/username/example'

try:
    os.mkdir(path + '/Music')
except FileExistsError:
    print('Cannot create a file when that file already exists: Music')

try:
    os.mkdir(path + '/Video')
except FileExistsError:
    print('Cannot create a file when that file already exists: Video')

try:
    os.mkdir(path + '/Picture')
except FileExistsError:
    print('Cannot create a file when that file already exists: Picture')

try:
    os.mkdir(path + '/Compressed')
except FileExistsError:
    print('Cannot create a file when that file already exists: Compressed')

try:
    os.mkdir(path + '/Text')
except FileExistsError:
    print('Cannot create a file when that file already exists: Text')

try:
    os.mkdir(path + '/Office')
except FileExistsError:
    print('Cannot create a file when that file already exists: Office')

try:
    os.mkdir(path + '/Pdf')
except FileExistsError:
    print('Cannot create a file when that file already exists: Pdf')

try:
    os.mkdir(path + '/Exe')
except FileExistsError:
    print('Cannot create a file when that file already exists: Exe')

try:
    os.mkdir(path + '/Racket')
except FileExistsError:
    print('Cannot create a file when that file already exists: Racket')


for file in os.listdir(path):
    splitted = file.rsplit('.')[-1]
    if  splitted == 'mp3':
        shutil.move(path + '/' + file , path + '/Music')
    if splitted == 'mp4' or splitted == 'avi' or splitted == 'mpeg' or splitted == '3gp' or splitted == 'm3u' or splitted == 'm4a' or splitted == 'mkv':
        shutil.move(path + '/' + file , path + '/Video')
    if splitted == 'png' or splitted == 'jpeg' or splitted == 'jpg' or splitted == 'gif' or splitted == 'bmp':
        shutil.move(path + '/' + file , path + '/Picture')
    if splitted == 'zip' or splitted == 'rar' or splitted == '7z' or splitted == 'ZIP':
        shutil.move(path + '/' + file , path + '/Compressed')
    if splitted == 'txt':
        shutil.move(path + '/' + file , path + '/Text')
    if splitted == 'csv' or splitted == 'doc' or splitted == 'docx' or splitted == 'accdb' or splitted == 'pptx' or splitted == 'pub' or splitted == 'rtf' or splitted == 'xls' or splitted == 'xlsx':
        shutil.move(path + '/' + file , path + '/Office')
    if splitted == 'pdf':
        shutil.move(path + '/' + file , path + '/Pdf')
    if splitted == 'exe' or splitted == 'msi':
        shutil.move(path + '/' + file , path + '/Exe')
    if splitted == 'rkt':
        shutil.move(path + '/' + file , path + '/Racket')
    else:
        print('Can not find the file type.')


