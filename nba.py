import csv

def csv_to_dict(csv_file):
    result = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            key = row.pop('Rk')
            result[key] = row
    return result

csv_file = 'nba.csv'
data = csv_to_dict(csv_file)

def merge_binary():
    tempdict = []
    tempdict.append([data["1"]["Player"],data["1"]['PTS']])
    #tempdict.append([data["2"]["Player"],data["2"]['PTS']])
    #print(tempdict)
    for i in range(len(data)):
        current = [data[f"{i+1}"]["Player"],data[f"{i+1}"]["PTS"]]
        for i in range(len(tempdict)):
            if current in tempdict:
                pass
            else:
                spot = binary_spot_search(current, tempdict)

def binary_spot_search(value, dict):
    found = False
    while not found:
        unchange = dict
        length = len(dict)
        pos = length//2
        middle = dict[pos]
        print("middle ", middle)
        print(value[1], middle[1])

        if value[1] == middle[1]:
            print("value found")
            return unchange.index(middle)

        elif value[1] < middle[1]:
            print("1test")
            if len(dict) == 1:
                return unchange.index(dict[0])
            dict = dict[:pos]

        elif value[1] > middle[1]:
            print("2test")
            if len(dict) == 1:
                return unchange.index(dict[0])+1
            dict = dict[pos:]



merge_binary()