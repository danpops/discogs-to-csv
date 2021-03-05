# pip3 install discogs_client

import discogs_client
import csv

# INPUT YOUR DISCOGS USER TOKEN!
discogs_user_token = ""

if discogs_user_token == "":
    exit("Please input your user token.")

dc = discogs_client.Client("my-discogs-generator/0.1 +http://github.com/danpops",
                           user_token=discogs_user_token)

print("Hang tight... we're getting your collection...")

me = dc.identity()
items_in_collection = [r.release for r in me.collection_folders[0].releases]
rows = []

print("Alright, now we're crunching your data...")
for r in items_in_collection:
    row = {}

    try:
        row['primaryGenre'] = r.genres[0]
        if len(r.genres) > 1:  # if album has more than 1 genre
            row['secondaryGenres'] = ", ".join(r.genres[1:])

        row['primaryStyle'] = r.styles[0]
        if len(r.styles) > 1:  # if album has more than 1 style
            row['secondaryStyles'] = ", ".join(r.styles[1:])

        row['catalogNumber'] = r.labels[0].data['catno']
        row['artists'] = ", ".join(a.name for a in r.artists)
        row['format'] = r.formats[0]['descriptions'][0]

    except (IndexError, TypeError):
        None
        # ideally, these exceptions only occur when data is missing
        # but usually the program checks if values are missing, rather than
        # ignoring any exception resulting from trying

    row['title'] = r.title

    if r.year > 0:
        row['year'] = r.year

    rows.append(row)

print("Got what I needed! Now I'll write your CSV...")

# write to CSV file called 'collection.csv'
with open('collection.csv', 'w') as csvfile:
    csvfile.write('\ufeff')  # utf8 BOM needed to run Excel

    fieldnames = ['format', 'primaryGenre', 'primaryStyle', 'secondaryGenres',
                  'secondaryStyles', 'catalogNumber', 'artists', 'title', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='')

    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print("All done! Happy collecting :)")
