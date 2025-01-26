import csv,os

with open("100MostStreamedSongs.csv", encoding='utf-8') as file:
  reader=csv.DictReader(file)
  for row in reader:
    dir=os.listdir()
    artist=row["Artist(s)"]
    if artist not in dir:
      os.mkdir(artist)
