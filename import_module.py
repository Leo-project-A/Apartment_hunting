import csv

RESULT_FILE = 'apartment_listings'
HEADERS = ['item_id', 'address', 'area', 'rooms', 'floor', 'squareMeter', 'price']

def import_data(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(row)
                line_count += 1
        print(f'Processed {line_count} lines.')

def unload_data(data, file_format):
    filename = '.'.join([RESULT_FILE, file_format])
    ## CSV FILE
    if file_format == 'csv':
        with open(filename, 'w',encoding = 'utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer = csv.DictWriter(file, fieldnames=HEADERS)   
            
            writer.writeheader()
            writer.writerows(data)
