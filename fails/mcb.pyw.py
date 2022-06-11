import shelve, pyperclip, sys

# Использование: py.exe msb.pyw save <ключевое слово> - Сохраняет буфер обмена в ключевое слово.
#                py.exe msb.pyw <ключевое слово> - Загружает ключевое слово в буффер обмена.
#                py.exe msb.pyw list - Загружает все ключевые слова в буфер обмена.

msbshelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    msbshelf[sys.argv[2]] = pyperclip.past()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(msbshelf.keys())))
    elif sys.argv[1] in msbshelf:
        pyperclip.copy(msbshelf[sys.argv[1]])


msbshelf.close()
