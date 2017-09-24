
import csv
print('starting..')
node_data_directory = 'osm_node_data_per_zipcode' # we create new directory
if not os.path.exists(node_data_directory):
    os.makedirs(node_data_directory)

directory = 'osm_node_data'  # directory of the script above  
file_name = 'locations2017-09-22_1.csv' ## this is the result of the script above
if platform.system() == 'Windows':
    newline=''
else:
    newline=None
    
l = []    
csv_path = os.path.join('./'+directory, file_name)
spamReader = csv.reader(open(csv_path, newline=newline), delimiter=',', quotechar='|')
for row in spamReader:
    zip = row[2]
    if (len(zip) < 6):
        zip_csv_path = os.path.join('./'+node_data_directory, zip.strip()+'.csv')
        with open(zip_csv_path, 'a', newline=newline, encoding='utf-8') as f:
            output_writer = csv.writer(f)

            #if(not zip in l):
                #output_writer.writerow(['idx','street','postcode','housenumber','lon','lat'])
                #l.append(zip)



            output_writer.writerow(row)
        
print('-done')