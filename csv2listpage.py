import csv

# "query.csv" is a export from wikidata listing settlements with
# itemLabel and  article's

def main():
    prevletter = "A"
    print ("=="+prevletter+"==")
    with open('query.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            article = row['article'].split("/")[-1].strip()
            item = row['itemLabel'].strip()
            if (row['article'] == "") or (article == item):
                wikiline = ("*[[" + row['itemLabel']+"]]")
            else:
                wikiline = ("*[[" + article +"|" + item.replace("_"," ") +"]]")
            if row['itemLabel'][0] != prevletter:
                prevletter = row['itemLabel'][0]
                print ("")
                print ("=="+prevletter+"==")
            print(wikiline)

main()