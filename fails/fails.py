import os
from io import open

print(os.getcwd())                  # показать коталог
os.chdir('C:\\Windows\\System32')   # изменть текущий коталог
print(os.getcwd())
#os.makedirs(r'C:\Users\AlexF\Desktop\pythonFail')
os.chdir(r'C:\Users\AlexF\Desktop\pythonFail')
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('C:\\Windows', 'C:\\'))
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
print(os.getcwd())
path = r'C:\Users\AlexF\Desktop\pythonFail'
print(os.path.basename(path))
print(os.path.dirname(path))
calcFilePath = r'C:\Users\AlexF\Desktop\pythonFail'
print(os.path.split(calcFilePath))
print(calcFilePath.split(os.path.sep))

print(os.path.getsize(r'C:\Users\AlexF\Desktop\FoundPy\Scripts\activate_this.py'))
print(os.listdir(r'C:\Users\AlexF\Desktop\FoundPy\Scripts'))

totalSize = 0
for filename in os.listdir(r'C:\Users\AlexF\Desktop\FoundPy\Scripts'):
    totalSize += os.path.getsize(os.path.join(r'C:\Users\AlexF\Desktop\FoundPy\Scripts', filename))
print(totalSize)

print(os.path.exists(r'C:\Windows'))
print(os.path.exists(r'C:\some'))
print(os.path.isdir(r'C:\Windows\System32'))
print(os.path.isfile(r'C:\Windows\System32'))
print(os.path.isdir(r'C:\Windows\System32\calc.exe'))
print(os.path.isfile(r'C:\Windows\System32\calc.exe'))


helloFile = open(r'C:\Users\AlexF\Desktop\hello.txt', 'r')
print(helloFile.read())
helloFile.close()

sonnet = open(r'C:\Users\AlexF\Desktop\sonnet29.txt', 'r')
print(sonnet.readlines())
sonnet.close()

baconFile = open(r'C:\Users\AlexF\Desktop\bacon.txt', 'w')
baconFile.write('Hello, World!\n')
baconFile.close()

baconFile = open(r'C:\Users\AlexF\Desktop\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable')
baconFile.close()

baconFile = open(r'C:\Users\AlexF\Desktop\bacon.txt', 'r')
print(baconFile.readlines())
baconFile.close()