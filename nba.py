import csv

def csv_to_dict(csv_file):
    result = {}
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')  # Specify the delimiter as ';'
        for row in reader:
            key = row.pop('Player')  # Assuming 'Player' column contains unique keys
            result[key] = row
    return result

# Example usage:
csv_file = 'nba.csv'
data_dict = csv_to_dict(csv_file)
print(data_dict)
