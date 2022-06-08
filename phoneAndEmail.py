#phoneAndEmail.py - находит телефнные номера и адреса электронной почты в буффере обмена
import pyperclip, re

# Создание регулярного выражения для номеров телефона.
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                  # территориальный код
(\s|-|\.)?                          # разделитель
(\d{3})                             # первые 3 цифры
(\s|-|\.)?                           # разделитель
(\d{4})                             # последние 4 цифры
(\s*(ext|x|ext.)\s*(\d{2,5}))?     # дополнительный номер
)''', re.VERBOSE)

# Создание регулярного выражения для адресов электронной поты.
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+           # имя пользователя
@                           # символ @
[a-zA-Z0-9.-]+              # имя домена
(\.[a-zA-Z]{2,4})          # остольная часть домена
)''', re.VERBOSE)

# Поиск соответсвий в тексте, содержащемся в буффере обмена.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Копирование результатов в буффер обмена.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буффер обмена: ')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены')

