import os
import re

phoneNumberRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('Мой номер телефона: (415)-555-4242.')
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

heloRegex = re.compile(r'Batman|Tina Fey')
mo = heloRegex.search('Batman and Tina Fey')
print(mo.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile потерял колесо')
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('Two Adventures of Batman')
print(mo.group())

phoneNumberRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('Мой номер телефона: 555-4242.')
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')
mo == None
print(mo.group())

phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{3,4}')
mo = phoneNumberRegex.search('Мой номер телефона: 415-555-4242.')
print(mo.group())


phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{3,4}')
mo = phoneNumberRegex.findall('Позвони мен завтра по номеру 415-555-1011. 415-555-9999 - это телефонный номер моего офиса.')
print(mo)

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies')
print(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

beginsWithHello = re.compile(r'Hello')
mo = beginsWithHello.search('Hello World!')
print(mo.group())

endsWithNumber = re.compile(r'\d+$')
mo = endsWithNumber.search('You number is 42')
print(mo.group())

bginsandendsWithNumber = re.compile(r'^\d+$')
mo = bginsandendsWithNumber.search('1234567890')
print(mo.group())

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To server man> for dinner')
print(mo.group())

noNewlineRegex = re.compile('.*', re.DOTALL)
print(noNewlineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the low.').group())