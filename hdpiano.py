infile = open('Browse by Difficulty - HDpiano.txt', 'r', encoding='windows-1251')

# for txtline in infile:
#     print(txtline)


line = 'dummy'
while line:
    try:
        line = infile.readline()
    except UnicodeDecodeError:
        print(UnicodeDecodeError)
    else:
        if line.find('hdpiano.com/lesson') != -1:
            split_line = line.split('/')
            title_artist = split_line[-2].replace('-', ' ').title().strip()
            listx = title_artist.split(' By ')
            title = listx[0]
            if len(listx) == 2:
                artist = listx[1]
            else:
                artist = ' '
            print(title, '-', artist)
infile.close()

# for item in txt.split('\n'):
#     # print(item)
#     title = item.split('by')[0]
#     artist = item.split('>')[-2][:-3]
#     print(title + '- ' + artist)
