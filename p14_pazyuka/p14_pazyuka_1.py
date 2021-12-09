import csv
with open('Christmas_Songs.csv', 'w', newline='') as csvfile:
    songs = ['All I Want for Christmas Is You', 'Merry Christmas Everyone','Jingle Bell Rock', 'Blue Christmas',
             'Last Christmas', 'I Wish It Could Be Christmas Everyday']
    years = ['1994','1985','1957','1964','1984','1973']
    fieldnames = ['Song', 'Year']
    d = [{'Song':songs[i], 'Year' : years[i]} for i in range(len(songs))]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(d)):
        writer.writerow(d[i])


with open('Christmas_Songs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['Song'], row['Year'])

