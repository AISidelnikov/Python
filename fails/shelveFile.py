import shelve

# shelveFile = shelve.open(r'C:\Users\AlexF\Desktop\mydata')
# cats = ['zophie', 'pooka', 'simon']
# shelveFile['cats'] = cats
# shelveFile.close()

shelveFile = shelve.open(r'C:\Users\AlexF\Desktop\mydata')
print(type(shelveFile))
print(shelveFile['cats'])
shelveFile.close()

shelveFile = shelve.open(r'C:\Users\AlexF\Desktop\mydata')
print(list(shelveFile.keys()))
print(list(shelveFile.values()))
shelveFile.close()

