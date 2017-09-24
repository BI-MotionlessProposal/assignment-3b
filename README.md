The geocoding with help of the OSM dataset stored in CSV files in the osm_node_data folder (116MB). The data contains 2474455 nodes out of 2475388 nodes in the OSM data.

In the folder osm_node_data_per_zipcode the data is devided up in one CSV file per zipcode (some data is missing because of an error)

The CSV columns in these files are: 
- idx,
- street,
- postcode,
- housenumber,
- lon,
- lat



boliga_all_detailed_address.csv (28.2 MB)- contains boliga data with 3 additional columns 

The CSV columns in these files are: 
- address,
- zip_code,
- price,
- sell_date,
- sell_type,
- price_per_sq_m,
- no_rooms,
- housing_type,
- size_in_sq_m,
- year_of_construction,
- price_change_in_pct,
- aktuel_vardi
- street,
- housenumber,
- postcode


```python

%matplotlib notebook


import pandas as pd
import matplotlib.pyplot as plt

complete_data = './boliga_all.csv'

df = pd.read_csv(complete_data)
df.head()
#df.info()
df.describe()
df.price

df[['price']].head()

#df['price'].plot()
print s
```

Geocode the entire dataset of Danish housing sales data, see Assignment 2. 
Add two new columns to the DataFrame, one for latitude (lat) and one for longitude (lon) coordinates per address. 
Do the geocoding with help of the OSM dataset stored in a file as discussed in class. Save that DataFrame to a CSV file with the help of pandas'

#### Our solution to this:
##### Step 1

```python
%%bash 
wget --directory-prefix=./data/ http://download.geofabrik.de/europe/denmark-latest.osm.bz2
bzip2 -d ./data/denmark-latest.osm.bz2
```

##### Step 2

This script was divided into two files in reality to handle the big data. But the script below creates just one.


```python
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

```
#### step 3
This script chunks up the osm data into CSV files for every postcode. The files are stored in a folder called osm_node_data.
The name of the file is the postcode.
The reason to chunk up the osm data by postcode is to be able to hold the osm data in a panda DataFrame without using too much RAM memory. 

```python


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
```
#### step 4


```python

%matplotlib notebook
import os
import re
import csv
import platform
import pandas as pd
import matplotlib.pyplot as plt




import pandas as pd
import matplotlib.pyplot as plt

## (The import is not 100% correct we import more than we need)

# Functions that extract values with regex
def get_gc_street(a):
    #if(a[:0] == '"'):
    reg_exp = re.compile(r'^("*)([^0-9]*)(\s)(\d*)')
    mo = reg_exp.search(a)
    mo.groups()
    
    r = mo.group(2)
    if (type(r) == str):
        return r.strip()
    else:
        return 'none'


def get_gc_street_no(a):
    
    reg_exp = re.compile(r'^("*)([^0-9]*)(\s)(\w*)')
    mo = reg_exp.search(a)
    r = mo.group(4)
    if (type(r) == str):
        r.strip
        if ( len( r ) > 4):        
            r = r[:-4]
            stopwords = ['TV','TH','ST','MF']
            for w in stopwords:            
                 r = r.replace(w, '')    
        return r

    else:
        return 'none'

def get_gc_zipcode(a):
    a = str(a)
    try:

        reg_exp = re.compile(r'(\d{4})([^0-9]*)$')
        mo = reg_exp.search(a)
        mo.groups()
        r = mo.group(1)
        if (type(r) == str):
            return r.strip()
        else:
            return 'none'
    except:
        return 'except'

def get_gc_city(a):
    
    reg_exp = re.compile(r'(\d{4})([^0-9]*)$')
    mo = reg_exp.search(a)
    mo.groups()
    r = mo.group(2)
    if (type(r) == str):
        return r.strip()
    else:
        return 'none'


   
print('start..')
        


if platform.system() == 'Windows':
    newline=''
else:
    newline=None
    
l = []    
csv_path = os.path.join('./', 'boliga_all.csv') # All boliga data that was scraped in Assignment 2

spamReader = csv.reader(open(csv_path, newline=newline))
for idx, row in enumerate(spamReader):
    if(len(row)<2):
         continue
    
    if (idx == 0):
        row.append('street')    
        row.append('housenumber') 
        row.append('postcode')

    else:        
        a = row[0]
        row.append(get_gc_street(a))
        row.append(get_gc_street_no(a))        
        row.append(get_gc_zipcode(a))


        zip_csv_path = os.path.join('./', 'boliga_all_detailed_address.csv')
        with open(zip_csv_path, 'a', newline=newline, encoding='utf-8') as f:
            output_writer = csv.writer(f)

            #if(not zip in l):
            output_writer.writerow(row)
                #l.append(zip)

print('done') 
```
                       


A remark: This script needs more robustness to handle errors when RedEx fails. 
Unfortunately, the script could not run to completeness because of an exception error so we ended up with a large but incomplete boliga_all_detailed_address.csv file.


#### step 5

```python
import os
import re
import csv
import platform
import pandas as pd
import matplotlib.pyplot as plt

if platform.system() == 'Windows':
    newline = ''
else:
    newline=None
    
csv_path = os.path.join('./', 'boliga_all_detailed_address.csv') # Our boliga data with street, housenumber and postcode


spamReader = csv.reader(open(csv_path, newline=newline))
for idx, row in enumerate(spamReader):
    if (len(row) < 2):
        continue

    if (idx == 0):
        row.append('lon')
        row.append('lat')
        continue

    else:
        a = row[12] + ' ' + row[13] + ' ' + row[14]  # 12 is street, 13 is housenumber 14 is postcode

        # print(a)
        # break
        zip_csv_path = os.path.join('./osm_node_data_per_zipcode', row[14] + '.csv')
        # print(zip_csv_path)


        if (os.path.isfile(zip_csv_path)):

            df = pd.read_csv(zip_csv_path)

            mask = df.loc[(df.street == str(row[12]))]  # & ( df.housenumber == str(row[13] )) ]#) & (df.housenumber == row[13]) & (df.street  == row[12] ))
            #
            # mask = df[(df['postcode'] == str(row[13]) ) & (df['street'] == str(row[12]))]

            if mask.lat.values.__len__() > 0:
                print(mask.lat.values[1])
                print(mask.lon.values[1])
                row.append(mask.lat.values[1])
                row.append(mask.lon.values[1])

                zip_csv_path = os.path.join('./', 'boliga_all_detailed_lon_lat.csv')
                with open(zip_csv_path, 'a', newline=newline, encoding='utf-8') as f:
                    output_writer = csv.writer(f)

                    output_writer.writerow(row)

print('done')


```


#Over all remark    
Geo-coding the osm took quite a long time with osmread, which was written in the lecture notes. 
But the problem wasn't with the library but that we got errors due to lack of server resources. 
We didn't have enough resources and kept getting the error "The kernel appears to have died. It will restart automatically." after 2474455 nodes.
2475387 nodes should be correct.



?


 ## Find the average price per square meter 
The group_zip_price.py file loops through all the zip codes and calculates the average price per area for the years 1992 and 2016. (Run from the root of the project [python group_zip_price.py ] ) the script loops through the files in the data folder. if only some areas need to be calcultated clean the directory, place only the coresponding files in the data folder and run the group_zip_price.py  script.


##Distance from Roskilde
Due to some corrupt data in our CSV files we calculated the distance from roskilde for a very small dataset. The python script that calculates the distance is distances_from_roskilde.py and reads entries from the boliga_all_detailed_lon_lat.csv dataset then loops through the rows and calculates the distances from the static point beeing the center of roskilde festival and the end point the current house entry.



 
