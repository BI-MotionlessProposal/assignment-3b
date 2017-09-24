import os
import re
import csv
import platform
import pandas as pd
import matplotlib.pyplot as plt

if platform.system() == 'Windows':
    newline = ''
else:
    newline = None

csv_path = os.path.join('./', 'boliga_all_detailed_address.csv')

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
            mask = df.loc[(df.street == str(row[
                                                12]))]  # & ( df.housenumber == str(row[13] )) ]#) & (df.housenumber == row[13]) & (df.street  == row[12] ))
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
