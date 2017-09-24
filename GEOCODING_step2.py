from osmread import parse_file, Node
import os
import csv
import platform
  
i = 0
def decode_node_to_csv():
    for entry in parse_file('./data/denmark-latest.osm'):
        if (isinstance(entry, Node) and 
            'addr:street' in entry.tags and 
            'addr:postcode' in entry.tags and 
            'addr:housenumber' in entry.tags):

            yield entry

file_name = 'locations2017-09-22_1.csv'
csv_path = os.path.join(os.getcwd(), file_name)
print('start..')
if platform.system() == 'Windows':
    newline=''
else:
    newline=None
with open(csv_path, 'w', newline=newline, encoding='utf-8') as f:
    output_writer = csv.writer(f)
    lr = ['idx','street','postcode','housenumber','lon','lat']
    output_writer.writerow(lr)
    for idx, decoded_node in enumerate(decode_node_to_csv()):

        output_writer.writerow([idx,decoded_node.tags['addr:street'], decoded_node.tags['addr:postcode'], decoded_node.tags['addr:housenumber'],decoded_node.lon,decoded_node.lat]) 

    
print('done')
print (i)