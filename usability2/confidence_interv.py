import csv

with open("all_seasons.csv", newline="") as csvfile:
    height_taker = csv.reader(csvfile,delimiter='.', quotechar='e' )
    for row in height_taker:
        print(', '.join(row))