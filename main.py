import csv,os

with open("100MostStreamedSongs.csv", encoding='utf-8') as file:
  reader=csv.DictReader(file)
  for row in reader:
    dir=os.listdir()
    artist=row["Artist(s)"].title()
    if artist not in dir:
      os.mkdir(artist)
    song=row["Song"]
    path_way=os.path.join(f"{artist}/",song)
    f=open(path_way,'w')
    f.close()