openfile = open('best1.txt', 'r')
user = openfile.readlines()
print(user)

file = open("nieuw_bestand.txt", 'w')
for i in user:
    if i != '\n':
        i.strip()
        file.write(i)