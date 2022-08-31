# Zaimportuj niezbędne biblioteki
import json,csv,sys,argparse

#Przekazywanie parametrów za pomocą argumentów podawanych przy uruchomieniu programu
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--Output", help = "Pass the output file")
parser.add_argument("-i", "--Input", help = "Pass the input file")
args = parser.parse_args()
if args.Output:
    print("Displaying Output as: ", args.Output)
if args.Input:
    print('Displaying Input as:', args.Input)

# Wyświetl przekazywane parametry
print("\nArguments passed:", end = " ")

source_file = 'list_of_resources.json'
source_file_sys = sys.argv[4]
print(source_file_sys)
dest_file = 'resources_excel_readable_2.csv'
dest_file_sys = sys.argv[2]
print(dest_file_sys)
resources = json.load(open(source_file))
keys_resources = list(resources['resources'][0].keys())
values_resources = list(resources['resources'][0].values())

# Usuń pierwszy element ze zmiennej systemowej
sys.argv[1:]
n = len(sys.argv)
# Wyświetl ścieżkę programu
print(sys.argv[0])
# Wyświetl ilość elementów w zmiennej systemowej
print(str(sys.argv))
print("Count of elements in env var: ", len(sys.argv))
for i in range(1, n):
    print(sys.argv[i], end = " ")
print('Keys from resources: ',keys_resources)
print('Values from resources: ',values_resources)

# Kodowanie znaków ustala się w metodzie otwierającej plik docelowy
with open(dest_file, 'w', newline='', encoding='utf-8') as outfile1:
    # Delimiter pomiędzy obiektami (wartościami) ustala się przy tworzeniu zmiennej writer
    writer1 = csv.DictWriter(outfile1, fieldnames=keys_resources, delimiter=';', dialect='excel', quoting=csv.QUOTE_MINIMAL, restval='')
    try:
        for key, values in resources.items():
            writer1.writeheader()
            writer1.writerows(values)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format('errors.json', writer1.line_num, e))  
outfile1.close()

